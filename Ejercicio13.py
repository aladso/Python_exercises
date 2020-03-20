# Calculate Fibonacci sequence for a given number of values


def fibonacci():
    values_asked = int(input("How many numbers of the Fibonacci sequence do you want? --> "))
    v = 1
    fib = [0, 1]

    if values_asked > 1:
        while v < values_asked - 1:
            fib.append(fib[v - 1] + fib[v])
            v = v + 1  # We can add v += 1, which is the same as v = v + 1

        print("The Fibonacci sequence asked is: " + str(fib))
    elif values_asked == 0:
        print("Enter a number different from 0 please.")
    elif values_asked == 1:
        print("The Fibonacci sequence asked is: " + str(fib[0]))


x = 1
while x == 1:
    fibonacci()

    user = str(input("Do you want to calculate it again? [y/n]: "))
    if user == "n":
        x = 0
