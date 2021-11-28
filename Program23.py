# Name: Numaan Qureshi
# Email: numaan.qureshi58@myhunter.cuny.edu
# Date: October 10 2021
# This program compares snow count within two images.

import matplotlib.pyplot as plt

firstImage = input("Enter first image file name: ")
secondImage = input("Enter second image file name: ")
t = float(input("Enter threshold of white pixels: "))


a = plt.imread(firstImage)  # Read in image
b = plt.imread(secondImage)

asnowCount = 0  # Number of pixels that are almost white
bsnowCount = 0

for i in range(a.shape[0]):
    for j in range(a.shape[1]):
        # Check if red, green, and blue are > t:
        if (a[i, j, 0] > t) and (a[i, j, 1] > t) and (a[i, j, 2] > t):
            asnowCount = asnowCount + 1

for n in range(b.shape[0]):
    for m in range(b.shape[1]):
        # Check if red, green, and blue are > t:
        if (b[n, m, 0] > t) and (b[n, m, 1] > t) and (b[n, m, 2] > t):
            bsnowCount = bsnowCount + 1

x = asnowCount - bsnowCount

print("Snow count of first image: ", asnowCount)
print("Snow count of second image: ", bsnowCount)
print("Difference between first and second image: ", x)

# END
