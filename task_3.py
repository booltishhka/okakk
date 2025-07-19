import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

def f(x1, x2):
    """Функция f(x1, x2) = 0.5 + (cos²(sin(|x1² - x2²|)) - 0.5) / (1 + 0.001*(x1² + x2²))²"""
    numerator = np.cos(np.sin(np.abs(x1**2 - x2**2)))**2 - 0.5
    denominator = (1 + 0.001*(x1**2 + x2**2))**2
    return 0.5 + numerator / denominator

x1 = np.linspace(-2.0, 2.0, 100)
x2 = np.linspace(-2.0, 2.0, 100)
X1, X2 = np.meshgrid(x1, x2)
Y = f(X1, X2)

x10, x20 = 0.0, 0.0
y0 = f(x10, x20)

fig = plt.figure(figsize=(16, 12))
fig.suptitle(f'Графики функции f(x₁, x₂) в точке ({x10}, {x20}), f({x10}, {x20}) = {y0:.4f}',
             fontsize=14, y=0.98)

ax1 = fig.add_subplot(221, projection='3d')
surf1 = ax1.plot_surface(X1, X2, Y, cmap=cm.viridis, linewidth=0, antialiased=True)
ax1.set_xlabel('x₁')
ax1.set_ylabel('x₂')
ax1.set_zlabel('y = f(x₁, x₂)')
ax1.set_title('3D поверхность (изометрический вид)')
fig.colorbar(surf1, ax=ax1, shrink=0.5, aspect=5)

ax2 = fig.add_subplot(222)
contour = ax2.contourf(X1, X2, Y, 20, cmap=cm.viridis)
ax2.set_xlabel('x₁')
ax2.set_ylabel('x₂')
ax2.set_title('Вид сверху (2D проекция)')
ax2.grid(True)
fig.colorbar(contour, ax=ax2, shrink=0.5, aspect=5)

ax3 = fig.add_subplot(223)
y_x1 = f(x1, x20)
ax3.plot(x1, y_x1, 'b-', linewidth=2)
ax3.set_xlabel('x₁')
ax3.set_ylabel('y = f(x₁, x₂₀)')
ax3.set_title(f'График f(x₁) при x₂ = {x20}')
ax3.grid(True)
ax3.axvline(x=x10, color='r', linestyle='--', alpha=0.5)
ax3.axhline(y=y0, color='r', linestyle='--', alpha=0.5)

ax4 = fig.add_subplot(224)
y_x2 = f(x10, x2)
ax4.plot(x2, y_x2, 'g-', linewidth=2)
ax4.set_xlabel('x₂')
ax4.set_ylabel('y = f(x₁₀, x₂)')
ax4.set_title(f'График f(x₂) при x₁ = {x10}')
ax4.grid(True)
ax4.axvline(x=x20, color='r', linestyle='--', alpha=0.5)
ax4.axhline(y=y0, color='r', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()