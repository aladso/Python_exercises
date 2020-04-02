# The objective is to develop the game Cows and Bulls to guess a number

import random


def gen_rand_num():
    return random.randint(1000, 9999)


def cows_and_bulls():
    print('Welcome to the Cows and Bulls Game!')
    rnd_num = gen_rand_num()
    x = 1
    user_num = []
    user_try = 0

    while x == 1:
        y = 1
        while y == 1:
            user_num = int(input('Please insert a 4 digit number: '))
            if user_num in range(1000, 10000):
                y = 0

        user_digits = ''.join(str(user_num))
        rnd_digits = ''.join(str(rnd_num))

        cow = 0
        bull = 4

        for i in range(0, 4):
            if user_digits[i] == rnd_digits[i]:
                cow += 1
                bull -= 1

        print('Cows: ' + str(cow) + '\n' + 'Bulls: ' + str(bull) + '---------------------------\n')
        user_try += 1

        if cow == 4:
            print('Congrats!! You won!\n' + 'You did it in ' + str(user_try) + ' attempts')
            x = 0


if __name__ == '__main__':

    z = 1
    while z == 1:
        cows_and_bulls()
        user_ = str(input('Do you want to play again? [y/n]: '))
        if user_ == 'n':
            z = 0
