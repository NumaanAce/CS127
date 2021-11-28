# Name: Numaan Qureshi
# Email: numaan.qureshi58@myhunter.cuny.edu
# Date: September 30 2021
# This program creates a P-shaped logo.

import matplotlib.pyplot as plt
import numpy as np

logoImg = np.ones((30, 30, 3))

# logoImg[:, :5, 1] = 0
# logoImg[:5, :, 1] = 0
# logoImg[15:20, :, 1] = 0
# logoImg[:20, 25:30, 1] = 0
# logoImg[5:15, 5:25, :3] = 0
# logoImg[20:30, 5:, :3] = 0

logoImg[:, :6, 1] = 0
logoImg[:6, :, 1] = 0
logoImg[15:21, :, 1] = 0
logoImg[:20, 24:, 1] = 0
logoImg[6:15, 6:25, :3] = 0
logoImg[21:30, 6:, :3] = 0

plt.imsave("logo.png", logoImg)
plt.imshow(logoImg)
plt.show()

# END
