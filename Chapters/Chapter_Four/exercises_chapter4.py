import turtle
bob = turtle.Turtle()

# Exercise 1 Chapter 4

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)
square(bob, 100)





turtle.mainloop()