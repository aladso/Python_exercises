# The objective is to reverse a collection of words
import os


def str_input():
    user_str = str(input("Please enter a long string (multiple words): "))
    print("Thank you")
    os.system("pause")  # We control the timing of program execution. To continue we must press a key.
    return user_str


def reverse_str(user_str):
    return ' '.join(user_str.split()[::-1])


def reverse_str2(user_str):
    y = user_str.split()  # We have to create the list with full words before, otherwise,
    # we'll reverse the string letter by letter
    y.reverse()  # We could use y = user.split()[::-1] as well
    return " ".join(y)


x = 1
while x == 1:
    str_asked = str_input()
    reversed_str = reverse_str(str_asked)
    print(str(reversed_str))

    user = str(input("Do you want to do it again? [y/n]: "))
    if user == "n":
        x = 0

