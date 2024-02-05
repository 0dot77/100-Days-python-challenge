from turtle import Turtle, Screen

t = Turtle()
s = Screen()
t.shape("turtle")
t.color("blue")

for _ in range(30):
    t.pendown()
    t.forward(5)
    t.penup()
    t.forward(5)

s.exitonclick()