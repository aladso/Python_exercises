# Rock, paper, scissors game with two players

x = 1
name_p1 = str(input("What's your name Player 1?: "))
name_p2 = str(input("What's your name Player 2?: "))
score_p1 = 0
score_p2 = 0

while x == 1:

    p1 = str(input(name_p1 + ", what are you choosing? please put it in lowercase: "))
    p2 = str(input(name_p2 + ", what are you choosing? please put ir in lowercase: "))

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

    print("--------------\n" + "Scoreboard\n" + name_p1 + ": " + str(score_p1) + "\n" + name_p2 + ": " + str(score_p2)
          + "\n--------------")

    if score_p1 > score_p2:
        print(name_p1 + " is winning the game by " + str(score_p1-score_p2))
    elif score_p2 > score_p1:
        print(name_p2 + " is winning the game by " + str(score_p2-score_p1))
    elif score_p2 == score_p1:
        print("It is a draw")

    user = str(input("Do you want to play again? [y/n]: "))
    if user == "n":
        x = 0
