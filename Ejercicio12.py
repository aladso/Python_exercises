# Making a list with the first and the last element of a list
import random


def first_and_last(ls):
    f_l = [ls[:1], ls[-1:]]
    return f_l


# Instead of using the given list, I generate a random one
a = []
for i in range(0, random.randint(1, 35)):
    n = random.randint(1, 3465)
    a.append(n)

print("The list with the first and last number of the given list is: " + str(first_and_last(a)))
