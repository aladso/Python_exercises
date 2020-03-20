# Give every divisor for a given number

x = 1

while x == 1:
    num = int(input("Please insert a number: "))
    div = []

    ls = range(1, num + 1)
    for i in ls:
        a = num % i
        if a == 0:
            div.append(i)

    print("Divisors are the following list: " + str(div))

    c = str(input("Do you want to repeat? [y/n]: "))
    if c == "n":
        x = 0
