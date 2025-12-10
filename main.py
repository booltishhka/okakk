import numpy as np
from scipy.special import spherical_jn, spherical_yn
import matplotlib.pyplot as plt
C = 299792458.0
class SphereRCS:
    def __init__(self, D_input):
        self.r = D_input / 2.0
        print(f"Радиус сферы установлен: r = {self.r} м")
    def h_n(self, n, x):
        jn_val = spherical_jn(n, x, derivative=False)
        yn_val = spherical_yn(n, x, derivative=False)
        return jn_val + 1j * yn_val
    def calculate_sigma(self, f_hz):
        if f_hz <= 0:
            return 0.0
        lambda_val = C / f_hz
        k = 2 * np.pi / lambda_val
        kr = k * self.r
        N_max = int(np.round(kr + 4 * (kr ** (1 / 3)) + 2))
        sum_of_series = 0.0 + 0.0j
        for n in range(1, N_max + 1):
            jn_n = spherical_jn(n, kr)
            jn_n_minus_1 = spherical_jn(n - 1, kr)
            hn_n = self.h_n(n, kr)
            hn_n_minus_1 = self.h_n(n - 1, kr)
            a_n = jn_n / hn_n
            num_b = kr * jn_n_minus_1 - n * jn_n
            den_b = kr * hn_n_minus_1 - n * hn_n
            b_n = num_b / den_b
            term = ((-1) ** n) * (n + 0.5) * (b_n - a_n)
            sum_of_series += term
        sigma = (lambda_val ** 2 / np.pi) * np.abs(sum_of_series) ** 2
        return sigma
def run_simulation(D, f_min, f_max, num_points=200):
    rcs_calc = SphereRCS(D_input=D)
    frequencies = np.linspace(f_min, f_max, num_points)
    rcs_values = [rcs_calc.calculate_sigma(f) for f in frequencies]
    output_filename = "rcs_results.txt"
    header = f"Частота (Гц)    ЭПР (м^2)\n"
    data_lines = [f"{f:E}    {sigma:E}" for f, sigma in zip(frequencies, rcs_values)]
    try:
        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write(header)
            f.write('\n'.join(data_lines))
        print(f"\nДанные сохранены в файл: {output_filename}")
    except IOError as e:
        print(f"Ошибка сохранения файла: {e}")
    plt.figure(figsize=(10, 6))
    plt.plot(frequencies / 1e9, rcs_values, label=f'D = {D} м')
    plt.title("Эффективная площадь рассеяния идеально проводящей сферы")
    plt.xlabel("Частота, f (ГГц)")
    plt.ylabel("ЭПР, $\sigma$ ($м^2$)")
    plt.grid(True, which="both", ls="--")
    plt.legend()
    plt.show()
D_sphere = 25e-3
F_min = 0.01e9
F_max = 35e9
print(f"Расчет для D={D_sphere} м в диапазоне от {F_min / 1e9:.1f} ГГц до {F_max / 1e9:.1f} ГГц")
run_simulation(D_sphere, F_min, F_max)