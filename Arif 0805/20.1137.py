import requests
from bs4 import BeautifulSoup
import csv
import re

url = 'http://www.bvi.gov.vg/departments/royal-virgin-islands-police-force-0'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188'
}

data = []

fields = ['Names', 'Address' , 'Political Name']
filename = '20.2203.csv'

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

find_section = soup.find('div', class_='panels-flexible-region panels-flexible-region-4-center panels-flexible-region-last')
# print(find_section)
name = find_section.find('div', class_='panel-pane pane-entity-field pane-node-field-department-head-s-name')
print(name.text.strip())

roles = find_section.find('div', class_='field field-name-field-department-head-s-position field-type-text field-label-hidden')
print(roles.text.strip())

find_address = soup.find_all('div', class_='view-content')[3]
info = find_address.find('h5', class_='field-content').text
address = find_address.find('div', class_='views-field views-field-body').text.strip()
business_hours = find_address.find('div', class_='views-field views-field-field-business-hours').text.strip().replace('Business Hours:','')


emailAddress = soup.find('span', string='Email Address: ')
email_Address = emailAddress.find_next_sibling('span').get_text(strip=True)


contact_form_link = soup.find('a', string='Contact Form')

# Dapatkan teks dari parent elemen 'div' kedua yang berisi paragraf dengan teks yang diinginkan
result_text = contact_form_link.find_next('div').find_next('p')

print(result_text.text)

