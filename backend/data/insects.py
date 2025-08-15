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

bug_table = soup.find('table', class_= ['sortable', 'jquery-tablesorter'])

bugs = []

for row in bug_table.find_all('tr')[1:]:
    cells = row.find_all('td')
    name = cells[1].get_text(strip = True)
    
    img_tag = cells[2].find('img')
    img_url = None
    if img_tag and 'src' in img_tag.attrs:
        img_url = img_tag['src']

    price = cells[3].get_text(strip = True).replace('Bells', ' Bells')

    bugs.append({
        'name': name,
        'image_url': img_url,
        'sell_price': price
    })

# test
for buggies in bugs:
    print(buggies)