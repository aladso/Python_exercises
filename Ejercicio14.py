# The objective is to create a list of unique values in a list given by the user


def eliminate_dup_set(ls):

    new_list = set()
    for i in ls:
        new_list.add(i)
    print("These are the unique values in the list: " + str(new_list))


def eliminate_dup_list(ls):

    new_list = []
    for i in ls:
        if i not in new_list:
            new_list.append(i)

    print("These are the unique values in the list: " + str(new_list))


x = 1
while x == 1:
    user_ls = [1, 2, 6, 1, 8, 2]
    y = 1

    while y == 1:
        option = int(input("Using set (1) or list (2)?: "))  # If I put this line out of the while --> infinite loop
        if option == 1:
            eliminate_dup_set(user_ls)
            y = 0
        elif option == 2:
            eliminate_dup_list(user_ls)
            y = 0
        else:
            print("Please insert a correct value")

    user = str(input("Do you want to repeat? [y/n]: "))
    if user == "n":
        x = 0

