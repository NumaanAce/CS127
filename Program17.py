# Name: Numaan Qureshi
# Email: numaan.qureshi58@myhunter.cuny.edu
# Date: September 29 2021
# This program creates a colorful turtle spiral.

import turtle
wn = turtle.Screen()

stamps = input("Enter number of stamps the turtle will print: ")
a = int(stamps)

steps = 10
red = 186
green = 164
blue = 145

turtle.colormode(255)
robert = turtle.Turtle()
robert.shape("circle")
robert.speed(0)
robert.pensize(0)
robert.penup()
robert.color(red, green, blue)

for t in range(0,a):
    robert.stamp()
    steps += 2
    if (red or green or blue) + 3 <= 255:
        red += 3
        green += 3
        blue += 3
    robert.color(red, green, blue)
    robert.forward(steps)
    robert.right(24)

# END
