import requests
from bs4 import BeautifulSoup

# get soup from insects url, no wifi update variable later
def get_soup(url):
    str_html = requests.get(url).text
    soup = BeautifulSoup(str_html)
    return soup

url = "https://nookipedia.com/wiki/Bug/New_Horizons"
soup = get_soup(url)

# test
print(soup)

