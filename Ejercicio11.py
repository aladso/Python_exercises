# The objective is to determine if a number is prime or not


def get_int(text="Please enter an integer: "):  # I introduced a default value when defining the function
    return int(input(text))


x = 1
print("Hi!! In this code I will tell you if a number is prime or not\n")

while x == 1:

    count = 0

    num = get_int()
    check = [int(i) for i in range(1, num + 1)]
    print(str(check))

    div = [int(i) for i in check if num % i == 0]
    print(str(div))

    for j in div:
        if j != 1 and j != num:
            count = count + 1

    if count > 0:
        print("Your number is not prime")
    else:
        print("Your number is PRIME")

    user = str(input("Do you want to give another number? [y/n]: "))
    if user == "n":
        x = 0
