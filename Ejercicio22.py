# The objective is to read a file and count the number of a main word that appears in the text


def count_photos():
    dictionary = {}  # Be careful initializing a dictionary. The keys are different from lists
    with open('Ex22.txt', 'r') as f:
        line = f.readline()
        while line:
            line = str(line[3:-26])  # This way we grab from the 3rd to the 26th (starting from the end)
            if line in dictionary:
                dictionary[line] += 1
            else:
                dictionary[line] = 1

            line = f.readline()  # We need to update the process reading a new line
        print(dictionary)


if __name__ == '__main__':
    count_photos()

