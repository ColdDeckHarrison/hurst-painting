from turtle import Turtle, Screen
import random
import turtle
import colorgram
# rgb_colors = []

tim = Turtle()
tim.shape("turtle")
tim.color("blue")
tim.speed("fastest")
turtle.colormode(255)

# colors = colorgram.extract('image.jpg', 16)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

color_list = [(167, 11, 68), (251, 231, 63), (169, 87, 24), (55, 40, 33), (33, 43, 70),
              (106, 182, 237),
              (232, 129, 182), (8, 62, 144), (57, 132, 62), (108, 222, 203), (210, 54, 70), (63, 50, 68)]

random.choice(color_list)
tim.hideturtle()
tim.penup()
tim.setposition(-250, -250)
for _ in range(10):
    tim.dot(20, random.choice(color_list))
    tim.penup()
    tim.forward(50)

tim.setposition(-250, -200)
for _ in range(10):
    tim.dot(20, random.choice(color_list))
    tim.penup()
    tim.forward(50)

tim.setposition(-250, -150)
for _ in range(10):
    tim.dot(20, random.choice(color_list))
    tim.penup()
    tim.forward(50)

tim.setposition(-250, -100)
for _ in range(10):
    tim.dot(20, random.choice(color_list))
    tim.penup()
    tim.forward(50)

tim.setposition(-250, -50)
for _ in range(10):
    tim.dot(20, random.choice(color_list))
    tim.penup()
    tim.forward(50)

tim.setposition(-250, 0)
for _ in range(10):
    tim.dot(20, random.choice(color_list))
    tim.penup()
    tim.forward(50)

tim.setposition(-250, 50)
for _ in range(10):
    tim.dot(20, random.choice(color_list))
    tim.penup()
    tim.forward(50)

tim.setposition(-250, 100)
for _ in range(10):
    tim.dot(20, random.choice(color_list))
    tim.penup()
    tim.forward(50)

tim.setposition(-250, 150)
for _ in range(10):
    tim.dot(20, random.choice(color_list))
    tim.penup()
    tim.forward(50)

tim.setposition(-250, 200)
for _ in range(10):
    tim.dot(20, random.choice(color_list))
    tim.penup()
    tim.forward(50)


screen = Screen()
screen.exitonclick()
