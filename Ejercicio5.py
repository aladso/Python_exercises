# Create a list with every number they have in common, skipping duplicates

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 254]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 254, 300]

common = []

for i in a:
    for j in b:
        if i == j and i not in common:  # We add 'i not in common' to avoid duplicates
            common.append(i)

print("The common list is: " + str(common))
