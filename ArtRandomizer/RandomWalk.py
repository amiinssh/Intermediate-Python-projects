import random
import turtle as t

from main import screen

tim = t.turtles()

screen = t.Screen()


tim.speed(0)
tim.pensize(10)

directions = [0, 90 , 180 , 270]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

for _ in range(200):
    tim.color(random_color())
    tim.forward(50)
    tim.setheading(random.choice(directions))




screen.exitonclick()
