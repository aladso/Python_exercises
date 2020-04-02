# The objective is to make the computer guess a user number in the most optimal way


def ask_user_num():
    user_num = 0
    x = 1
    while x == 1:
        user_num = int(input('Please enter an integer number between 0 and 100: '))
        if user_num not in range(0, 101):
            print('Please enter a correct number')
        else:
            x = 0
    return user_num


def guess_number(user_num):
    tries = 0
    maximum = 100
    minimum = 0
    computer_num = 50
    x = 1
    while x == 1:  # We use binary search to optimize searching process
        tries += 1
        if computer_num < user_num:
            print('Computer guessed too low')
            minimum = computer_num + 1
        elif computer_num > user_num:
            print('You guessed it too high')
            maximum = computer_num - 1
        elif computer_num == user_num:
            print('Your number is ' + str(computer_num))
            print('Computer guessed it in ' + str(tries) + ' tries')
            x = 0
        computer_num = (maximum + minimum)//2


if __name__ == '__main__':
    y = 1
    while y == 1:
        num = ask_user_num()
        guess_number(num)

        user = str(input('Do you want to play again? [y/n]: '))
        if user == 'n':
            y = 0
