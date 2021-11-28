# Name: Numaan Qureshi
# Email: numaan.qureshi58@myhunter.cuny.edu
# Date: October 5 2021
# This program creates plaid stripes.

import matplotlib.pyplot as plt
import numpy as np

x = int(input("Please enter the size of your image: "))
output = input("Please enter the name of the output file: ")

plaidStripes = np.ones((x, x, 3))

# YELLOW
plaidStripes[1::2, :, 0] = 0.94
plaidStripes[1::2, :, 1] = 0.90
plaidStripes[1::2, :, 2] = 0.55

# BROWN
plaidStripes[:, 1::2, 0] = 0.73
plaidStripes[:, 1::2, 1] = 0.56
plaidStripes[:, 1::2, 2] = 0.56

plt.imsave(output, plaidStripes)
# plt.imshow(plaidStripes)
# plt.show()

# END
