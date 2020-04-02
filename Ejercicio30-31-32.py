# The objective is to program the Hangman game

import random


def pick_rnd_word():
    lst = []
    with open('sowpods.txt', 'r') as f:
        line = f.readline()
        while line:
            lst.append(line.strip())
            line = f.readline()
    wrd = random.choice(lst)
    return wrd


def hangman_game():
    board = []
    x = 1
    tries = 0
    wrd = pick_rnd_word()

    wrd_lst = list(wrd)  # I could use a set instead of a list to check faster if a letter is in a word
    rnd_letter = random.choice(wrd_lst)
    size = len(wrd_lst)
    for i in range(0, size):
        board.append('_')

    for i in range(0, size):
        if rnd_letter == wrd_lst[i]:
            board[i] = rnd_letter
    print(str(' '.join(board)))

    while x == 1:
        count = 0
        print('You have ' + str(6 - tries) + ' tries left!')
        user_letter = str(input('Please enter a letter: ')).upper()
        letter = list(user_letter)
        for i in range(0, size):
            for j in range(0, len(letter)):
                if letter[j] == wrd_lst[i]:
                    board[i] = letter[j]

        for j in range(0, len(letter)):
            if letter[j] not in wrd_lst:
                print('Letter not in the word, try again!')
                tries += 1

        print(str(' '.join(board)))
        for i in board:
            if i == '_':
                count += 1
        if count == 0:
            print('Well done! you WIN!!')
            x = 0
        elif tries == 6:
            print('Sorry but you LOST')
            print('The word was: ' + str(wrd))
            x = 0


if __name__ == '__main__':
    print('Welcome to Hangman game!')
    xm = 1
    while xm == 1:
        hangman_game()

        user = str(input('Do you want to play again? [y/n]: ')).lower()
        if user == 'n':
            xm = 0
