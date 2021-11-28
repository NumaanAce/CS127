# Name: Numaan Qureshi
# Email: numaan.qureshi58@myhunter.cuny.edu
# Date: October 23 2021
# This program lists UFO Sightings by state.

import matplotlib.pyplot as plt
import pandas as pd

a = input("Enter the input file name:")
b = input("Enter the output file name:")

UFO = pd.read_csv(a)

groupStates = UFO.groupby("state")
sec = groupStates["duration (seconds)"].mean()
topTen = sec.sort_values(ascending=False)[:10]

topTen.plot.bar()
plt.xlabel("State")
plt.ylabel("Seconds")

# plt.show()

fig = plt.gcf()
fig.savefig(b)

# END
