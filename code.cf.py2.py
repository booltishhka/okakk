# import argparse
# import json
# import matplotlib.pyplot as plt
#
#
# def main():
#     # Настройка парсера аргументов
#     parser = argparse.ArgumentParser(description='Построение графика из JSON файла')
#     parser.add_argument('file', help='Файл с данными (JSON)')
#     parser.add_argument('--fill', action='store_true', help='Залить область под графиком')
#     parser.add_argument('--color', default='blue', help='Цвет графика')
#     parser.add_argument('--output', help='Сохранить график в файл')
#     args = parser.parse_args()
#
#     # Загрузка данных
#     try:
#         with open(args.file) as f:
#             data = json.load(f)
#         x = data['x_values']
#         y = data['y_values']
#     except Exception as e:
#         print(f"Ошибка загрузки файла: {e}")
#         return
#
#     # Построение графика
#     plt.figure(figsize=(10, 6))
#     plt.plot(x, y, color=args.color, label=data.get('function', 'y = f(x)'))
#
#     if args.fill:
#         plt.fill_between(x, y, color=args.color, alpha=0.2)
#
#     # Оформление
#     plt.title(data.get('function', 'График функции'))
#     plt.xlabel('x')
#     plt.ylabel('y')
#     plt.grid(True)
#     plt.legend()
#
#     # Вывод или сохранение
#     if args.output:
#         plt.savefig(args.output)
#         print(f"График сохранен в {args.output}")
#     else:
#         plt.show()
#
#
# if __name__ == "__main__":
#     main()

import argparse
import json
import matplotlib.pyplot as plt
import os


def load_data(filename='results/function_values.json'):
    """Load x and y values from JSON file"""
    with open(filename) as f:
        data = json.load(f)
    return data['x_values'], data['y_values']


def plot_graph(x, y, fill=False, title=None, xlabel=None, ylabel=None):
    """Plot the graph with given parameters"""
    plt.figure(figsize=(10, 6))

    if fill:
        plt.fill_between(x, y, alpha=0.3)

    plt.plot(x, y, marker='o', linestyle='-')

    if title:
        plt.title(title)
    if xlabel:
        plt.xlabel(xlabel)
    if ylabel:
        plt.ylabel(ylabel)

    plt.grid(True)
    plt.show()


def main():
    parser = argparse.ArgumentParser(description='Plot graph from JSON data')
    parser.add_argument('--filename', default='results/function_values.json',
                      help='Path to JSON file with x and y values (default: results/function_values.json)')
    parser.add_argument('--fill', action='store_true', help='Fill area under the curve')
    parser.add_argument('--title', help='Title of the graph')
    parser.add_argument('--xlabel', help='Label for X axis')
    parser.add_argument('--ylabel', help='Label for Y axis')

    args = parser.parse_args()

    # Construct full path if needed
    if not os.path.isfile(args.filename):
        args.filename = os.path.join('results', args.filename)

    x, y = load_data(args.filename)
    plot_graph(x, y, args.fill, args.title, args.xlabel, args.ylabel)


if __name__ == '__main__':
    main()
