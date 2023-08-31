import requests
from bs4 import BeautifulSoup
import csv

url = 'https://greens.org.au/about/office-bearers'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62'
}

data = []

fields = ['Names', 'Roles' , 'Email']
filename = '20.0654.csv'

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

find_section = soup.find_all('div', class_='d-flex col-md-6 col-xl-4')

for info in find_section:
    name = info.find('h1').text.strip()
    roles = info.find_all('p')[1].text.strip()
    email = info.find('a', class_='btn btn-primary btn-sm')['href']

    data_save = {
        'Names' : name,
        'Roles' : roles,
        'Email' : email.replace('mailto:','')
    }

    data.append(data_save)
    print('Saving', data_save['Names'])
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)
