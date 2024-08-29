import turtle
import random

screen = turtle.Screen()

turtle.colormode(255)

tim = turtle.Turtle()
tim.shape("classic")
tim.color("black")

tim.speed(0)

tim.hideturtle()

bottom_left_x = -screen.window_width() // 2
bottom_left_y = -screen.window_height() // 2

tim.penup()
tim.goto(bottom_left_x, bottom_left_y)
tim.pendown()
tim.showturtle()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def draw_circles():
    radius = 30
    num_circles_per_line = 5
    num_lines = 5
    vertical_spacing = 80
    horizontal_spacing = 80

    for line in range(num_lines):
        tim.penup()
        tim.goto(bottom_left_x, bottom_left_y + line * vertical_spacing)
        tim.pendown()


        for _ in range(num_circles_per_line):
            color = random_color()
            tim.pencolor(color)
            tim.fillcolor(color)
            tim.begin_fill()
            tim.circle(radius)
            tim.end_fill()
            tim.penup()
            tim.forward(horizontal_spacing)
            tim.pendown()

        tim.hideturtle()
        tim.penup()
        tim.goto(bottom_left_x, bottom_left_y + (line + 1) * vertical_spacing)
        tim.pendown()

draw_circles()

screen.exitonclick()
