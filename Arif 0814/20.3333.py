import requests
from bs4 import BeautifulSoup
import csv
import re

url = 'https://www.usaid.gov/about-us/organization/leadership-listing'

headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203',
    'Cookie' : 'NSC_xxx_qvcxfc_01_02_mc_ttm=ffffffffaf1c7d1445525d5f4f58455e445a4a42378b; _gid=GA1.2.1483805118.1692230452; _ga=GA1.1.1608810166.1692230452; _ga_ZF8V4X5KXG=GS1.1.1692230452.1.1.1692230543.0.0.0; _ga_CSLL4ZEK4L=GS1.1.1692230451.1.1.1692230543.0.0.0' 
}

fields = ['Names', 'Roles' , 'Biography' , 'Link Bio Page Detail']
filename = '20.3333.csv'

data = []

list_item = []
processed_urls = set()

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

find_section = soup.find('main', id='main-content')

for linkItem in find_section.find_all('a', class_='usa-link usaid-link', href=True):
    urldetail = 'https://www.usaid.gov' + linkItem['href']
    
    if urldetail not in processed_urls:
        list_item.append((urldetail))  
        processed_urls.add(urldetail)

for bioDetail in list_item:  
    r = requests.get(bioDetail, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    
    name = soup.find('h1', class_='margin-0 desktop:margin-top-1 margin-bottom-1').text.strip()
    roles = soup.find('div', class_='field field--name-field-position-title field--type-string field--label-visually_hidden').text.replace('Position Title','').strip()

    section_bio = soup.find('div', class_='_none font-body-md block block-layout-builder block-field-blocknodepoint-of-contactbody')

    if section_bio:
        biography_paragraphs = section_bio.find_all('p')
        biography = '\n\n'.join([p.text for p in biography_paragraphs]) 

    data_save = {
        'Names' : name,
        'Roles' : roles,
        'Biography' : biography,
        'Link Bio Page Detail' : bioDetail,
    }

    data.append(data_save)
    print('Saving', data_save['Names'])
        # print( )
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)

            

