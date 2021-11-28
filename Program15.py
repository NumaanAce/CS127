# Name: Numaan Qureshi
# Email: numaan.qureshi58@myhunter.cuny.edu
# Date: September 26 2021
# This program omits blue from a submitted image.

import matplotlib.pyplot as plt
import numpy as np

inImage = input("Enter name of the input file:")
outImage = input("Enter name of the output file:")

img = plt.imread(inImage)
plt.imshow(img)
plt.show()

img2 = img.copy()
img2[:, :, 2] = 0

plt.imshow(img2)
plt.show()

plt.imsave(outImage, img2)

# END