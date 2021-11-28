# Name: Numaan Qureshi
# Email: numaan.qureshi58@myhunter.cuny.edu
# Date: October 23, 2021
# This program creates a shelter census.

import matplotlib.pyplot as plt
import pandas as pd

a = input("Enter the input file name:")
b = input("Enter the output file name:")

homeless = pd.read_csv(a)
homeless["Fraction Single Adults"] = homeless["Total Single Adults in Shelter"] / homeless["Total Individuals in Shelter"]

homeless.plot(x="Date of Census", y="Fraction Single Adults")

fig = plt.gcf()
fig.savefig(b)

# END