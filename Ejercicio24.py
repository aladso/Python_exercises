

def board():
    col = int(input('Insert number of columns: '))
    row = int(input('Insert number of rows: '))
    for i in range(row):
        print(col * ' ---')
        print(col * '|   ' + '|')
    print(col * ' ---')


if __name__ == '__main__':
    board()

