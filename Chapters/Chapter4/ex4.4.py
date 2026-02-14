import turtle
import math

bob = turtle.Turtle()
bob.hideturtle()


def polyline(t: turtle.Turtle, n: int, length: float, angle: float):
    """
    Рисует n прямых отрезков заданной длины с поворотом между ними на указанный угол.


    Параметры:
        t (turtle.Turtle): объект черепашки для рисования
        n (int): количество отрезков
        length (float): длина каждого отрезка
        angle (float): угол поворота между отрезками (в градусах)
    """
    for i in range(n):
        t.forward(length)
        t.left(angle)


def arc(t: turtle.Turtle, radius: float, angle: float):
    """
    Рисует дугу заданного радиуса и угловой протяжённости.

    Параметры:
        t (turtle.Turtle): объект черепашки для рисования
        radius (float): радиус дуги
        angle (float): центральный угол дуги (в градусах)
    """
    arc_length = 2 * math.pi * radius * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = angle / n
    t.left(step_angle / 2)
    polyline(t, n, step_length, step_angle)
    t.right(step_angle / 2)


def petal(t: turtle.Turtle, radius: float, angle: float):
    """
    Рисует один лепесток цветка, состоящий из двух симметричных дуг.

    Параметры:
        t (turtle.Turtle): объект черепашки для рисования
        radius (float): радиус дуг лепестка
        angle (float): угол каждой дуги (определяет "остроту" лепестка)
    """
    for i in range(2):
        arc(t, radius, angle)
        t.left(180 - angle)


def flower(alice: turtle.Turtle, radius: float, angle: float, n: int):
    """
    Рисует цветок из n лепестков, равномерно расположенных по кругу.

    Параметры:
        t (turtle.Turtle): объект черепашки для рисования
        radius (float): радиус дуг лепестков
        angle (float): угол каждой дуги лепестка
        n (int): количество лепестков
    """
    for i in range(n):
        petal(alice, radius, angle)
        alice.left(360 / n)


flower(bob, 50, 80, 10)

turtle.mainloop()
