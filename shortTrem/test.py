from turtle import*
import numpy as np

br = 140
r = 70
times = 6
angle = 360 / times
if r < br*np.sin(angle/2*np.pi/180):
    print("error")
    exit()
inner_range = br * np.cos(angle / 2 * np.pi / 180) - np.sqrt(r * r - (br * br * np.sin(angle / 2 * np.pi / 180) * np.sin(angle / 2 * np.pi / 180)))
heading_angle = np.arccos((br * br + r * r - inner_range * inner_range) / (2 * br * r))
heading_angle *= 180/np.pi
up()
goto(0, -br)
# circle(br)
nextangle = -90
down()
for _ in range(times):
    setheading(nextangle + 90 - heading_angle)
    circle(r, angle + 2*heading_angle)
    nextangle += angle
done()