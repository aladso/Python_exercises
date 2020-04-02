# The objective is to find out if a number is on a list

import random


def gen_random_sorted_list():
    lst = []

    for i in range(0, random.randint(5, 11)):
        lst.append(random.randint(0, 30))

    lst.sort()
    print(lst)
    return lst  # We could use lst.sort(reverse=True) to sort it from higher number to lower number


def binary_search():
    lst = gen_random_sorted_list()
    middle_index = len(lst)//2  # The operator // returns a int value
    middle_value = lst[middle_index]
    user_num = int(input("Please insert an integer number: "))
    q = 1
    while q == 1:
        if middle_value == user_num:
            print("The number is in the list")
            q = 0
        elif middle_value > user_num:
            lst = lst[:middle_index]
        elif middle_value < user_num:
            lst = lst[middle_index + 1:]

        if user_num in lst:
            print("The number is in the list")
            q = 0
        else:
            print('The number is not in the list')
            q = 0


def check_number():

    lst = gen_random_sorted_list()
    x = 1

    while x == 1:
        user_num = int(input("Please insert an integer number: "))
        if user_num in lst:
            print("The number is in the list")
        else:
            print('The number is not in the list')

        user = str(input('Do you want to check it again? [y/n]: '))
        if user == 'n':
            x = 0


if __name__ == '__main__':
    check_number()
