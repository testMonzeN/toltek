from turtle import *

screensize(5000, 5000)
m = 9
tracer(0)

for _ in range(2):
    forward(19 * m)
    left(270)
    forward(10 * m)
    right(90)

up()

forward(9 * m)
right(90)
forward(7 * m)
left(90)

down()
for _ in range(2):
    forward(100 * m)
    right(90)
    forward(101 * m)
    right(90)

up()
for x in range(-200, 200):
    for y in range(-200, 200):
        goto(x * m, y * m)
        dot(3, 'red')

done()