# The objective is to create a file with the information obtained from a website

import requests
from bs4 import BeautifulSoup


def get_article():

    url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
    r = requests.get(url)
    r_html = r.text

    soup = BeautifulSoup(r_html, 'html.parser')
    text = soup.find_all('p')
    f_name = str(input('Please enter a name for the new file: '))
    with open(f_name + '.txt', 'w') as new_file:
        for i in text:
            new_file.write(i.get_text())
            new_file.write('\n')


if __name__ == '__main__':
    get_article()

