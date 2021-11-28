#Name: Numaan Qureshi
#Email: numaan.qureshi58@myhunter.cuny.edu
#Date: September 23 2021
#This program creates a yellow pseudo-heart.

import turtle

turtle.colormode(255)
tess = turtle.Turtle()
tess.shape("turtle")

tess.left(60)

for i in range(0,255,10):
  tess.forward(10)		#Move forward
  tess.pensize(i)		#Set the drawing size to be i (larger each time)
  tess.color(i,i,0)		#Set the red channel to be i (brighter each time)

tess.penup()
tess.color(0,0,0)
tess.pensize(0)
tess.backward(260)
tess.pendown()

tess.left(60)

for i in range(0,255,10):
  tess.forward(10)		#Move forward
  tess.pensize(i)		#Set the drawing size to be i (larger each time)
  tess.color(i,i,0)		#Set the red channel to be i (brighter each time)
