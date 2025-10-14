import turtle
bob = turtle.Turtle()

# Exercises Chapter 4

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polygone(t, length,n):
    angle = 360/n
    for i in range(n):
        t.fd(length)
        t.lt(angle)
polygone(bob, 100, 7)



turtle.mainloop()