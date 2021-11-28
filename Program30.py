# Name: Numaan Qureshi
# Email: numaan.qureshi58@myhunter.cuny.edu
# Date: October 18, 2021
# This program loads and lists ramen by their rating in Singapore.

import pandas as pd
import numpy as np

a = input("Enter the name of the input file: ")

df = pd.read_csv(a)
df["Stars"] = pd.to_numeric(df["Stars"], downcast="float")

groupStyle = df.groupby('Style')
groupCountry = df.groupby('Country')
groupBrand = df.groupby('Brand')

singapore = groupCountry.get_group("Singapore")
singaporeMin = singapore["Stars"].min()
singaporePlace = singapore.loc[singapore["Stars"] == singaporeMin, 'Brand'].iloc[0]

print(groupStyle['Stars'].mean())
print(singaporePlace, "has the lowest rating in Singapore with", singaporeMin, "stars.")

# END

# Name an input
# Print avg rating, per serving style. For all under a certain style, average them by the total number of that style.
# Print the name and rating of the lowest rated spot in Singapore.
