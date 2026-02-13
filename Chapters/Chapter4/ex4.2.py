import turtle
import math

bob = turtle.Turtle()


def circle(t: turtle.Turtle, radius: float):
    arc(t, radius, 360)


def arc(t: turtle.Turtle, radius: float, angle: float):
    arc_length = 2 * math.pi * radius * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = angle / n
    t.left(step_angle / 2)
    polyline(t, n, step_length, step_angle)
    t.right(step_angle / 2)


def polyline(t: turtle.Turtle, n: int, length: float, angle: float):
    """Рисует n отрезков с заданной длиной length и углами angle
    (в градусах) между ними черепашкой t.
    """
    for i in range(n):
        t.forward(length)
        t.left(angle)


circle(bob, 100)
