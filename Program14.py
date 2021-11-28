# Name: Numaan Qureshi
# Email: numaan.qureshi58@myhunter.cuny.edu
# Date: September 25 2021
# This program creates a colored square.

hColor = input("Please enter a 6-digit Hexadecimal number:")

myString = ""

a = [myString, hColor]
b = "#".join(a)

import turtle

wn = turtle.Screen()
wn.bgcolor("white")
tess = turtle.Turtle()
tess.shape("turtle")
tess.color(b)


for i in range(4):
    tess.left(90)
    tess.forward(100)
    tess.stamp()

# End
