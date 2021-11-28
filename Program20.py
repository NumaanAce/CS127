# Name: Numaan Qureshi
# Email: numaan.qureshi58@myhunter.cuny.edu
# Date: September 30 2021
# This program creates influencer tiers.

import numpy as np
import matplotlib.pyplot as plt

elevations = np.loadtxt('elevationsNYC.txt')

mapShape = elevations.shape + (3,)

floodMap = np.zeros(mapShape)

for row in range(mapShape[0]):
    for col in range(mapShape[1]):
        if 5 < elevations[row, col] <= 20:
            floodMap[row, col, :3] = 0.5        # Gray Area (All colors = 50%)
        elif 0 < elevations[row, col] <= 6:     # Below Storm Surge Area
           floodMap[row, col, 0] = 1.0          # Red Channel = 100%
        elif elevations[row,col] <= 0:
            floodMap[row, col, 0] = 1.0
            floodMap[row, col, 1] = 1.0
            floodMap[row, col, 2] = 0
        else:
                                                # Above the 6 foot storm surge and didn't flood
            floodMap[row, col, 1] = 1.0         # Green Channel = 100%

# plt.imshow(floodMap)
# plt.show()
plt.imsave('floodMap.png', floodMap)