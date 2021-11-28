#Name: Numaan Qureshi
#Email: numaan.qureshi58@myhunter.cuny.edu
#Date: September 4, 2021
#This program draws a house.

import turtle
wn = turtle.Screen()             # Set up the window and its attributes
wn.bgcolor("khaki")


tess = turtle.Turtle()           # create tess and set some attributes
tess.color("darkblue")
tess.pensize(5)

alex = turtle.Turtle()           # create alex
alex.color("violet")
alex.pensize(5)

tess.forward(100)                 # Let tess draw an equilateral triangle
tess.left(90)
tess.forward(100)
tess.left(90)
tess.forward(100)
tess.left(90)
tess.forward (100)
tess.left(90)

alex.left(90)
alex.forward(100)# move her away from the origin
alex.right(30)
alex.forward(100)
alex.right(120)
alex.forward(100)
alex.right(120)
alex.forward(100)

wn.exitonclick()
