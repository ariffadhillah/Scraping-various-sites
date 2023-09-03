import requests
from bs4 import BeautifulSoup
import csv
import re

url = 'https://nationals.org.au/federal-management-committee/'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62'
}

data = []

fields = ['Names' ,'Roles' , 'Titles']
filename = '20.0653.csv'

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

find_section = soup.find('div', id='content')

title = soup.find('div', class_='page-title-head hgroup').text.strip()

find_item = find_section.find_all('div', class_='vc_row wpb_row vc_row-fluid')
for list_item in find_item:
    col_item = list_item.find('div', class_='wpb_column vc_column_container vc_col-sm-9')

    for info in col_item:
        name_elements = info.find_all('h3')
        for name_element in name_elements:
            name = name_element.text.strip()

        roles = info.find('p').text.strip()

        data_save = {
            'Names' : name,
            'Roles' : roles,
            'Titles': title,
        }

        data.append(data_save)
        print('Saving', data_save['Names'])
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            writer.writerows(data)

