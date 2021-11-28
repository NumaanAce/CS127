# Name: Numaan Qureshi
# Email: numaan.qureshi58@myhunter.cuny.edu
# Date: September 4, 2021
# This program draws a pinwheel.

import turtle

wn = turtle.Screen()
wn.bgcolor("white")

diego = turtle.Turtle()
diego.shape("arrow")
diego.color("purple")
diego.pensize(3)

diego.forward(30)

for i in range(3):
    diego.forward(50)
    diego.right(120)

diego.backward(30)
diego.right(90)
diego.forward(30)

for i in range(3):
    diego.forward(50)
    diego.right(120)

diego.backward(30)
diego.right(90)
diego.forward(30)

for i in range(3):
    diego.forward(50)
    diego.right(120)

diego.backward(30)
diego.right(90)
diego.forward(30)

for i in range(3):
    diego.forward(50)
    diego.right(120)

diego.backward(30)
wn.exitonclick()
