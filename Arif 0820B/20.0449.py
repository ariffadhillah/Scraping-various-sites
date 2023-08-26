import requests
from bs4 import BeautifulSoup
import csv
import re

url = 'https://www.houstontx.gov/council/'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203'
}

fields = ['Names', 'Titles' , 'Email' , 'Phone' ]
filename = '20.0449.csv'

data = []

list_item = []
processed_urls = set()

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')


find_item = soup.find_all('div', class_='col-md-3')[1:]

for info in find_item:
    title = info.find('h2').text.strip()
    name = info.find_all('p')[0].text.strip()
    phone = info.find_all('p')[1].text.replace('\n','').strip()
    email = info.find('span', class_='email').text.strip()

    data_save = {
        'Names': name,
        'Titles' : title,
        'Email' : email,
        'Phone' : phone.replace(email,'')
    }
    data.append(data_save)
    print('Saving', data_save['Names'])
    print( ' ')
# # # Menulis data ke file CSV setelah selesai looping
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(data)

