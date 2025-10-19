import turtle
import math

charle = turtle.Turtle()
charle.hideturtle()

def triangle(charle, length, angle):
    hight = length * math.sin(angle * math.pi / 180)
    charle.rt(angle)
    charle.fd(length)
    charle.lt(90 + angle)
    charle.fd(2 * hight)
    charle.lt(90 + angle)
    charle.fd(length)
    charle.lt(180 - angle)


def polypie(charle, length, number_of_segments):
    angle = 360 / number_of_segments
    for i in range(number_of_segments):
        triangle(charle, length, angle / 2)
        charle.left(angle)

def move(charle, length):
    charle.penup()
    charle.fd(length)
    charle.pendown()

charle.fillcolor("red")
charle.begin_fill()
polypie(charle, 50, 7)
charle.end_fill()
move(charle, 100)
charle.fillcolor("green")
charle.begin_fill()
polypie(charle, 50, 6)
move(charle, 100)
charle.end_fill()
charle.fillcolor("blue")
charle.begin_fill()
polypie(charle, 50, 5)
charle.end_fill()

turtle.mainloop()