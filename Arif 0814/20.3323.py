import requests
from bs4 import BeautifulSoup
import csv
import re

url = 'https://www.peacecorps.gov/about/leadership/'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203'
}

fields = ['Names', 'Roles', 'Biography' ]
filename = '20.3323.csv'

data = []

list_item = []
processed_urls = set()

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

find_section = soup.find_all('div', class_='layout-main-content')[1]

name = find_section.find('h3').text.strip()
roles = find_section.find('h4').text.strip()

if find_section:
    bio = find_section.find_all('p')[:6]
    biography = '\n\n'.join([paragraph.text for paragraph in bio])
        
    data_save = {
        'Names' : name,
        'Roles' : roles,
        'Biography' : biography
    }

    data.append(data_save)
    print('Saving', data_save['Names'])
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)


