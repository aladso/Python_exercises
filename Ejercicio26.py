# The objective is to calculate the winner of the 3 in a row game


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
    if game[0][0] == game[1][1] == game[2][2]:
        print('Player ' + str(game[0][0]) + ' is the winner!')
        winner = game[0][0]
    elif game[0][2] == game[1][1] == game[2][0]:
        print('Player ' + str(game[1][1]) + ' is the winner!')
        winner = game[0][2]

    return winner


if __name__ == '__main__':
    gm = [[1, 2, 0], [2, 1, 0], [2, 1, 1]]
    diag_w = calculate_diagonal_winner(gm)
    rw_col_w = calculate_winner_rows_columns(gm)
    if diag_w == 0 and rw_col_w == 0:
        print("It's a draw!!")
