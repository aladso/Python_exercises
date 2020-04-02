# The goal is to return the maximum between a list of numbers


def get_variables():
    lst = []
    i = 0
    size = int(input('How many numbers do you want to get the maximum from?: '))
    while i < size:
        lst.append(int(input("Please enter an integer number: ")))
        i += 1

    return lst


def get_max(lst):
    max_ = -1E-30
    for i in lst:
        if i > max_:
            max_ = i

    return max_


if __name__ == '__main__':
    nums = get_variables()
    maxi = get_max(nums)
    print('The maximum number of the list is ' + str(maxi))
