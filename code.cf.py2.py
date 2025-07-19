import argparse
import json
import matplotlib.pyplot as plt
import os
import sys


def load_data(filename):
    """Загрузка данных из JSON файла"""
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Ошибка: Файл '{filename}' содержит некорректные JSON данные")
        sys.exit(1)


def plot_function(data, args):
    """Построение графика функции с учетом параметров"""
    plt.figure(figsize=args.figsize)

    x = data['x_values']
    y = data['y_values']


    line, = plt.plot(x, y,
                     label=data.get('function', 'y = f(x)'),
                     color=args.color,
                     linewidth=args.linewidth,
                     linestyle=args.linestyle)


    if args.fill:
        plt.fill_between(x, y, color=args.fill_color, alpha=args.fill_alpha)


    plt.title(args.title if args.title else data.get('function', 'График функции'))
    plt.xlabel(args.xlabel if args.xlabel else 'x')
    plt.ylabel(args.ylabel if args.ylabel else 'y')
    plt.grid(args.grid)

    if args.legend:
        plt.legend()


    if args.output:
        os.makedirs(os.path.dirname(args.output), exist_ok=True)
        plt.savefig(args.output)
        print(f"График сохранен в файл: {args.output}")
    else:
        plt.show()


def parse_arguments():
    """Разбор аргументов командной строки"""
    parser = argparse.ArgumentParser(description='Визуализация графика функции из JSON файла')


    parser.add_argument('input_file',
                        help='Путь к JSON файлу с данными функции')


    parser.add_argument('--color', '-c',
                        default='blue',
                        help='Цвет линии графика (по умолчанию: blue)')

    parser.add_argument('--linewidth', '-lw',
                        type=float, default=1.5,
                        help='Толщина линии (по умолчанию: 1.5)')

    parser.add_argument('--linestyle', '-ls',
                        default='-',
                        choices=['-', '--', '-.', ':'],
                        help='Стиль линии (по умолчанию: "-")')


    parser.add_argument('--fill', '-f',
                        action='store_true',
                        help='Включить заливку под кривой')

    parser.add_argument('--fill-color', '-fc',
                        default='lightblue',
                        help='Цвет заливки (по умолчанию: lightblue)')

    parser.add_argument('--fill-alpha', '-fa',
                        type=float, default=0.3,
                        help='Прозрачность заливки (0-1, по умолчанию: 0.3)')


    parser.add_argument('--title', '-t',
                        help='Заголовок графика')

    parser.add_argument('--xlabel', '-xl',
                        help='Подпись оси X')

    parser.add_argument('--ylabel', '-yl',
                        help='Подпись оси Y')

    parser.add_argument('--grid', '-g',
                        action='store_true',
                        help='Включить сетку')

    parser.add_argument('--no-legend',
                        dest='legend',
                        action='store_false',
                        help='Отключить легенду')


    parser.add_argument('--figsize', '-fs',
                        nargs=2, type=float, default=[10, 6],
                        metavar=('WIDTH', 'HEIGHT'),
                        help='Размер графика в дюймах (по умолчанию: 10 6)')


    parser.add_argument('--output', '-o',
                        help='Сохранить график в файл (вместо отображения)')

    return parser.parse_args()


def main():
    args = parse_arguments()
    data = load_data(args.input_file)
    plot_function(data, args)


if __name__ == "__main__":
    main()