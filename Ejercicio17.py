from bs4 import BeautifulSoup
import requests


def get_headers():
    url = "https://www.nytimes.com/"
    r = requests.get(url)
    r_html = r.text  # We access the data decoded by requests with .text

    soup = BeautifulSoup(r_html, 'html.parser')  # It analyzes the data obtained by requests
    titles = soup.find_all('h2')  # 'h2' is the class of the header in the html code
    titles = [i.get_text() for i in titles]  # We use .get_text to extract all the text in 'h2' class
    return titles


if __name__ == '__main__':
    y = get_headers()
    for z in y:
        print(str(z))
