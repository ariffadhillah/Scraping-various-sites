import requests
from bs4 import BeautifulSoup
import csv
import re

url = 'https://www.wicourts.gov/courts/supreme/justices/index.htm'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203'
}

fields = ['Names', 'Roles', 'PII']
filename = '20.0426.csv'

data = []

list_item = []
processed_urls = set()

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

find_element_p = soup.find_all('p', class_='team-title-heading')

for listpageDetails in find_element_p:
    bio_detail = listpageDetails.find('a', href=True)
    url_bio = 'https://www.wicourts.gov/courts/supreme/justices/' + bio_detail['href']
    if url_bio not in processed_urls:
        list_item.append(url_bio)
        processed_urls.add(url_bio)

for detail_bio_url in list_item:
    r = requests.get(detail_bio_url, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    print(detail_bio_url)

    find_section = soup.find('section', id='content')


    names = find_section.find('h2').text.replace('Chief','').replace('Justice','').strip()
    name = names

    roles = find_section.find('h2').text.replace(name,'')
    text_PII = find_section.find('div', class_='side_nav_content').text.replace('Back to justices','').strip()

    data_save = {
        'Names' : name,
        'Roles' : roles,
        'PII' : text_PII, 

    }

    data.append(data_save)
    print('Saving', data_save['Names'])
    print( ' ')
    # # # Menulis data ke file CSV setelah selesai looping
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)
