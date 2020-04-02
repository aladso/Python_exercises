import json
from collections import Counter
from bokeh.plotting import figure, show, output_file


def count_bd(bd):
    month = []
    lst = [bd[ii].split('/') for ii in bd]
    print(lst)
    for ii in range(0, len(lst)):
        month.append(lst[ii][1])
    count = Counter(month)
    print(count)
    return count


def plot_bd_count(count):
    output_file('bd_count.html')
    x_axis = [ii for ii in count]
    y_axis = [count[ii] for ii in count]
    x_range = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    p = figure(x_range=x_range)
    p.vbar(x=x_axis, top=y_axis, width=0.5)
    show(p)


if __name__ == '__main__':
    x = 1

    while x == 1:
        b = 0
        with open('birthdays.json', 'r') as f:
            birthdays = json.load(f)

        cnt = count_bd(birthdays)
        plot_bd_count(cnt)
        print('Welcome to the birthday dictionary. We know the birthdays of: ')
        for i in birthdays:
            print(i)
        if str(input('Do you want to know a birthday? [y/n]: ')) == 'y':
            b = 1
        while b == 1:
            user_b = str(input('Which birthday do you want to know?: ')).capitalize()
            print(user_b)
            if user_b not in birthdays:
                print('Please enter a valid name')
            else:
                print('{} birthday is {}'.format(user_b, birthdays[user_b]))
                b = 0

        more_b = str(input('Would you like to add any other birthday? [y/n]: ')).lower()
        if more_b == 'y':
            name = str(input('Please insert a name: ')).capitalize()
            birthday = str(input('Please insert birthday in format dd/mm/yyyy: '))
            birthdays[name] = birthday

        with open('birthdays.json', 'w') as f:
            json.dump(birthdays, f)

        user = str(input('Do you want to try again? [y/n]: ')).lower()
        if user == 'n':
            x = 0
