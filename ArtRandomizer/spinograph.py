import random
import turtle as t

from main import screen

tim = t.turtles()

screen = t.Screen()


tim.speed(0)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

for _ in range(1, 361, 3):
    radius = 30
    tim.right(5)
    tim.circle(radius)
    tim.color(random_color())



screen.exitonclick()
