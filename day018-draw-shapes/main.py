from turtle import Turtle, Screen
t = Turtle()
t.shape("turtle")
# 삼각형에서 십각형 그리기

for i in range(3, 10):
    for j in range(0, i):
        t.forward(100)
        t.right(360 / i)


s = Screen()
s.exitonclick()