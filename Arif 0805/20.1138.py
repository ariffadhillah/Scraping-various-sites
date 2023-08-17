import requests
from bs4 import BeautifulSoup
import csv
import re

url = 'http://www.bvi.gov.vg/content/governors-groupdeputy-governors-office'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188'
}

data = []

fields = ['Names', 'Roles', 'Department Contact Information' , 'Address Office' , 'Business Office Hours' , 'Telephone Office' , 'Fax Office']
filename = '20.1138.csv'

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

panels = soup.find('div', class_='panels-flexible-region panels-flexible-region-departments_ministry-center panels-flexible-region-last')

info = panels.find('h5', class_='field-content').text

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

img_elements = panels.find_all('img')

for sibling_img_element in img_elements:
    roles = sibling_img_element.find_next('div').find_next('div').get_text(separator='\n', strip=True)
    name = sibling_img_element.find_next('div').find_next('span').get_text(separator='\n', strip=True)

    data_20_1138 = {
        'Names' : name,
        'Roles' : roles,
        'Department Contact Information' : info,
        'Address Office': address.strip(), 
        'Business Office Hours': business_hours.strip(),
        'Telephone Office': tel,
        'Fax Office': fax
    }

    data.append(data_20_1138)
    print('Saving', data_20_1138['Names'])
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        for item in data:
            writer.writerow(item)  