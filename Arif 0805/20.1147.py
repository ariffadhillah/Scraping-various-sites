import requests
from bs4 import BeautifulSoup
import csv
import re

url = 'https://www.judicial.ky/judicial-administration/president-court-of-appeal'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188'
}

data = []

fields = ['Names','Roles' , 'Titles', 'PII']
filename = '20.1147.csv'

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

find_section = soup.find('div', class_='post-content')
names = find_section.find_all('a')
title_ = find_section.find_all('div', {'class': ['fusion-text fusion-text-1', 'fusion-text fusion-text-3']})
discription_ = find_section.find_all('div', {'class': ['fusion-text fusion-text-2', 'fusion-text fusion-text-4']})

for i in range(len(names)):
    name = names[i].text.strip()
    
    if i < len(title_):
        title = title_[i].text.strip()
    else:
        title = ""
    
    if i < len(discription_):
        description = discription_[i].text.strip()
    else:
        description = ""
    
    data_20_1147 = {
        'Names' : name,
        'Roles' : 'President of the Court of Appeal of the Cayman Islands',
        'Titles' : title,
        'PII': description
    }

    data.append(data_20_1147)
    print('Saving', data_20_1147['Names'])
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        for item in data:
            writer.writerow(item) 

