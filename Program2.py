#Name: Numaan Qureshi
#Email: numaan.qureshi58@myhunter.cuny.edu
#Date: September 3, 2021
#This program draws a nonagon.

import turtle
wn = turtle.Screen()

nonagonA = turtle.Turtle()
for i in range(9):
  nonagonA.forward(100)  #Move thomasH forward 100 steps
  nonagonA.left(40)      #Turn thomasH 60 degrees to the left

wn.exitonclick()
