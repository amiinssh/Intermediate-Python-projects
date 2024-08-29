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
    return (r, g, b)

def draw_shape():
    num_of_sides = 3
    angle = 360 / num_of_sides
    for _ in range(num_of_sides < 10):
        color = random_color()
        tim.pencolor(color)
        tim.forward(100)
        tim.right(angle)
        num_of_sides += 1

draw_shape()
tim.color(random_color())
screen = tim.screen()
screen.exitonckick()