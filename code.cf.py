import os
import json
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 100 * np.sqrt(np.abs(1 - 0.01 * x**2)) + 0.01 * np.abs(x + 10)


results_dir = 'results'
if not os.path.exists(results_dir):
    os.makedirs(results_dir)


x_start = -15
x_end = 15
step = 0.1


x_values = np.arange(x_start, x_end + step, step)
y_values = f(x_values)


results = {
    "x_values": x_values.tolist(),
    "y_values": y_values.tolist()
}

output_file = os.path.join(results_dir, 'function_values.json')
with open(output_file, 'w') as f_json:
    json.dump(results, f_json, indent=4)


plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='y = 100√(|1 - 0.01x²|) + 0.01|x + 10|', color='blue')
plt.title('График функции y = f(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.savefig(os.path.join(results_dir, 'function_plot.png'))
plt.show()

print(f"Сохранено в  '{results_dir}'")
