import requests
from bs4 import BeautifulSoup
import csv
import re

url = 'https://wellington.govt.nz/your-council/about-the-council/mayor-and-councillors/councillors'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62'
}

data = []

fields = ['Names', 'Roles']
filename = '20.0732.csv'

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

find_item = soup.find_all('a', class_='link-block pb--s landing-item')

for info_item in find_item:
    name = info_item.find('h2').text.strip()
    roles = info_item.find('p').text.strip()
    # print(name)
    # print(roles)

    data_save = {
        'Names' : name,
        'Roles' : roles
    }

    data.append(data_save)
    print('Saving', data_save['Names'])
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)