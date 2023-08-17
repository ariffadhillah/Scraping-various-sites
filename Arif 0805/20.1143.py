import requests
from bs4 import BeautifulSoup
import csv
import re

url = 'http://www.bvi.gov.vg/content/ministry-education-and-culture'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188'
}

data = []
fields = ['Names' , 'Roles' , 'Office Telephone' , 'Office Email' , 'Office Address' , 'Business Hours']

filename = '20.1143.csv'

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

panels = soup.find('div', class_='panels-flexible-region panels-flexible-region-departments_ministry-center panels-flexible-region-last')

info = panels.find('h3', class_='panel-title').text

address = panels.find('div', class_='views-field views-field-body').text.strip()
business_hours = panels.find('div', class_='views-field views-field-field-business-hours').text.strip().replace('Business Hours:','')

if panels:
    text = panels.get_text()
    tel_match = re.search(r'Telephone:\s*(.+)', text)
    email_match = re.search(r'Email:\s*(.+)', text)
    fax_match = re.search(r'Fax:\s*(.+)', text)

    if tel_match:
        tel = tel_match.group(1)
    if email_match:
        email = email_match.group(1)
    if fax_match:
        fax = email_match.group(1)

name1 = panels.find_all('div', class_='field-item even')[1].text.strip()
name2_elements = panels.find_all('strong')

names_list = [name1]
for name2_element in name2_elements:
    name2 = name2_element.get_text(strip=True)
    names_list.append(name2)
# print(names_list)

roles_list = []

selectors = [
    '#block-system-main > div > div > div > div.panels-flexible-row.panels-flexible-row-departments_ministry-main-row.clearfix > div > div.panels-flexible-region.panels-flexible-region-departments_ministry-center.panels-flexible-region-last > div > div.field.field-name-field-head-s-title.field-type-text.field-label-hidden > div > div',
    '#block-system-main > div > div > div > div.panels-flexible-row.panels-flexible-row-departments_ministry-main-row.clearfix > div > div.panels-flexible-region.panels-flexible-region-departments_ministry-center.panels-flexible-region-last > div > div:nth-child(9) > div > div > div > div:nth-child(2) > div',
    '#block-system-main > div > div > div > div.panels-flexible-row.panels-flexible-row-departments_ministry-main-row.clearfix > div > div.panels-flexible-region.panels-flexible-region-departments_ministry-center.panels-flexible-region-last > div > div.panel-pane.pane-entity-field.pane-node-field-permanent-secretaries-and > div > div > div > div > p:nth-child(1)',
    '#block-system-main > div > div > div > div.panels-flexible-row.panels-flexible-row-departments_ministry-main-row.clearfix > div > div.panels-flexible-region.panels-flexible-region-departments_ministry-center.panels-flexible-region-last > div > div.panel-pane.pane-entity-field.pane-node-field-permanent-secretaries-and > div > div > div > div > p:nth-child(2)'
]



for idx, (selector, name) in enumerate(zip(selectors, names_list)):
    role_element = soup.select_one(selector)
    if role_element:
        role = role_element.get_text().strip().replace('Deputy Secretary (Ag.)Claude Kettle', '').replace('Ms. Haley Trott (Ag.)','').replace('Margaret Jones-Greene','')

        print(name, role)

        data_20_1143 = {
            'Names' : name,
            'Roles' : role.replace('\n',''),
            'Office Telephone' : tel,
            'Office Email' : email,
            'Office Address' : address,
            'Business Hours' : business_hours
        }
        data.append(data_20_1143)
        print('Saving', data_20_1143['Names'])

    else:
        print(f"Role tidak ditemukan untuk {name}")

with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(data)






