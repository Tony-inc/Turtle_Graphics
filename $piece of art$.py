from turtle import Turtle, Screen
import turtle as t
import random


screen = Screen()
screen.screensize(1000, 1000)

tim = Turtle()

tim.shape("turtle")

tim.speed(0)
t.colormode(255)

# import colorgram
# colors = colorgram.extract("image.jpeg", 20)
#
# color_bank = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     color_bank.append(new_color)
#
# print(color_bank)

color_bank = [(250, 249, 245), (209, 165, 124), (139, 49, 106), (164, 168, 38), (244, 79, 57), (248, 225, 229), (4, 143, 57), (216, 231, 233), (234, 111, 163), (67, 197, 218), (241, 65, 139), (2, 142, 184), (161, 55, 52), (217, 230, 225), (249, 226, 25), (21, 165, 127), (253, 230, 0), (154, 176, 163), (30, 194, 218), (226, 170, 191)]

tim.penup()
tim.hideturtle()

start_position = tim.setpos(-200, -100)
y = -100

for _ in range(10):
    for _ in range(10):
        tim.dot(20, random.choice(color_bank))
        tim.forward(50)
    y += 50
    tim.setpos(-200, y)

screen.exitonclick()