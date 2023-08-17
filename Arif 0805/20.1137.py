import requests
from bs4 import BeautifulSoup
import csv
import re

url = 'http://www.bvi.gov.vg/departments/royal-virgin-islands-police-force-0'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188'
}

data = []

fields = ['Names', 'Roles', 'Department Contact Information' , 'Address' , 'Business Hours' , 'Email Address' , 'Contact Information']
filename = '20.1137.csv'

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

find_section = soup.find('div', class_='panels-flexible-region panels-flexible-region-4-center panels-flexible-region-last')


name = find_section.find('div', class_='panel-pane pane-entity-field pane-node-field-department-head-s-name')
roles = find_section.find('div', class_='field field-name-field-department-head-s-position field-type-text field-label-hidden')

find_address = soup.find_all('div', class_='view-content')[3]
info = find_address.find('h5', class_='field-content').text

address = find_address.find('div', class_='views-field views-field-body').text.strip()
business_hours = find_address.find('div', class_='views-field views-field-field-business-hours').text.strip().replace('Business Hours:','')


emailAddress = soup.find('span', string='Email Address: ')
email_Address = emailAddress.find_next_sibling('span').get_text(strip=True)


contact_form_link = soup.find('a', string='Contact Form')

# Dapatkan teks dari parent elemen 'div' kedua yang berisi paragraf dengan teks yang diinginkan
contact_form = contact_form_link.find_next('div').find_next('p')


data_20_1137 = {
    'Names' : name.text.strip(),
    'Roles' : roles.text.strip(),
    'Department Contact Information' : info.strip(),
    'Address': address.strip(),
    'Business Hours': business_hours.strip(),
    'Email Address': email_Address.strip(),
    'Contact Information': contact_form.text.strip()
}

data.append(data_20_1137)
print('Saving', data_20_1137['Names'])
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    for item in data:
        writer.writerow(item)  