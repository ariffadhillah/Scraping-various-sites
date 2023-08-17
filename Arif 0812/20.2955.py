import requests
from bs4 import BeautifulSoup
import csv
import re
import codecs

url = 'https://www.rree.go.cr/?sec=ministerio&cat=vicecanciller%20bilateral'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.200'
}

data = []

fields = ['Names', 'Roles', 'Titles', 'Diplomatic experience' , 'Academic training' , 'Languages']
filename = '20.2955.csv'

r = requests.get(url, headers=headers, verify=False)
soup = BeautifulSoup(r.content, 'lxml')

find_section = soup.find('article', class_='article animated fadeIn')
title = find_section.find('h1').text.strip()

infoname = find_section.find_all('p')[0]
name = infoname.find('strong').text

inforoles = find_section.find_all('p')[0].text
roles = inforoles.replace(name, '').replace('\n', ' , ').replace(' , Embajadora  ,', 'Embajadora , ').strip()


element_Diplomaticexperience = find_section.find_all('p')[1:10]
_Diplomaticexperience = []

for pII_ in element_Diplomaticexperience:
    _Diplomaticexperience.append(pII_.text)

_Diplomaticexperience_text = '\n'.join(_Diplomaticexperience)

element_Academictraining = find_section.find_all('p')[10:14]
_Academictraining = []

for pII_ in element_Academictraining:
    _Academictraining.append(pII_.text)

_Academictraining_text = '\n'.join(_Academictraining)

element_Languages = find_section.find_all('p')[14]
_Languages = []

for pII_ in element_Languages:
    _Languages.append(pII_.text)

_Languages_text = '\n'.join(_Languages)

savedata = {
    'Names' : name,
    'Roles' : roles,
    'Titles' : title,
    'Diplomatic experience' : _Diplomaticexperience_text,
    'Academic training' : _Academictraining_text,
    'Languages' : _Languages_text
}

data.append(savedata)
print('Saving', savedata['Names'])
with codecs.open(filename, 'w', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(data)
