import argparse
import json
import matplotlib.pyplot as plt


def main():
    # Настройка парсера аргументов
    parser = argparse.ArgumentParser(description='Построение графика из JSON файла')
    parser.add_argument('file', help='Файл с данными (JSON)')
    parser.add_argument('--fill', action='store_true', help='Залить область под графиком')
    parser.add_argument('--color', default='blue', help='Цвет графика')
    parser.add_argument('--output', help='Сохранить график в файл')
    args = parser.parse_args()

    # Загрузка данных
    try:
        with open(args.file) as f:
            data = json.load(f)
        x = data['x_values']
        y = data['y_values']
    except Exception as e:
        print(f"Ошибка загрузки файла: {e}")
        return

    # Построение графика
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, color=args.color, label=data.get('function', 'y = f(x)'))

    if args.fill:
        plt.fill_between(x, y, color=args.color, alpha=0.2)

    # Оформление
    plt.title(data.get('function', 'График функции'))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()

    # Вывод или сохранение
    if args.output:
        plt.savefig(args.output)
        print(f"График сохранен в {args.output}")
    else:
        plt.show()


if __name__ == "__main__":
    main()