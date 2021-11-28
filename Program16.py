# Name: Numaan Qureshi
# Email: numaan.qureshi58@myhunter.cuny.edu
# Date: September 28 2021
# This program converts Parsecs to Light-Years and vice-versa.

conversion = input('Please enter the conversion you want to do:' 
                    ' "a" for Light-Year to Parsec conversion' 
                    ' "b" for Parsec to Light-Year conversion:')

x = conversion.lower()
print("Your selection:", x)

if x == "a":
    l = input("Please enter a number of Light Years:")
    print(float(l), "Light-Years is equal to", float(l) / 3.26156, "Parsecs.")
elif x == "b":
    p = input("Please enter a number of Parsecs:")
    print(float(p), "Parsecs is equal to", float(p) * 3.26156, "Light-Years.")
else:
    print("Error: not a valid value!")

# End
