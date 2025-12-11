import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
C = 299792458.0
ETA = 376.73
I0 = 1.0
f = 6.5e9
L_LAMBDA = 0.01
lambda_val = C / f
k = 2 * np.pi / lambda_val
l = L_LAMBDA * lambda_val
kl = k * l
print(f"--- Параметры антенны ---")
print(f"Частота (f): {f / 1e9:.2f} ГГц")
print(f"Длина волны (λ): {lambda_val:.4f} м")
print(f"Длина диполя (l): {l * 1e3:.3f} мм")
print(f"Параметр (kl): {kl:.4f}")
def E_theta_mag(theta):
    if np.isclose(theta, 0.0) or np.isclose(theta, np.pi):
        return 0.0
    numerator = np.cos(kl * np.cos(theta)) - np.cos(kl)
    denominator = np.sin(theta)
    return np.abs(numerator / denominator)
def F_squared(theta, E_max):
    e_theta = E_theta_mag(theta)
    return (e_theta / E_max) ** 2
def integrand(theta, E_max):
    return F_squared(theta, E_max) * np.sin(theta)
E_max_val = E_theta_mag(np.pi / 2.0)
integral_result, error = quad(integrand, 0, np.pi, args=(E_max_val,))
D_max_val = 4 * np.pi / (2 * np.pi * integral_result)
D_max_dB = 10 * np.log10(D_max_val)
print(f"\n--- Результаты расчетов ---")
print(f"Максимальное значение КНД (D_max) в разах: {D_max_val:.4f}")
print(f"Максимальное значение КНД (D_max) в дБ: {D_max_dB:.2f} дБ")
print(f"Аналитический D_max для короткого диполя: 1.5000 (1.76 дБ)")
num_points = 361
theta_rad = np.linspace(0, np.pi, num_points)
theta_deg = np.rad2deg(theta_rad)
F2_values = np.array([F_squared(t, E_max_val) for t in theta_rad])
D_values = F2_values * D_max_val
D_dB_values = 10 * np.log10(D_values)
plt.figure(figsize=(10, 6))
plt.plot(theta_deg, D_dB_values, label=f'$D_{{max}}$ = {D_max_dB:.2f} дБ')
plt.title(f'КНД (D) симметричного вибратора ($l/\lambda={L_LAMBDA}$) в дБ (Декартовы координаты)')
plt.xlabel('Угол $\\theta$ (градусы)')
plt.ylabel('КНД, $D(\\theta)$ (дБ)')
plt.xlim(0, 180)
plt.xticks(np.arange(0, 181, 30))
plt.grid(True, which="both", ls="--")
plt.legend()
plt.show()
D_linear_norm = D_values / D_max_val
ax = plt.subplot(111, projection='polar')
ax.plot(theta_rad, D_linear_norm, color='blue', linewidth=2)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
ax.set_rticks(np.linspace(0, 1, 5))
ax.set_yticklabels([f'{r * D_max_dB:.1f} дБ' for r in np.linspace(0, 1, 5)])
ax.set_title(f'КНД (D) симметричного вибратора ($l/\lambda={L_LAMBDA}$) в дБ (Полярные координаты)', va='bottom')
plt.show()
print("\n--- Завершение ---")