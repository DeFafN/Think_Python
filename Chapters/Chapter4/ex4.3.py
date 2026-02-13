import turtle
import math

bob = turtle.Turtle()


def triangle(t: turtle.Turtle, length: float, angle: float):
    """
    Рисует равнобедренный треугольник с заданной боковой стороной и углом при вершине.

    Черепашка начинает в нижней левой вершине, рисует боковую сторону, затем основание,
    потом вторую боковую сторону и возвращается в начальную точку.

    Параметры:
        t (turtle.Turtle): объект черепашки для рисования
        length (float): длина боковой стороны треугольника
        angle (float): угол при вершине треугольника в градусах
    """
    hight = length * math.sin(angle * math.pi / 180)
    t.rt(angle)
    t.fd(length)
    t.lt(90 + angle)
    t.fd(2 * hight)
    t.lt(90 + angle)
    t.fd(length)
    t.lt(180 - angle)


def polypie(t: turtle.Turtle, length: float, number_of_segments: int):
    """
    Рисует правильный многоугольник, разделённый на одинаковые треугольные секторы (пирог).

    Функция рисует указанное количество секторов, каждый из которых является
    равнобедренным треугольником с заданной боковой стороной (радиусом).

    Параметры:
        t (turtle.Turtle): объект черепашки для рисования
        length (float): длина боковой стороны треугольника (радиус описанной окружности)
        number_of_segments (int): количество секторов (например, 5 — пятиугольник)
    """
    angle = 360 / number_of_segments
    for i in range(number_of_segments):
        triangle(t, length, angle / 2)
        t.left(angle)


def move(t: turtle.Turtle, length: float):
    """
    Перемещает черепашку вперёд на заданное расстояние без рисования.

    Используется для позиционирования черепашки перед началом следующего рисунка.

    Параметры:
        t (turtle.Turtle): объект черепашки для перемещения
        length (float): расстояние, на которое нужно переместиться
    """
    t.penup()
    t.fd(length)
    t.pendown()

polypie(bob, 50, 5)
move(bob, 100)
polypie(bob, 50, 6)
move(bob, 100)
polypie(bob, 50, 7)

turtle.mainloop()
