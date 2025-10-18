
import math

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
    polyline(t, n, length, angle)

def circle(t, r):
    arc(t, r, 360)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle/360
    n =  int(arc_length / 3 + 1)
    step_length = arc_length / n
    arc_angle = angle / n
    polyline(t, n, step_length, arc_angle)



# main -> bob, circle (t = bob, radius = input)
# circle -> arc (bob, radius, angle=360)
# arc -> (bob, radius, 360) arc_length, n, step_length, arc_angle -> polyline
# polyline -> (bob, n, step_length, arc_angle)