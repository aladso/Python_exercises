# The goal is to generate a password according to a strength level given by the user

import random
import string


def password_gen(option):

    password = []
    aux = []
    values = string.ascii_letters + string.digits + string.punctuation
    weak = str("humano, persona, gente, hombre, mujer, familia, amigo, conocido")
    la_string = weak.split(",")

    if option == 1:
        for i in range(0, random.randint(8, 15)):
            aux.append(random.choice(values))
            password = "".join(aux)
            password.replace(" ", "")

    elif option == 0:
        for j in range(0, 2):
            aux.append(random.choice(la_string))
            aux_2 = "".join(aux)
            password = aux_2.replace(" ", "")

    return password


if __name__ == '__main__':

    x = 1
    while x == 1:
        print("Hello and welcome to the password generator")
        user_opt = input("Please enter 0 to generate a weak password or 1 to generate a strong password: ")

        if user_opt != "1" and user_opt != "0":
            print("Input not correct")
        else:
            p = password_gen(int(user_opt))
            print("This is your new password: " + str(p))
        user = str(input("Do you want to generate a new password? [y/n]: "))
        if user == "n":
            x = 0
