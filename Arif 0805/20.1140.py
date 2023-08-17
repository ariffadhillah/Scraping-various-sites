import requests
from bs4 import BeautifulSoup
import csv
import re

url = 'http://www.bvi.gov.vg/ministry/ministry-of-finance'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188'
}

data = []

fields = ['Names', 'Roles', 'Department Contact Information' , 'Address Office' , 'Business Office Hours' , 'Telephone Office', 'Fax Office']
filename = '20.1140.csv'

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

panels = soup.find('div', class_='panels-flexible-region panels-flexible-region-departments_ministry-center panels-flexible-region-last')

info = panels.find('h3', class_='panel-title').text

address = panels.find('div', class_='views-field views-field-body').text.strip()
business_hours = panels.find('div', class_='views-field views-field-field-business-hours').text.strip().replace('Business Hours:','')

if panels:
    text = panels.get_text()
    tel_match = re.search(r'Telephone:\s*(.+)', text)
    fax_match = re.search(r'Fax:\s*(.+)', text)

    if tel_match:
        tel = tel_match.group(1)
    if fax_match:
        fax = fax_match.group(1)

name1 = panels.find_all('div', class_='field-item even')[1].text.strip()

name2_elements = panels.find_all('strong', class_='govps')
name2 = ' - '.join(name2_element.get_text(strip=True) for name2_element in name2_elements)

name = f"{name1}\n{name2}"

roles1 = panels.find_all('div', class_='field-item even')[0].text.strip()

roles2 = panels.find('div', class_='govps').text.strip()

roles = f"{roles1}\n{roles2}"

# Memisahkan setiap baris name dan roles dan mencetak satu per satu
names_list = name.split('\n')
roles_list = roles.split('\n')

for i in range(len(names_list)):
    name_ = names_list[i]
    roles_ = roles_list[i]

    data_20_1140 = {
        'Names' : name_,
        'Roles' : roles_,
        'Department Contact Information' : info.strip(),
        'Address Office': address.strip(), 
        'Business Office Hours': business_hours.strip(),
        'Telephone Office': tel,
        'Fax Office': fax
    }

    data.append(data_20_1140)
    print('Saving', data_20_1140['Names'])
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        for item in data:
            writer.writerow(item)  