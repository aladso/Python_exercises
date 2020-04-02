# The objective is to get user input for the three in a row game


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
    g = 1
    zeros = 0
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
            print(game)
        zeros -= 1
        if zeros == 0:
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
            print(game)
        zeros -= 1
        if zeros == 0:
            g = 0

    return game


if __name__ == '__main__':
    gm = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    result = locate_user(gm)
    print('The final result is ' + str(result))

