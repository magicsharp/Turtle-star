#This program would print out a turtle background and turtle itself given the user input with a turtle width of 5. 


import turtle
from turtle import *

t = turtle.Turtle()
s = turtle.Screen()


color_back = str(input("Enter a backgorund color: "))
color = str(input("Enter a turtle color: "))

s.bgcolor(color_back)
t.pencolor(color)
t.width(5)

for i in range(5):
    t.forward(300)
    t.right(144)
    
turtle.exitonclick()