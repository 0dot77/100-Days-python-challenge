import turtle

import colorgram
from turtle import Turtle, Screen
import random


t = Turtle()
s = Screen()
turtle.colormode(255)
s.setup(500,500, 100, 100)

t.shape("turtle")

rgb_colors = []
colors = colorgram.extract('image.jpeg', 6)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b

    new_color = (r,g,b)
    rgb_colors.append(new_color)

color_list = rgb_colors



for _ in range(10):
    t.penup()
    t.goto(-230, -230 + _ * 50)
    t.pendown()
    for i in range(10):
        t.color(random.choices(color_list))
        t.dot(20)
        t.penup()
        t.forward(50)
        t.pendown()


s.exitonclick()