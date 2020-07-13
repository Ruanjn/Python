import turtle
import random
import time
l = random.randint(1, 19)
x = turtle.Turtle()

wn = turtle.Screen()
wn.bgcolor("white")

turtle.tracer(20)
x.speed(0)
x.penup()
x.color('red')


def mandala(y, c):
  j = 0
  for i in range(380):
        x.goto(0,0)
        x.setheading(1*i)
        x.forward(c)
        x.left(j)
        x.pendown()
        x.dot(2)
        x.forward(y)
        x.penup()
        x.dot(1)
        j=j+(l)
  return


while True:
  x.color('blue')

  mandala(60, 80)
  l = random.randint(1, 49)
  x.color('yellow')
  mandala(10, 50)
  l = random.randint(1, 9)
  x.color('green')
  mandala(40, 150)
  time.sleep(3)
  x.clear()
  l = random.randint(1, 49)