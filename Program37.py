# Name: Numaan Qureshi
# Email: numaan.qureshi58@myhunter.cuny.edu
# Date: October 28 2021
# This program writes down video game sales.

import pandas as pd
import matplotlib.pyplot as plt


def main():
    a = input("Enter file name:")
    df = pd.read_csv(a)
    b = df["Name"].count()
    c = df["Genre"].value_counts()
    d = df["Publisher"].value_counts()[:3]

    print("There are", b, "total games.")
    print("The number of games in each genre is:")
    print(c)
    print("The top 3 game publishers are:")
    print(d)


if __name__ == "__main__":
    main()

# END
