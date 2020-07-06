from turtle import*
import numpy as np

br = 140
r = 80
angle = 60
times = int(360 / angle)
angle = 360 / times
inner_range = br * np.cos(angle / 2 * np.pi / 180) - np.sqrt(r * r - (br * br * np.sin(angle / 2 * np.pi / 180) * np.sin(angle / 2 * np.pi / 180)))
heading_angle = np.arccos((br * br + r * r - inner_range * inner_range) / (2 * br * r))
# up()
goto(0, -br)
circle(br)
nextangle = -90
down()
for _ in range(3 * int(times)):
    setheading(nextangle + 90 - heading_angle)
    circle(r, 2 * (angle + inner_range))
    nextangle += angle
done()