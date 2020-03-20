# Game to guess a given number

import random

print("Hello and welcome to the game where you will have to guess the number between 1 and 9")
x = 1
guess = 0

while x == 1:

    options = [int(i) for i in range(1, 10)]
    num = random.choice(options)

    u_num = int(input("Please insert a number between 1 and 9, both included: "))

    if u_num in range(1, 10):
        if u_num == num:
            print("Congrats!! You guessed it right!!")
            guess = guess + 1
        elif u_num < num:
            print("You guessed it too low :(")
        elif u_num > num:
            print("you guessed it too high :(")
    else:
        print("Your input is not correct")

    print("If you don't want to play again please type 'exit': ")
    user = str(input("If you don't want to play again please type 'exit', otherwise press enter: "))
    if user == "exit":
        x = 0

print("Thanks for playing, your number of guesses was: " + str(guess))
