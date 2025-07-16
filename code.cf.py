import math
import turtle

def f(x):
    return 100 * math.sqrt(abs(1 - 0.01 * x ** 2)) + 0.01 * abs(x + 10)


screen = turtle.Screen()
screen.setup(800, 600)
screen.title("График функции")

t = turtle.Turtle()
t.speed(0)
t.penup()


t.goto(-300, 0)
t.pendown()
t.goto(300, 0)
t.penup()
t.goto(0, -200)
t.pendown()
t.goto(0, 200)
t.penup()


x = -15
t.goto(x * 20, f(x) - 200)
t.pendown()
while x <= 5:
    t.goto(x * 20, f(x) - 200)
    x += 0.1

turtle.done()

