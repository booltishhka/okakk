import os
import math


def f(x):
    return 100 * math.sqrt(abs(1 - 0.01 * x ** 2)) + 0.01 * abs(x + 10)


def main():
    # Параметры расчета
    x_start = -15
    x_end = 5
    step = 0.1

    # Создаем папку для результатов
    results_dir = "results"
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)

    # Вычисляем значения функции
    x_values = []
    y_values = []
    current_x = x_start
    while current_x <= x_end:
        x_values.append(current_x)
        y_values.append(f(current_x))
        current_x = round(current_x + step, 2)  # Более точное округление

    # Сохраняем результаты в файл
    results_file = os.path.join(results_dir, "results.txt")
    with open(results_file, 'w') as file:
        for x, y in zip(x_values, y_values):
            file.write(f"{x:.4f}\t{y:.4f}\n")

    print(f"Данные сохранены в файл: {results_file}")

    # Пытаемся построить график (если установлен matplotlib)
    try:
        import matplotlib.pyplot as plt

        plt.figure(figsize=(10, 6))
        plt.plot(x_values, y_values, color='blue', linewidth=2)
        plt.title('График функции y = 100√|1−0.01x²| + 0.01|x+10|')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)

        plot_file = os.path.join(results_dir, "function_plot.png")
        plt.savefig(plot_file)
        print(f"График сохранен как: {plot_file}")

        # Пытаемся показать график
        try:
            plt.show()
        except:
            print("Не удалось отобразить график, но он сохранен в файл")

    except ImportError:
        print("\nДля построения графика необходимо установить matplotlib")
        print("Установите его командой: pip install matplotlib")
        print("Текстовые результаты доступны в файле results.txt")


if __name__ == "__main__":
    main()
