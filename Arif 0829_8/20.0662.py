import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.act.org.nz/people'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62'
}

data = []

fields = ['Names', 'Roles', 'Titles']
filename = '20.0662.csv'

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

title = soup.find('h1', class_='headline mb-3').text.strip()

find_item = soup.find_all('div', class_='person-wrap person-type-basic')
for find_people in find_item:
    name = find_people.find('h3').text.strip()
    roles = find_people.find('div', class_='mp-title-role').text
    # print(name)
    # print()
    # print(title)

    data_save = {
        'Names' : name,
        'Roles' : roles.replace('\n','').replace('         ',' ').strip(),
        'Titles' : title
    }

    data.append(data_save)
    print('Saving', data_save['Names'])
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)