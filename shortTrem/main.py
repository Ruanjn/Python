import turtle
import random

l = random.randint(1, 19)
x = turtle.Turtle()
j = 0
turtle.tracer(20)
# x.tracer(20)
x.speed(0)
x.penup()
for i in range(360):
    x.goto(0, 0)
    x.setheading(5 * i)
    x.forward(100)
    x.left(j)
    x.pendown()
    x.forward(60)
    x.penup()
    j = j + l
    x.stamp()
turtle.done()