import turtle
from turtle import Turtle, Screen
import random

t = Turtle()
s = Screen()

t.shape("turtle")
t.speed(100)
turtle.colormode(255)

def random_color_n():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    color_tuple = (r,g,b)
    return color_tuple

def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        t.color(random_color_n())
        t.circle(100)
        t.setheading(t.heading() + size_of_gap)

draw_spirograph(5)


s.exitonclick()