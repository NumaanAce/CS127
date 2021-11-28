#Name: Numaan Qureshi
#Email: numaan.qureshi58@myhunter.cuny.edu
#Date: September 24 2021
#This program creates the shades from yellow to red.

import turtle

turtle.colormode(255)
tess = turtle.Turtle()
tess.shape("turtle")

for i in range(0,255,10):
  tess.forward(10)		#Move forward
  tess.pensize(i)		#Set the drawing size to be i (larger each time)
  tess.color(255,255-i,0)

tess.penup()
tess.pensize(0)
tess.color(0,0,0)
tess.backward(260)
tess.right(90)
tess.pendown()

for i in range(0,255,10):
  tess.forward(10)		#Move forward
  tess.pensize(i)		#Set the drawing size to be i (larger each time)
  tess.color(255,255-i,0)
