# Name: Numaan Qureshi
# Email: numaan.qureshi58@myhunter.cuny.edu
# Date: October 25, 2021
# This program graphs a percentage over time of the Superbowl Statistics.

import matplotlib.pyplot as plt
import pandas as pd

a = input("Enter name of input file:")
b = input("Enter name of output file:")

df = pd.read_csv(a)

df["Date"] = pd.to_datetime(df["Date"].apply(str))

df["% Points"] = (df["Winner Pts"] / (df["Winner Pts"] + df["Loser Pts"])) * 100

df.plot(x="Date", y="% Points")

fig = plt.gcf()
fig.savefig(b)

# END
