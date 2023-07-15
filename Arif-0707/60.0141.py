import requests
from bs4 import BeautifulSoup
import json
import re
import csv

baseurl = 'https://www.asfi.gob.bo/index.php/inf-interes-dcf/entidades-en-proceso-de-adecuacion'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67'
}

fields = ['Title', 'Category', 'Publication Date', 'URL PDF']
filename = '60.0141.csv'

data = []

r = requests.get(baseurl, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

searchArticel = soup.find('div', {'itemprop':'articleBody'})
category = searchArticel.find_all('p')[4]
date_ = searchArticel.find_all('p')[5]

table = searchArticel.find_all('table')[1]

links = table.find_all('a')
for link in links:
    urlPdf = 'https://www.asfi.gob.bo'+link['href']
    name = link.text

    data_60_0141 = {
        'Title': name,
        'Category': category.text,
        'Publication Date': date_.text,
        'URL PDF' : urlPdf
    }
    data.append(data_60_0141)
    print('Saving', data_60_0141['Title'])
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)

print(f"Save data to file {filename}")