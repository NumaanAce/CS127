# Name: Numaan Qureshi
# Email: numaan.qureshi58@myhunter.cuny.edu
# Date: October 15 2021
# This program analyzes data for a covid cases in an entered borough.

import matplotlib.pyplot as plt
import pandas as pd

a = input("Enter borough name:")
b = input("Enter output name:")

pop = pd.read_csv('covidCases.csv')

pop['Fraction'] = pop[a] / pop['Case Count']

pop.plot(x='Date of Interest', y='Fraction')

print("Min:", pop[a].min())
print("Max:", pop[a].max())
print("Mean:", pop[a].mean())
print("Median:", pop[a].median())
print("Standard Deviation:", pop[a].std())

fig = plt.gcf()
fig.savefig(b)

# END
