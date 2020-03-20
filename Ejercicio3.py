# Determine if there is a lower number in the given list.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
x = 1  # Be careful with not using the same variable for the while loop and for the for loop

while x == 1:
    b = []
    num = int(input("Please enter a number to see if there is a lower number on the given list: "))

    for i in a:
        if i < num:
            # The first part was print(i) to show the objects < num of the list one-by-one.
            b.append(i)
    print("b = " + str(b))
    # print([aa for aa in a if aa < 5]) to show the list in a single line

    c = str(input("Do you want to repeat? [y/n]: "))
    if c == "n":
        x = 0
