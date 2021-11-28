# Name: Numaan Qureshi
# Email: numaan.qureshi58@myhunter.cuny.edu
# Date: 18 November 2021

import math

def is_square(positive_int):
    root = math.sqrt(positive_int)
    return positive_int == int(root + 0.5) ** 2

def perfectSquareChecker(num):
    if not (is_square(num)):
        print("Hey, this number isn't even! Try again next time.")
        return

    print("This number is a perfect square, it is the product of:", math.sqrt(num), "squared.")

def main():
    """
    You are provided the above two functions, your job now is to take
    user input and validate it. In other words, take integer input from
    the user, and make sure that it is a perfect square. If it's not,
    you need to keep asking the user for a perfect square until they
    enter one.
    Hint, you should use a while loop to validate input!
    Another hint, you are provided the function (is_square) which will
    check to see if a positive integer is a perfect square or not!
    """
    integer = int(input("Please enter an integer:"))
    is_square(integer)
    while not is_square(integer):
        perfectSquareChecker(integer)
        integer = int(input("Please enter an integer:"))
    perfectSquareChecker(integer)




if __name__ == "__main__":
    main()


