#Name: Numaan Qureshi
#Email: numaan.qureshi58@myhunter.cuny.edu
#Date: September 20 2021
#This program reverses an entered phrase and finds its acronym.

phrase = input("Enter a phrase:")

d = phrase[::-1]
print("Reversed Phrase:", d)

x = d.upper()
y = x.split()

myString = ""

for z in range(len(y)):
  myString += (y[z][-1])

print("Last letters of reversed words:", myString)
