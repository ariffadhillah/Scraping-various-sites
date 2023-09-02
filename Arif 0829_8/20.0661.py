import requests
from bs4 import BeautifulSoup
import csv
import re

url = 'https://www.national.org.nz/team'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62'
}

data = []

fields = ['Names' ,'Roles' , 'PII']
filename = '20.0661.csv'

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

find_item = soup.find_all('div', {'class':['col-12 col-lg-6','col-12 col-lg-3 mb-4']})

for info_item in find_item:
    name_element = info_item.find('h3', {'class':['mb-3 w-100 float-left text-uppercase' , 'mb-3 w-100 float-left']})
    element_PII = info_item.find('div', {'class':['cont','cont text-white']})
    
    if name_element and element_PII:
        name = name_element.text.strip()
        roles = element_PII.find(['h5','strong']).text.strip().title()
        try:
            text_PII = element_PII.find('p').text.strip().title()
        except:
            text_PII = ''

        data_save = {
            'Names' : name,
            'Roles' : roles,
            'PII': text_PII.replace(roles,'').strip(),
        }

        data.append(data_save)
        print('Saving', data_save['Names'])
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            writer.writerows(data)