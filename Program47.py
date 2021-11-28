# Name: Numaan Qureshi
# Email: numaan.qureshi58@myhunter.cuny.edu
# Date: 18 November 2021

import random as rd

playerMove = int(input('Please enter an integer. 1 for "Rock", 2 for "Paper", 3 for "Scissors": '))
computerMove = rd.randrange(1, 4)

while playerMove > 0:
    print(computerMove)
    if playerMove == 1 and computerMove == 1:
        print("Round finished and the result is Draw")
    elif playerMove == 1 and computerMove == 2:
        print("Round finished and the winner is Computer")
    elif playerMove == 1 and computerMove == 3:
        print("Round finished and the winner is Human")
    elif playerMove == 2 and computerMove == 1:
        print("Round finished and the winner is Human")
    elif playerMove == 2 and computerMove == 2:
        print("Round finished and the result is Draw")
    elif playerMove == 2 and computerMove == 3:
        print("Round finished and the winner is Computer")
    elif playerMove == 3 and computerMove == 1:
        print("Round finished and the winner is Computer")
    elif playerMove == 3 and computerMove == 2:
        print("Round finished and the winner is Human")
    elif playerMove == 3 and computerMove == 3:
        print("Round finished and the result is Draw")
    elif playerMove > 3 or playerMove < 0:
        print("Round finished and the result is Invalid")
    playerMove = int(input('Please enter an integer. 1 for "Rock", 2 for "Paper", 3 for "Scissors": '))
    computerMove = rd.randrange(1, 4)

if playerMove == 0:
    print("Game is finished and the winner is Human")


# END
