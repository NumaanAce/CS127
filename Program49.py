# Name: Numaan Qureshi
# Email: numaan.qureshi58@myhunter.cuny.edu
# Date: 23 November 2021

import matplotlib.pyplot as plt
import numpy as np


def main():
    print("------------------------------------------\n"
          "        Welcome to the Color Maker!       \n"
          "------------------------------------------\n"
          "Please enter for each rbg color the value in which to increase/decrease them.\n"
          "If all 3 values given are 0, the program will end and save the resulting image.")    # Intro to Program
    output = input("Please enter the outfile name: ")   # Input to set image file name

    red = float(input("How much do you want to change the red value by? "))         # Input to set red color
    green = float(input("How much do you want to change the green value by? "))     # Input to set green color
    blue = float(input("How much do you want to change the blue value by? "))       # Input to set blue color

    img = np.zeros((10, 10, 3))     # Creating empty plot of zeros, aka a completely black plot.
    red_val = 0                     # Creating a variable to manipulate red input in the upcoming code.
    green_val = 0                   # Creating a variable to manipulate green input in the upcoming code.
    blue_val = 0                    # Creating a variable to manipulate blue input in the upcoming code.

    while (0 != red <= 255) or (0 != green <= 255) or (0 != blue <= 255):   # While loop for when colors < 255 and != 0
        if (red_val + red) > 255:
            red_val = 255
        elif (red_val + red) < 0:
            red_val = 0
        else:
            red_val += red

        if (green_val + green) > 255:
            green_val = 255
        elif (green_val + green) < 0:
            green_val = 0
        else:
            green_val += green

        if (blue_val + blue) > 255:
            blue_val = 255
        elif (blue_val + blue) < 0:
            blue_val = 0
        else:
            blue_val += blue

        curRGB = [float(red_val / 255), float(green_val / 255), float(blue_val / 255)]
        print("The current rgb values are:", curRGB, "\n"
                                                     "")
        red = float(input("How much do you want to change the red value by? "))
        green = float(input("How much do you want to change the green value by? "))
        blue = float(input("How much do you want to change the blue value by? "))

    img[:, :, 0] = float(red_val / 255)
    img[:, :, 1] = float(green_val / 255)
    img[:, :, 2] = float(blue_val / 255)
    print("You're done! Congrats on the color, it looks beautiful!")

    # plt.imsave(output, img)
    plt.imshow(img)
    plt.show()


if __name__ == "__main__":
    main()
