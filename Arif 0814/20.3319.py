import requests
from bs4 import BeautifulSoup
import csv
import re

url = 'https://www.nlrb.gov/about-nlrb/who-we-are/the-board'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203'
}

fields = ['Names', 'Roles' , 'Biography']
filename = '20.3319.csv'

data = []

list_item = []
processed_urls = set()

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

find_section = soup.find('div', class_='flex-row')
# print(find_section)


for linkItem in find_section.find_all('a',  href=True):
    urlbio = linkItem['href'].replace('/about-nlrb/who-we-are/board/','').replace('/bio/david-m-prouty','david-m-prouty')
    # print(urlbio)
    urldetail = 'https://www.nlrb.gov/bio/' + urlbio

    if urldetail not in processed_urls:
        list_item.append((urldetail))  
        processed_urls.add(urldetail)

for bioDetail in list_item:  
    r = requests.get(bioDetail, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    
    print(bioDetail)

    name = soup.find('h1', class_='uswds-page-title page-title').text.strip()
    roles = soup.find('div', class_='field field--name-field-bio__officer-title field--type-string field--label-hidden field__item').text.strip()

    section_bio = soup.find('div', class_='node__content')

    if section_bio:
        biography_paragraphs = section_bio.find_all('p')
        biography = '\n\n'.join([p.text for p in biography_paragraphs]) 

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

