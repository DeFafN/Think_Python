import turtle
import math

joe = turtle.Turtle()
#joe.hideturtle()

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle/360
    n =  int(arc_length / 3 + 1)
    step_length = arc_length / n
    arc_angle = angle / n
    polyline(t, n, step_length, arc_angle)

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.rt(angle)

letter_spacing = 60
def move_to_next_letter(turtle, letter_spacing, line_length):
    turtle.penup()
    turtle.forward(letter_spacing)
    turtle.left(90)
    turtle.forward(line_length)
    turtle.pendown()


def draw_a(turtle, line_length):
    turtle.left(75)
    turtle.forward(line_length)
    turtle.right(150)
    turtle.forward(line_length)
    turtle.backward(line_length // 2)
    turtle.right(105)
    turtle.forward(line_length // 4)
    turtle.penup()
    turtle.backward(line_length // 4)
    turtle.left(105)
    turtle.forward(line_length // 2)
    turtle.pendown()

def draw_b(turtle, line_length):
    turtle.left(90)
    turtle.forward(line_length)
    turtle.right(90)
    turtle.forward(line_length // 4)
    turtle.backward(line_length // 4)
    turtle.right(90)
    turtle.forward(line_length // 2)
    turtle.left(90)
    arc(turtle, line_length // 4, 180)


def draw_v(turtle, line_length):
    turtle.left(90)
    turtle.forward(line_length)
    turtle.right(90)
    arc(turtle, line_length // 4, 180)
    turtle.lt(180)
    arc(turtle, line_length // 4, 180)

def draw_g(turtle, line_length):
    turtle.left(90)
    turtle.forward(line_length)
    turtle.right(90)
    turtle.forward(line_length // 3)

def draw_d(turtle, line_length):
    polyline(turtle, 4, line_length // 2, 90)
    turtle.penup()
    turtle.rt(90)
    turtle.fd(line_length // 2)
    turtle.rt(90)
    turtle.pendown()
    turtle.fd(line_length // 5)
    turtle.lt(90)
    turtle.fd(line_length // 5)
    turtle.lt(90)
    turtle.penup()
    turtle.fd(line_length // 2 + ((line_length // 5) * 2))
    turtle.lt(90)
    turtle.pendown()
    turtle.fd(line_length // 5)
    turtle.lt(90)
    turtle.fd(line_length // 5)

def draw_e(turtle, line_length):
    turtle.forward(line_length // 3)
    turtle.backward(line_length // 3)
    turtle.left(90)
    turtle.forward(line_length // 2)
    turtle.right(90)
    turtle.forward(line_length // 3)
    turtle.backward(line_length // 3)
    turtle.left(90)
    turtle.forward(line_length // 2)
    turtle.right(90)
    turtle.forward(line_length // 3)

def draw_zh(turtle, line_length):
    turtle.penup()
    turtle.goto(-line_length//2, line_length//2)
    turtle.pendown()
    turtle.goto(line_length//2, -line_length//2)
    turtle.penup()
    turtle.goto(0, line_length//2)
    turtle.pendown()
    turtle.goto(0, -line_length//2)
    turtle.penup()
    turtle.goto(line_length//2, line_length//2)
    turtle.pendown()
    turtle.goto(-line_length//2, -line_length//2)

def draw_z(turtle, line_length):
    turtle.penup()
    turtle.left(90)
    turtle.forward(line_length)
    turtle.pendown()
    turtle.rt(90)
    arc(turtle, line_length // 4, 180)
    turtle.lt(180)
    arc(turtle, line_length // 4, 180)

def draw_i(turtle, line_length):
    turtle.left(90)
    turtle.forward(line_length)
    turtle.right(140)
    turtle.forward(line_length * 1.28)
    turtle.left(140)
    turtle.forward(line_length)

def draw_k(turtle, line_length):
    turtle.left(90)
    turtle.forward(line_length)
    turtle.backward(line_length // 2)
    turtle.right(150)
    turtle.forward(line_length * 0.6)
    turtle.backward(line_length * 0.6)
    turtle.left(120)
    turtle.forward(line_length * 0.6)

def draw_l(turtle, line_length):
    turtle.forward(line_length)
    turtle.backward(line_length)
    turtle.right(90)
    turtle.forward(line_length // 2)
    turtle.left(90)
    turtle.penup()
    turtle.forward(line_length)
    turtle.pendown()

def draw_m(turtle, line_length):
    turtle.forward(line_length)
    turtle.right(135)
    turtle.forward(line_length // 2)
    turtle.left(90)
    turtle.forward(line_length // 2)
    turtle.right(135)
    turtle.forward(line_length)
    turtle.penup()
    turtle.backward(line_length)
    turtle.pendown()

def draw_n(turtle, line_length):
    turtle.forward(line_length)
    turtle.right(150)
    turtle.forward(line_length * 1.1547)
    turtle.left(150)
    turtle.forward(line_length)
    turtle.penup()
    turtle.backward(line_length)
    turtle.pendown()

def draw_o(turtle, line_length):
    for i in range(18):
        turtle.forward(2)
        turtle.right(10)
    turtle.penup()
    turtle.right(90)
    turtle.forward(line_length)
    turtle.left(90)
    turtle.forward(line_length // 2)
    turtle.pendown()

def draw_p(turtle, line_length):
    turtle.left(90)
    turtle.forward(line_length)
    turtle.right(90)
    for i in range(18):
        turtle.forward(2)
        turtle.right(10)
    turtle.right(90)
    turtle.forward(line_length // 2)
    turtle.right(90)
    turtle.forward(line_length // 2)
    turtle.penup()
    turtle.backward(line_length // 2)
    turtle.left(90)
    turtle.forward(line_length // 2)
    turtle.left(90)
    turtle.forward(line_length)
    turtle.pendown()

def draw_r(turtle, line_length):
    turtle.left(90)
    turtle.forward(line_length)
    turtle.right(90)
    for _ in range(18):
        turtle.forward(2)
        turtle.right(10)
    turtle.right(90)
    turtle.forward(line_length // 2)
    turtle.right(45)
    turtle.forward(line_length // 2)
    turtle.penup()
    turtle.backward(line_length // 2)
    turtle.left(45)
    turtle.forward(line_length // 2)
    turtle.left(90)
    turtle.forward(line_length)
    turtle.pendown()

def draw_s(turtle, line_length):
    turtle.forward(line_length)
    turtle.left(135)
    turtle.forward(line_length // 1.414)
    turtle.left(45)
    turtle.forward(line_length // 2)
    turtle.left(45)
    turtle.forward(line_length // 1.414)
    turtle.penup()
    turtle.right(135)
    turtle.forward(line_length // 2)
    turtle.pendown()

def draw_t(turtle, line_length):
    turtle.forward(line_length)
    turtle.backward(line_length // 2)
    turtle.right(90)
    turtle.forward(line_length // 2)
    turtle.left(90)
    turtle.forward(line_length // 2)
    turtle.backward(line_length)
    turtle.penup()
    turtle.forward(line_length)
    turtle.pendown()

def draw_u(turtle, line_length):
    turtle.forward(line_length)
    turtle.backward(line_length)
    turtle.right(90)
    turtle.forward(line_length)
    turtle.left(90)
    turtle.forward(line_length)
    turtle.penup()
    turtle.backward(line_length)
    turtle.pendown()

def draw_f(turtle, line_length):
    turtle.forward(line_length)
    turtle.right(90)
    turtle.forward(line_length // 2)
    turtle.right(90)
    turtle.forward(line_length)
    turtle.backward(line_length)
    turtle.left(90)
    turtle.forward(line_length // 2)
    turtle.right(90)
    turtle.penup()
    turtle.forward(line_length)
    turtle.pendown()

def draw_h(turtle, line_length):
    turtle.forward(line_length)
    turtle.backward(line_length)
    turtle.right(90)
    turtle.forward(line_length // 2)
    turtle.left(90)
    turtle.forward(line_length)
    turtle.right(90)
    turtle.forward(line_length // 2)
    turtle.right(90)
    turtle.forward(line_length)
    turtle.penup()
    turtle.backward(line_length)
    turtle.pendown()

def draw_c(turtle, line_length):
    turtle.penup()
    turtle.forward(line_length)
    turtle.right(90)
    turtle.forward(line_length // 2)
    turtle.right(90)
    turtle.pendown()
    for _ in range(18):
        turtle.forward(2)
        turtle.right(10)
    turtle.penup()
    turtle.left(90)
    turtle.forward(line_length // 2)
    turtle.left(90)
    turtle.forward(line_length)
    turtle.pendown()

def draw_x(turtle, line_length):
    turtle.left(45)
    turtle.forward(line_length * 1.414)
    turtle.backward(line_length * 0.707)
    turtle.right(90)
    turtle.forward(line_length * 0.707)
    turtle.penup()
    turtle.backward(line_length * 0.707)
    turtle.left(90)
    turtle.forward(line_length * 0.707)
    turtle.pendown()

def draw_yy(turtle, line_length):
    turtle.left(90)
    turtle.forward(line_length // 2)
    turtle.right(45)
    turtle.forward(line_length // 1.414)
    turtle.backward(line_length // 1.414)
    turtle.right(90)
    turtle.forward(line_length // 1.414)
    turtle.backward(line_length // 1.414)
    turtle.left(45)
    turtle.forward(line_length // 2)
    turtle.penup()
    turtle.backward(line_length)
    turtle.right(90)
    turtle.forward(line_length)
    turtle.pendown()

def draw_ya(turtle, line_length):
    turtle.left(90)
    turtle.forward(line_length)
    turtle.right(135)
    turtle.forward(line_length // 1.414)
    turtle.right(90)
    turtle.forward(line_length // 1.414)
    turtle.backward(line_length // 1.414)
    turtle.right(180)
    turtle.forward(line_length // 1.414)
    turtle.penup()
    turtle.backward(line_length // 1.414)
    turtle.left(135)
    turtle.forward(line_length)
    turtle.pendown()

draw_k(joe, 100)
#move_to_next_letter(joe, letter_spacing, 100)
#draw_C(joe, 100)
#move_to_next_letter(letter_spacing)
#draw_T(joe, 100)
#move_to_next_letter(letter_spacing)
#draw_R(joe, 100)
#move_to_next_letter(letter_spacing)
#draw_A(joe, 100)
turtle.mainloop()
