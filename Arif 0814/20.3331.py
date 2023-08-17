import requests
from bs4 import BeautifulSoup
import csv
import re

url = 'https://about.usps.com/who/leadership/pmg-exec-leadership-team.htm'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203'
}

fields = ['Names', 'Roles' , 'Biography' , 'Link Bio Page Detail']
filename = '20.3331.csv'

data = []

list_item = []
processed_urls = set()

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

find_section = soup.find('main', id='contentstart')
find_ul = find_section.find_all('ul', class_='list-unstyled memberlist')

for find_li in find_ul:
    seacrh_li = find_li.find_all('li')
    for li in seacrh_li:
        linkItem = li.find('a', href=True)
        if linkItem:
            # link_href = linkItem['href']
            urldetail = 'https://about.usps.com' + linkItem['href']

            if urldetail not in processed_urls:
                list_item.append((urldetail))  
                processed_urls.add(urldetail)


for bioDetail in list_item:  
    r = requests.get(bioDetail, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    section_bio = soup.find('div', class_='col-12 col-md-8 col-xxl-9 bodycontent')

    if section_bio:
        name = section_bio.find('h1').text.strip()
        roles = section_bio.find('p', class_='lead').text.strip()
        biography_paragraphs = section_bio.find_all('p')[1:]
        biography = '\n\n'.join([p.text for p in biography_paragraphs]) 

        data_save = {
            'Names' : name,
            'Roles' : roles,
            'Biography' : biography,
            'Link Bio Page Detail' : bioDetail,
        }

        data.append(data_save)
        print('Saving', data_save['Names'] , data_save['Roles'] , data_save['Link Bio Page Detail'])
        # print( )
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            writer.writerows(data)

            

