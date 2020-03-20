# In this exercises the objective is to calculate in which year the user will be 100 years old

import time

strings = time.strftime("%Y,%m,%d,%H,%M,%S")
date = strings.split(",")
date_values = [int(x) for x in date]
year = date_values[0]

i = 1

while i == 1:
    name = input("Introduce your name, please: ")
    name = str(name)
    age = input("Introduce your age, please: ")
    age = int(age)
    # We could also use age = int(input("Introduce your age, please: ")), the same for year_born and name.
    year_born = input("Introduce the year you were born, please: ")
    year_born = int(year_born)

    year100 = year_born + 100

    print("You will turn 100 in " + str(year100))
    x = str(input("Do you want to repeat the process?[y/n]: "))
    if x == "n":
        i = 0
