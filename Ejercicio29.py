# The goal is to program the 3 in a row game from the functions programmed previously


def board(game):
    col = 3
    row = 3
    for i in range(row):
        print(col * ' ---')
        print('| ' + str(game[i][0]) + ' | ' + str(game[i][1]) + ' | ' + str(game[i][2]) + ' |')
    print(col * ' ---')


def calculate_winner_rows_columns(game):

    winner = 0
    for i in range(3):  # Check rows
        if game[i][0] == game[i][1] == game[i][2]:
            if game[i][0] != 0:
                print('Player ' + str(game[i][0]) + ' is the winner!')
                winner = game[i][0]

    for i in range(3):  # Check columns
        if game[0][i] == game[1][i] == game[2][i]:
            if game[0][i] != 0:
                print('Player ' + str(game[i][0]) + ' is the winner!')
                winner = game[0][i]

    return winner


def calculate_diagonal_winner(game):
    winner = 0
    if game[0][0] == game[1][1] == game[2][2] != 0:
        print('Player ' + str(game[0][0]) + ' is the winner!')
        winner = game[0][0]
    elif game[0][2] == game[1][1] == game[2][0] != 0:
        print('Player ' + str(game[1][1]) + ' is the winner!')
        winner = game[0][2]

    return winner


def get_user_input(player):
    u = 1
    lst = []
    while u == 1:
        user_input = str(input('Please ' + player + ' insert the coordinates you want to locate your number as x,y: '))
        user_input.strip()
        lst = user_input.split(',')
        if len(lst) != 2:
            print('Please insert valid coordinates')
        elif int(lst[0]) < 1 or int(lst[0]) > 3 or int(lst[1]) < 1 or int(lst[1]) > 3:
            print('Please insert valid coordinates')
        else:
            u = 0

    print(str(lst))
    return lst


def locate_user(game):
    g = 1  # Se puede añadir un input para coger nombres reales para Player1 y Player 2
    zeros = 0
    cr_w = 0
    diag_w = 0
    for i in range(3):
        for j in range(3):
            if game[i][j] == 0:
                zeros += 1

    while g == 1:
        p1_check = 1
        p2_check = 1

        while p1_check == 1:
            player = 'Player 1'
            user_coord = get_user_input(player)
            row = int(user_coord[0]) - 1
            col = int(user_coord[1]) - 1
            if game[row][col] == 0:
                game[row][col] = 1
                p1_check = 0
            else:
                print('Please insert valid coordinates')
            board(game)
            cr_w = calculate_winner_rows_columns(game)
            diag_w = calculate_diagonal_winner(game)
        zeros -= 1
        if zeros == 0:
            g = 0
            p2_check = 0
        elif cr_w != 0 or diag_w != 0:
            g = 0
            p2_check = 0

        while p2_check == 1:
            player = 'Player 2'
            user_coord = get_user_input(player)
            row = int(user_coord[0]) - 1
            col = int(user_coord[1]) - 1
            if game[row][col] == 0:
                game[row][col] = 2
                p2_check = 0
            else:
                print('Please insert valid coordinates')
            board(game)
            cr_w = calculate_winner_rows_columns(game)
            diag_w = calculate_diagonal_winner(game)

        zeros -= 1
        if zeros == 0:
            g = 0
        elif cr_w != 0 or diag_w != 0:
            g = 0
    if cr_w == 0 and diag_w == 0:
        print('It is a draw!!')
    return game


if __name__ == '__main__':
    x = 1
    while x == 1:
        gm = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        result = locate_user(gm)

        user = str(input('Do you want to play again? [y/n]: '))
        if user == 'n':
            x = 0
