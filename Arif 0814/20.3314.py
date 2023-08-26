import requests
from bs4 import BeautifulSoup
import csv
import re

url = 'https://www.gsa.gov/about-us/organization/leadership-directory?topnav=about-us'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203'
}

fields = ['Names', 'Roles', 'Titles' ]
filename = '20.3314.csv'

data = []

list_item = []
processed_urls = set()

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

find_section = soup.find('div', id='leadership')

find_item = find_section.find_all('div', {'class': ['grid-row grid-gap-md']})

for item_card in find_item:
    card_item = item_card.find_all('p')
    
    title_element = item_card.find_previous_sibling('h2', class_='staff-office')
    title = title_element.text.strip() if title_element else ""
    
    for item_text in card_item:
        info_text = list(item_text.stripped_strings)

        if info_text:
            name = info_text[0]
            roles = '  ,  '.join(info_text[1:])

            data_save = {
                'Names': name,
                'Roles': roles.replace(name, '').replace('Biography', '').strip(),
                'Titles': title
            }
            data.append(data_save)
            print('Saving', data_save['Names'])

# Menulis data ke file CSV setelah selesai looping
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(data)
