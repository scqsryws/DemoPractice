# 蟒蛇实例
# import turtle
#
#
# def drawSnake(rad, angle, len, neckrad):
#     for i in range(len):
#         turtle.circle(rad, angle)
#         turtle.circle(-rad, angle)
#     turtle.circle(rad, angle / 2)
#     turtle.fd(rad)
#     turtle.circle(neckrad + 1, 180)
#     turtle.fd(rad * 2 / 3)
#
#
# def main():
#     turtle.setup(1300, 800, 0, 0)
#     pythonsize = 30
#     turtle.pensize(pythonsize)
#     turtle.pencolor("blue")
#     turtle.seth(-40)
#     drawSnake(40, 80, 5, pythonsize / 2)
#
#
# main()
'''
import turtle

turtle.setup(1300, 500, 200, 200)
turtle.penup()
turtle.forward(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("blue")
turtle.seth(-45)
for i in range(4):
    turtle.circle(40, 90)
    turtle.circle(-40, 90)
turtle.circle(40, 90/2)
turtle.forward(40)
turtle.circle(16, 180)
turtle.forward(40 * 2 / 3)
turtle.done()
'''

import turtle

turtle.setup(1300, 700)
turtle.hideturtle()
turtle.pencolor('red')
turtle.fillcolor('yellow')
turtle.speed(10)
turtle.penup()
turtle.goto(-100, 0)
turtle.pendown()
turtle.begin_fill()
turtle.fd(200)
while abs(pos(x,y)) < 1:
    turtle.left(170)
    turtle.forward(200)

turtle.end_fill()
turtle.done()





















