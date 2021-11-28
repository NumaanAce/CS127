#Name: Numaan Qureshi
#Email: numaan.qureshi58@myhunter.cuny.edu
#Date: September 23 2021
#This program encrypts an entered message.

message = input("Enter a word here:")
d = message.upper()
print("Your word:", d)

codeWord = ""

for Ch in d:
  offset = ord(Ch) - ord("A") + 13
  wrap = offset % 26
  codeCh = chr(ord("A") + wrap)
  codeWord += codeCh

print("Your word in code is", codeWord)
