import turtle
t = turtle.Turtle()

def koch(t, length):
    if length < 5:
        t.forward(length)
    else:
        koch(t, length / 3)
        t.left(60)
        koch(t, length / 3)
        t.right(120)
        koch(t, length / 3)
        t.left(60)
        koch(t, length / 3)

def snowflake(t, length):
    koch(t, 100)
    t.right(120)
    koch(t, 100)
    t.right(120)
    koch(t, 100)

snowflake(t, 1000)
turtle.mainloop()