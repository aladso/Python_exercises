# The objective is to get an article for a given url

import requests
from bs4 import BeautifulSoup


def get_article():

    url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
    r = requests.get(url)
    r_html = r.text

    soup = BeautifulSoup(r_html, 'html.parser')
    text = soup.find_all('p')
    for i in text:
        print(i.get_text())


if __name__ == '__main__':
    get_article()
