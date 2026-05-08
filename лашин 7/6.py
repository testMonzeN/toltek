from turtle import *

screensize(5000, 5000)
m = 25
tracer(0)

for _ in range(2):
    forward(12 * m)
    right(90)
    forward(18 * m)
    right(90)

up()

forward(4 * m)
right(90)
forward(5 * m)
left(90)

down()
for _ in range(2):
    forward(15 * m)
    right(90)
    forward(7 * m)
    right(90)

up()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x * m, y * m)
        dot(3, 'red')

done()