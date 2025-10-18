import turtle
import math
bob = turtle.Turtle()

# Exercises Chapter 4

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def polygone(t, length,n):
    angle = 360/n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    polygone(t, circumference/n, n)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle/360
    n =  arc_length / 4 + 1
    step_length = arc_length / n
    arc_angle = angle / n
    for i in range(int(n)):
        t.fd(step_length)
        t.lt(arc_angle)

turtle.mainloop()