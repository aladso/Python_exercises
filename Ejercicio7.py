# generate a list with the even numbers on a given list

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [i for i in a if i % 2 == 0]  # This way we can compact the code

print(b)
