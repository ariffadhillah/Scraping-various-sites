import requests
from bs4 import BeautifulSoup
import csv
import re
import time


url = 'https://council.nyc.gov/districts/'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203'
}

fields = ['Names','Borough','Party','Neighborhoods','Email']
filename = '20.0439.csv'

data = []

list_item = []
processed_urls = set()

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

time.sleep(.5)

find_tbody_table = soup.find('tbody', class_='list')
for find_tr in find_tbody_table.find_all('tr'):
    info_tr = find_tr.find_all('td')
    if len(info_tr) >= 7:
        name = info_tr[1].text
        borough = info_tr[3].text
        party = info_tr[4].text
        neighborhoods = info_tr[5].text

        email_element = info_tr[6].find('a', href=True)
        email_href = email_element['href'] if email_element else ""

        data_save = {
            'Names': name,
            'Borough': borough,
            'Party': party,
            'Neighborhoods': neighborhoods,
            'Email': email_href
        }
        data.append(data_save)
        print('Saving', data_save['Names'])
        print( ' ')
# # # Menulis data ke file CSV setelah selesai looping
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(data)
