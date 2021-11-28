# Name: Numaan Qureshi
# Email: numaan.qureshi58@myhunter.cuny.edu
# Date: October 7 2021
# This program uses turtle to create a square eye.

import turtle
turtle.colormode(255)
turtle.bgcolor("khaki")

ben = turtle.Turtle()
ben.speed(0)
ben.pensize(5)

for i in range(36):
    ben.pencolor(0, i*7, 0)
    ben.forward(10)
    ben.left(10)
    for n in range(4):
        ben.left(90)
        ben.forward(300)
        ben.backward(50)

# END

# LIBRARIES: turtle
# VARIABLES: i, n
# FUNCTIONS: for, range

# Desc: The program uses RGB values and a turtle to create a square eye with increasing green colors as you go
# counter-clockwise. We use a for loop that loops 36 times, and contains an inner for loop that loops 4 times. The
# outer loop creates the middle, or the "retina" of the eye and the inner loop creates the squares that protrude and
# create the outline of the eye.
