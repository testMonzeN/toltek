from turtle import *

screensize(5000, 5000)
m = 25
tracer(0)

for _ in range(11):
    forward(23 * m)
    left(270)
    forward(19 * m)
    right(90)

up()
forward(3 * m)
right(90)
forward(9 * m)
left(90)

down()
for _ in range(12):
    forward(14 * m)
    right(90)
    forward(22 * m)
    right(90)

up()


for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x * m, y * m)
        dot(3, 'red')

done()