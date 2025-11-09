import turtle
import exercises_chapter4_poligone

alice = turtle.Turtle()
alice.hideturtle()
alice.color("red")

def petal(alice, radius, angle):
    for i in range(2):
        exercises_chapter4_poligone.arc(alice, radius, angle)
        alice.left(180 - angle)

def flower(alice, radius, angle, n):
    for i in range(n):
        petal(alice, radius, angle)
        alice.left(360 / n)

def move(alice, length):
    alice.penup()
    alice.forward(length)
    alice.pendown()

flower(alice, 50, 60, 7)
move(alice, 150)
alice.color("blue")
flower(alice, 50, 80, 10)
move(alice, 150)
alice.color("green")
flower(alice, 100, 20, 20)




turtle.mainloop()