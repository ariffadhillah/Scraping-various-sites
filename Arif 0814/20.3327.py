import requests
from bs4 import BeautifulSoup
import csv
import re

url = 'https://www.sba.gov/about-sba/organization/sba-leadership'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203'
}

fields = ['Names', 'Title' , 'Office']
filename = '20.3327.csv'

data = []

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

find_section = soup.find('div', class_='usa-prose field__item')
find_tables = find_section.find_all('table')

for find_table in find_tables:
    for find_tr in find_table.find_all('tr'):
        td_list = find_tr.find_all('td')
        if len(td_list) >= 3:  
            name = td_list[0].text
            title = td_list[1].text
            office = td_list[2].text

            data_save = {
                'Names': name,
                'Title' : title,
                'Office' : office
            }
            data.append(data_save)
            print('Saving', data_save['Names'])
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fields)
                writer.writeheader()
                writer.writerows(data)