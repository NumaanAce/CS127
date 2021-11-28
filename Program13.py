# Name: Numaan Qureshi
# Email: numaan.qureshi58@myhunter.cuny.edu
# Date: September 25 2021
# This program lists a user's favorite books and their authors' initials.

books = input("Enter a list of books and their authors:")

a = books.split("; ")
glue = "."

for n in range(len(a)):
    b = a[n].split(" - ")
    c = b[1].split(" ")
    d = [c[0][0], c[1][0], ""]
    e = ".".join(d)
    print(b[0], "by", e)

print("Thank you for using my book organizer!")

# Work Process/Incorrect Attempts
# for n in range(len(a)):
#   b = a[n].split(" - ")
#   c = b[1].split(" ")
#   print(b[0], "by", c[0][0],".",c[1][0])

# for n in range(len(a)):
#   b = a[n].split(" - ")
#   c = b[1].split(" ")
# d = [c[0][0], c[1][0]]
# print(b[0], "by", ".".join(c[0][0],c[1][0]))
