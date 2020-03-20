# The objective is playing rock, paper and scissors against the machine

import random

print("Welcome to rock, scissors, paper game!!")
x = 1
name_p1 = str(input("What's your name Player 1?: "))
name_p2 = str("Computer")
score_p1 = 0
score_p2 = 0
pos = ["scissors", "paper", "rock"]

while x == 1:

    y = 1
    p1 = str(input(name_p1 + ", what are you choosing? please put it in lowercase: "))
    p2 = random.choice(pos)
    print(name_p2 + " selects " + p2)

    if p1 == p2:
        print("Draw!!")
    elif p1 == "scissors" and p2 == "paper":
        print("Congratulations " + name_p1 + ", you won!")
        score_p1 = score_p1 + 1
    elif p1 == "paper" and p2 == "scissors":
        print("Congratulations " + name_p2 + ", you won!")
        score_p2 = score_p2 + 1
    elif p1 == "rock" and p2 == "paper":
        print("Congratulations " + name_p2 + ", you won!")
        score_p2 = score_p2 + 1
    elif p1 == "paper" and p2 == "rock":
        print("Congratulations " + name_p1 + ", you won!")
        score_p1 = score_p1 + 1
    elif p1 == "scissors" and p2 == "rock":
        print("Congratulations " + name_p2 + ", you won!")
        score_p2 = score_p2 + 1
    elif p1 == "rock" and p2 == "scissors":
        print("Congratulations " + name_p1 + ", you won!")
        score_p1 = score_p1 + 1
    else:
        print(name_p1 + " input is not correct")
        y = 0

    if y != 0:
        print(
            "--------------\n" + "Scoreboard\n" + name_p1 + ": " + str(score_p1) + "\n" + name_p2 + ": " + str(score_p2)
            + "\n--------------")

        if score_p1 > score_p2:
            print(name_p1 + " is winning the game by " + str(score_p1 - score_p2))
        elif score_p2 > score_p1:
            print(name_p2 + " is winning the game by " + str(score_p2 - score_p1))
        elif score_p2 == score_p1:
            print("It's a draw!")

    user = str(input("Do you want to play again? [y/n]: "))
    if user == "n":
        x = 0

if score_p1 > score_p2:
    print("The winner is " + name_p1 + "!!")
elif score_p2 > score_p1:
    print("The winner is " + name_p2 + "!!")
elif score_p2 == score_p1:
    print("It's a draw!")
