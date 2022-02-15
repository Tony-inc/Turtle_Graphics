from turtle import Turtle, Screen
import turtle as t
import random

screen = Screen()
screen.screensize(1500, 1500)

tim = Turtle()

tim.shape("turtle")
tim.pensize(2)
tim.speed(0)
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def circle(angle):
    tim.color(random_color())
    tim.circle(200)
    tim.setheading(angle)


def square(angle):
    tim.color(random_color())
    for _ in range(4):
        tim.forward(400)
        tim.right(90)
    tim.setheading(angle)


for x in range(0, 360, 3):
    circle(x)
    square(x)

screen.exitonclick()