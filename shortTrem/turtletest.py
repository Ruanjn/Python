from turtle import*
import numpy as np


def square(x, y):
    up()
    goto(x, y)
    down()
    for i in range(4):
        forward(340)
        right(90)


def c(r, x, y):
    up()
    goto(x, y)
    down()
    circle(r)


def wheel(br, inter, angle, model):
    if model ==1:
        times = 360/angle
        up()
        goto(0, -br)
        down()
        for _ in range(2*times):
            goto(, )
            goto(, )


def sunflowe(n, x, y):
    up()
    y = 180-y
    goto(-x/2, -(x/2)/np.tan(y/2*(np.pi/180)))
    down()
    for _ in range(n):
        forward(x)
        # print(position())
        left(y)


tracer(6, 10)
speed(10)
# sunflowe(50, 150, 27)
setheading(0)
# Turtle()
# goto(0, 0)
# heading()
# goto(-170, 170)
# square(-170, 170)
# right(45)
# square(0, 240)
# c(240, -170, -170)
# left(45)
#
# up()
# goto(0, -200)
# down()
# circle(200, 360, 3)
# c(170, 0, -170)
# c(155, 0, -155)
# c(100, 0, -100)
# c(85, 0, -85)
# c(15, 0, -15)
# c(255, 0, -255)
# hideturtle()
done()


