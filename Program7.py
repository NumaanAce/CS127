#Name: Numaan Qureshi
#Email: numaan.qureshi58@myhunter.cuny.edu
#Date: September 16 2021
#This program shifts an entered message by five letters.

myString = input("Enter a message:")

for c in myString:
  print(c, "shifted by 5 characters is:", chr(ord(c) + 5))
