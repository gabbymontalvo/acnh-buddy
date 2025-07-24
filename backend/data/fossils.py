import requests
from bs4 import BeautifulSoup

# getting soup object from html string
def get_soup(url):
    str_html = requests.get(url).text
    soup = BeautifulSoup(str_html)
    return soup

url = 'https://nookipedia.com/wiki/Fossil/New_Horizons'
soup = get_soup(url)

# make sure soup is woroking
print(soup)

# trying to locate table using .find
fossil_table = soup.find('table', class_= ['sortable', 'jquery-tablesorter'])

# empty list 
fossils = []

# looping through table to try and find all fossils
for row in fossil_table.find_all('tr')[1:]:
    cells = row.find_all('td')
    name = cells[0].get_text(strip = True)
    price = cells[3].get_text(strip = True)
    museum = cells[4].get_text(strip = True)

    fossils.append({
        'name': name,
        'sell_price': price,
        'museum_desc': museum
    })

# run to make sure works!
for fossil in fossils:
    print(fossil)