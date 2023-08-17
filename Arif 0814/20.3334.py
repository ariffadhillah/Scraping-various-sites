import requests
from bs4 import BeautifulSoup
import csv
import re

url = 'https://ustda.gov/about/'

headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203',
    'Cookie' : 'PHPSESSID=2f07af12926ac38f6d51a12d22ffbb20; _ga=GA1.2.662475344.1692230464; _gid=GA1.2.779185014.1692230464; _ga_6LNSPGT3JV=GS1.2.1692234002.2.1.1692234010.0.0.0' 
}

fields = ['Names', 'Roles' , 'Biography' , 'Link Bio Page Detail']
filename = '20.3334.csv'

data = []

list_item = []
processed_urls = set()

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

find_section = soup.find('div', class_='staff-listings-box')

for linkItem in find_section.find_all('a', class_='wrap-link', href=True):
    roles = linkItem.text
    # print(roles)
    urldetail = linkItem['href']
    
    if urldetail not in processed_urls:
        list_item.append((urldetail, roles))  
        processed_urls.add(urldetail)


for bioDetail , roles in list_item:  
    r = requests.get(bioDetail, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    find_bio = soup.find('div', id='content')
         
    name = find_bio.find('div', class_='section-header').text.strip()

    section_bio = soup.find('main', class_='site-main')

    # print(section_bio)



    if section_bio:
        biography_paragraphs = section_bio.find_all('p')
        biography = '\n\n'.join([p.text for p in biography_paragraphs])
    

    data_save = {
        'Names' : name,
        'Roles' : roles.replace(name,'').replace('\n','').strip(),
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

