import requests
from bs4 import BeautifulSoup

URL = 'https://www.nytimes.com/'


def get_nyt_titles():
    response = requests.get(URL).text
    soup = BeautifulSoup(response, 'html.parser')
    titles = soup.find_all('h2')
    titles = [element.get_text() for element in titles]
    return titles[:-2]


def run():
    titles = get_nyt_titles()
    print(titles)


if __name__ == "__main__":
    run()
