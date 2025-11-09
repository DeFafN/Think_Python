import turtle
import math

t = turtle.Turtle()
t.hideturtle()

start_radius = 3  # Константа
radius_grouth_speed = 0.1
angle = 0
total_angle_degrees = 1800
step_degrees = 5

for angle in range(0, total_angle_degrees, step_degrees):
    theta = math.radians(angle)
    r = start_radius * math.exp(radius_grouth_speed * theta)
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    t.goto(x, y)

turtle.mainloop()