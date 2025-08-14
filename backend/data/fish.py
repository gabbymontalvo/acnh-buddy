import requests
from bs4 import BeautifulSoup

# get soup from html string
def get_soup(url):
    str_html = requests.get(url).text
    soup = BeautifulSoup(str_html)
    return soup

url = 'https://nookipedia.com/wiki/Fish/New_Horizons'
soup = get_soup(url)

fish_table = soup.find('table', class_= ['sortable', 'jquery-tablesorter'])

fish = []

for row in fish_table.find_all('tr')[1:]:
    cells = row.find_all('td')
    name = cells[1].get_text(strip = True)

    img_tag = cells[2].find('img')
    img_url = None
    if img_tag and 'src' in img_tag.attrs:
        img_url = img_tag['src']

    price = cells[3].get_text(strip = True).replace('Bells', ' Bells')

    fish.append({
        'name': name,
        'image_url': img_url,
        'sell_price': price
    })

for fishies in fish:
    print(fishies)

# Notes:
# make list more comprehensive for fish
# - add image, maybe time of day can be caught?
# - both fish and fossils super basic right now
# - but successful first two webscrapes
# - next: bugs