import requests
from bs4 import BeautifulSoup
import csv

url = 'https://bom.mu/financial-stability/supervision/licensees/list-of-licensees?field_licensees_type_value=2'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69'
}

data = []

fields = ['Company Name' , 'Address']
filename = '90.0773.csv'

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

find_section = soup.find_all('div', {'class':['views-column col-sm-6 views-column-1 views-column-first','views-column col-sm-6 views-column-2 views-column-last']})

for info in find_section:
    companyName = info.find('div', class_='views-field views-field-title').text.strip()
    address = info.find('div', class_='views-field views-field-body').text.strip()

    data_save = {
        'Company Name' : companyName.strip(),
        'Address' : address
    }
    data.append(data_save)
    print('Saving', data_save['Company Name'])
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)