import requests
from bs4 import BeautifulSoup
import csv
import re

url = 'https://www.prc.gov/leadership'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203'
}

fields = ['Names','Roles','Biography']
filename = '20.3324.csv'

data = []

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

listbio = []
processed_urls = set()

find_section = soup.find('div', class_='item-list')

find_li = find_section.find_all('li')

for find_href in find_li:
    anchor_tags = find_href.find_all('a', href=True)
    for anchor in anchor_tags:
        linkbio = 'https://www.prc.gov' + anchor['href']

        if linkbio not in processed_urls:
            listbio.append(linkbio)
            processed_urls.add(linkbio)

for detailsbio in listbio:
    r = requests.get(detailsbio, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    print(detailsbio)    
    find_desc_bio = soup.find('div', class_='ds-2col-stacked node node-commissioner node-full view-mode-full clearfix')

    name = find_desc_bio.find('div', class_='field field-name-title field-type-ds field-label-hidden').text.strip()
    roles = find_desc_bio.find('div', class_='field field-name-field-position field-type-text field-label-hidden').text.strip()
    biography = find_desc_bio.find('div', class_='group-left').text.strip()

    data_save = {
        'Names' : name,
        'Roles' : roles,
        'Biography' :biography
    }
    data.append(data_save)
    print('Saving', data_save['Names'])
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)




