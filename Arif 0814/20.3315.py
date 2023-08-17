import requests
from bs4 import BeautifulSoup
import csv
import re

url = 'https://www.usitc.gov/commissioner_bios'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203'
}

fields = ['Names','Roles','Titles','PII','Link Bio Page Detail']
filename = '20.3315.csv'

data = []

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')
        
list_item = []
processed_urls = set()

element_titles = soup.find('div', id='block-usitc-v2-page-title')
title = element_titles.find('h1').text.strip()

# print(title)


find_section = soup.find('div', class_='view-header')
list_bio = find_section.find_all('div', class_='bio-content')

for itembio in list_bio:
    roles_element = itembio.find('div', class_='bio-position')
    if roles_element:
        roles = roles_element.text.strip()
    else:
        roles = ''
    
    for linkItem in itembio.find_all('a', class_='views-more-link', href=True):
        urldetail = 'https://www.usitc.gov' + linkItem['href']

        if urldetail not in processed_urls:
            list_item.append((urldetail, roles))  
            processed_urls.add(urldetail)
            
for bioDetail, roles in list_item:  
    r = requests.get(bioDetail, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')


    name = soup.find('span', class_='field field--name-title field--type-string field--label-hidden').text.strip()

    find_section_p = soup.find('div', class_='clearfix text-formatted field field--name-field-bio-summary field--type-text-with-summary field--label-hidden field__item')

    element_pII = find_section_p.find_all('p')
    _pII = []

    for pII_ in element_pII:
        _pII.append(pII_.text)

    pII_text = '\n'.join(_pII)

    data_save = {
        'Roles' : roles,
        'Names' : name.replace(roles,'').strip(),
        'Titles' : title,
        'PII' : pII_text,
        'Link Bio Page Detail' : bioDetail
    }

    data.append(data_save)
    print('Saving', data_save['Names'])
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)



