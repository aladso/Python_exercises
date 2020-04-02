# The objective is to see which elements are present in the both files that are going ot be inspected


def get_filename():
    filename = str(input("Please insert file name you want to read: "))
    return filename


def read_file(file_name):
    lst = []
    with open(file_name + '.txt', 'r') as f:
        line = f.readline()
        while line:
            lst.append(int(line))
            line = f.readline()

    return lst


def compare_lists(list1, list2):

    aux_list = []

    for j in list1:
        if j in list2:
            aux_list.append(j)

    return aux_list


if __name__ == '__main__':
    filename1 = get_filename()
    lst1 = read_file(filename1)
    print(lst1)

    filename2 = get_filename()
    lst2 = read_file(filename2)
    print(lst2)
    
    auxlst = compare_lists(lst1, lst2)
    print("The list of overlapped numbers is: " + str(auxlst))
