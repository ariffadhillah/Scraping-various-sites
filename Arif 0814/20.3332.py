import requests
from bs4 import BeautifulSoup
import csv
import re

url = 'https://ncua.gov/about/ncua-board'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203'
}

fields = ['Names', 'Roles' , 'Titles']
filename = '20.3332.csv'

data = []

list_item = []
processed_urls = set()

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

find_section = soup.find('div', id='block-main-content')

title = soup.find('h1', class_='title page-title').text.strip()

find_description = find_section.find_all('div', class_='description')

for info in find_description:
    name = info.find('h2').text.strip()
    roles = info.find('p').text.strip()

    data_save = {
        'Names' : name,
        'Roles' : roles,
        'Titles' : title
    }

    data.append(data_save)
    print('Saving', data_save['Names'])
        # print( )
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)

