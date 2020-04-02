if __name__ == '__main__':
    birthdays = {'Alejandro': '01/08/1996', 'Jose': '01/05/1971', 'Marta': '14/04/2004', 'Maria': '15/05/1998'}
    x = 1
    for i in birthdays:
        print(i)

    while x == 1:

        print('Welcome to the birthday dictionary. We know the birthdays of: ')
        for i in birthdays:
            print(i)
        b = 1
        while b == 1:
            user_b = str(input('Which birthday do you want to know?: ')).capitalize()
            print(user_b)
            if user_b not in birthdays:
                print('Please enter a valid name')
            else:
                print('{} birthday is {}'.format(user_b, birthdays[user_b]))
                b = 0

        user = str.lower(input('Do you want to try again? [y/n]: '))
        if user == 'n':
            x = 0

