from turtle import*
import numpy as np
import math


def polyline(n, length, angle):
    for i in range(n):
        fd(length)
        lt(angle)


def polygon(n, length):
    angle = 360.0/n
    polyline(n, length, angle)


def arc(r, angle):
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    lt(step_angle/2)
    polyline(n, step_length, step_angle)
    rt(step_angle/2)


def petal(r, angle):
    for i in range(2):
        arc(r, angle)
        lt(180-angle)


def flower(n, r, angle):
    down()
    for i in range(n):
        petal(r, angle)
        lt(360.0/n)


def move(length):
    pu()
    fd(length)
    pd()


def draw_pie(n, r):
    polypie(n, r)
    pu()
    # fd(r*2 + 10)
    pd()


def polypie(n, r):
    angle = 360.0 / n
    for i in range(n):
        isosceles(r, angle/2)
        lt(angle)


def isosceles(r, angle):
    y = r * math.sin(angle * math.pi / 180)
    rt(angle)
    fd(r)
    lt(90+angle)
    fd(2*y)
    lt(90+angle)
    fd(r)
    lt(180-angle)


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


def dot_circle(r):
    up()
    goto(0, 0)
    down()
    dot(r)


def out_flower(br, r, times):
    angle = 360/times
    if r < br*np.sin(angle/2*np.pi/180):
        return
    inner_range = br*np.cos(angle/2*np.pi/180)-np.sqrt(r*r-(br*br*np.sin(angle/2*np.pi/180)*np.sin(angle/2*np.pi/180)))
    heading_angle = np.arccos((br*br+r*r-inner_range*inner_range)/(2*br*r))*180/np.pi
    up()
    goto(0, -br)
    # circle(br)
    next_angle = -90
    down()
    for _ in range(3 * int(times)):
        setheading(next_angle+90-heading_angle)
        circle(r, angle+2*heading_angle)
        next_angle += angle
    up()


def wheel(br, inter, angle, model):
    times = 360 / angle
    up()
    goto(0, -br)
    nextangle = -90
    down()
    if model == 1:
        for _ in range(3*int(times)):
            nextangle += angle
            nextx = np.cos(nextangle*np.pi/180)*(br+inter)
            nexty = np.sin(nextangle*np.pi/180)*(br+inter)
            goto(nextx, nexty)
            nextx = np.cos(nextangle*np.pi/180)*br
            nexty = np.sin(nextangle*np.pi/180)*br
            goto(nextx, nexty)
    elif model == 2:
        for _ in range(3 * int(times)):
            nextangle += angle
            nextx = np.cos(nextangle * np.pi / 180) * (br + inter)
            nexty = np.sin(nextangle * np.pi / 180) * (br + inter)
            goto(nextx, nexty)
            nextangle += angle
            nextx = np.cos(nextangle * np.pi / 180) * br
            nexty = np.sin(nextangle * np.pi / 180) * br
            goto(nextx, nexty)


def sunflowe_line(n, x, y):
    up()
    y = 180-y
    goto(-x/2, -(x/2)/np.tan(y/2*(np.pi/180)))
    down()
    for _ in range(n):
        forward(x)
        # print(position())
        left(y)

hideturtle()
pensize(2)
# print(position()[0])
tracer(5, 10)
speed(11)
out_flower(140, 100, 20)
# move(-100)
goto(0, 0)
flower(4, 120.0, 120.0)

# move(100)
# flower(10, 40.0, 80.0)

# move(100)
# flower(20, 240.0, 20.0)
# move(100)
size = 90
# draw_pie(5, size)
draw_pie(6, size)
# draw_pie(7, size)
# draw_pie(8, size)
# print(np.sin(30*np.pi/180))
wheel(150, 20, 12, 2)
# wheel(200, 50, 12, 1)
# sunflowe_line(50, 150, 12)
dot_circle(15)

setheading(0)
goto(0, 0)
square(-170, 170)
right(45)
square(0, 240)
c(240, -170, -170)
left(45)
up()
goto(0, -200)
down()
# circle(200, 360, 3)
# c(170, 0, -170)
# c(155, 0, -155)
# c(100, 0, -100)
# c(85, 0, -85)
c(15, 0, -15)
c(255, 0, -255)
# hideturtle()
done()


