import requests
from bs4 import BeautifulSoup
import csv
import re
import codecs

url = 'https://www.rree.go.cr/?sec=ministerio&cat=vicecanciller%20multilateral'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.200'
}

data = []

fields = ['Names', 'Roles', 'Titles', 'PII']
filename = '20.2956.csv'

r = requests.get(url, headers=headers, verify=False)
soup = BeautifulSoup(r.content, 'lxml')

find_section = soup.find('article', class_='article animated fadeIn')
title = find_section.find('h1').text.strip()

infoname = find_section.find_all('p')[0]
name = infoname.find('strong').text

inforoles = find_section.find_all('p')[0].text
roles = inforoles.replace(name, '').replace('\n', ' , ').replace(' , Embajador , ', 'Embajador , ').strip()

element_pII = find_section.find_all('p')[1:]


_pII = []

for pII_ in element_pII:
    _pII.append(pII_.text)

pII_text = '\n'.join(_pII)

savedata = {
    'Names' : name,
    'Roles' : roles,
    'Titles' : title,
    'PII' : pII_text
}

data.append(savedata)
print('Saving', savedata['Names'])
with codecs.open(filename, 'w', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(data)
