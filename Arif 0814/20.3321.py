import requests
from bs4 import BeautifulSoup
import csv
import re

url = 'https://www.ntsb.gov/about/board/Pages/default.aspx'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203'
}

fields = ['Names','Roles','Biography']
filename = '20.3321.csv'

data = []

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

listbio = []
processed_urls = set()

find_section = soup.find_all('section', class_='col-6 gray-bkg gray-callout')

for seeBiography in find_section:
    biography =  seeBiography.find('a', href=True)
    urlbio = 'https://www.ntsb.gov' + biography['href']
    if url not in processed_urls:
        listbio.append(urlbio)
        processed_urls.add(urlbio)

for detailsbio in listbio:
    r = requests.get(detailsbio, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    name = soup.find('span', class_='faux-title header-three').text.strip()
    roles = soup.find('span', class_='title').text.strip()

    elementbiography = soup.find('div', id='board_member_biography').text

    biographytext = elementbiography.replace('\n', '\n\n').replace('Biography','').strip()

    data_save = {
        'Names' : name,
        'Roles' : roles,
        'Biography' :biographytext
    }
    data.append(data_save)
    print('Saving', data_save['Names'])
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)