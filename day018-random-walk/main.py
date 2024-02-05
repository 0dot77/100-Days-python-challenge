import turtle
from turtle import Turtle, Screen
import random

t = Turtle()
turtle.colormode(255)
t.shape("turtle")
t.pensize(15)
s = Screen()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    color_tuple = (r,g,b)
    return color_tuple

status = 0
forward_n = 30

while status < 100:

    randomNum = random.randint(0,3)
    t.color(random_color())

    if randomNum == 0:
        t.forward(forward_n)
        t.right(90)
    elif randomNum == 1:
        t.forward(forward_n)
        t.left(90)
    elif randomNum == 2:
        t.forward(forward_n)
        t.right(-90)
    elif randomNum == 3:
        t.forward(forward_n)
        t.left(-90)

    status += 1


s.exitonclick()