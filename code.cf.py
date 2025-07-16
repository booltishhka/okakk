import math
import turtle

def f(x):
    return 100 * math.sqrt(abs(1 - 0.01 * x ** 2)) + 0.01 * abs(x + 10)

# Настройки окна
screen = turtle.Screen()
screen.setup(800, 600)
screen.title("График функции")

t = turtle.Turtle()
t.speed(0)
t.penup()

# Рисуем оси
t.goto(-300, 0)
t.pendown()
t.goto(300, 0)
t.penup()
t.goto(0, -200)
t.pendown()
t.goto(0, 200)
t.penup()

# Рисуем график
x = -15
t.goto(x * 20, f(x) - 200)  # Масштабируем координаты
t.pendown()
while x <= 5:
    t.goto(x * 20, f(x) - 200)  # Смещаем график вниз
    x += 0.1

turtle.done()

