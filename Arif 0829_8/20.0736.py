import requests
from bs4 import BeautifulSoup
import csv
import re

url = 'https://www.aucklandcouncil.govt.nz/mayor-of-auckland/Pages/default.aspx'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62'
}

data = []

fields = ['Names','Roles','Titles', 'PII']
filename = '20.0736.csv'

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

find_section = soup.find('div', class_='pattern-card-2-row')

title = soup.find('p', class_='heading-te-reo top green').text.strip()
roles = soup.find('h1').text.strip()

text_PII = soup.find('div', class_='lead m-b-2').text.strip()

name_element = find_section.find('div', class_='card-poster-image')

if name_element:
    name = name_element.get('title').replace('Mayor of Auckland, ','')

    data_save = {
        'Names' : name.replace('.',''),
        'Roles' : roles,
        'Titles' : title,
        'PII': text_PII,
    }
    data.append(data_save)
    print('Saving', data_save['Names'])
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)
