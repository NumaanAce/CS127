#Name: Numaan Qureshi
#Email: numaan.qureshi58@myhunter.cuny.edu
#Date:
#This program prints a user's chosen message and a letter in various ways.

message = input("Please enter a message:")
letter = input("Please enter a letter:")
print("You entered", message)
print("Your message in uppercase is", message.upper())
print("Your message in lowercase is", message.lower())
print("The total amount of your entered letter in your message is", message.count(letter))
