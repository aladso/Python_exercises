# The objective is to know if a number is even, multiple of 4 or odd

i = 1

while i == 1:
    num = int(input("Please enter a number: "))
    a = num % 2
    b = num % 4
    if a == 0 and b != 0:
        print("The number " + str(num) + " is even")
    elif a == 0 and b == 0:
        print("The number " + str(num) + " is even and a multiple of 4")
    else:
        print("The number " + str(num) + " is odd")

    check = int(input("Please enter a number for dividing the first number: "))
    c = num % check

    if c == 0:
        print("The number " + str(check) + " divides evenly the number " + str(num))
    else:
        print("The number " + str(check) + " does not divide evenly the number " + str(num))

    d = str(input("Do you want to repeat the game) [y/n]: "))

    if d == "n":
        i = 0


