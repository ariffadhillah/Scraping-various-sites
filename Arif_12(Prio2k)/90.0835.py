import requests
from bs4 import BeautifulSoup
import csv
import time

url = 'https://www.lafv.li/DE/AndUuml;beruns/Mitglieder/Passiv-Mitglieder'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69'
}

data = []

fields = ['Names' , 'Company Name' , 'Telephone' , 'Website']
filename = '90.0835.csv'

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

find_table = soup.find('table', class_='contentTable')
find_tbody = find_table.find('tbody')

time.sleep(1)
for find_tr in find_tbody.find_all('tr')[1:]:
    find_td = find_tr.find_all('td')
    if find_td:
        companyName = find_td[0].text
        telephone = find_td[1].text
        website = find_td[2].text
        name = find_td[3].text

        data_save = {
            'Names' : name,
            'Company Name' : companyName,
            'Telephone' : telephone,
            'Website' : website
        }
        data.append(data_save)
        print('Saving', data_save['Names'])
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            writer.writerows(data)
