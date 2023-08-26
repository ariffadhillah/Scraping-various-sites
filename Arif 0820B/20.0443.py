import requests
from bs4 import BeautifulSoup
import csv
import re

url = 'https://chicagocitytreasurer.com/'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.54'
}

fields = ['Names', 'Roles', 'PII']
filename = '20.0443.csv'

data = []

processed_urls = set()

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

name = soup.find_all('h2', class_='elementor-heading-title elementor-size-default')[2].text.strip()
roles = soup.find_all('h2', class_='elementor-heading-title elementor-size-default')[3].text.strip()

element_PII = soup.find('div', class_='elementor-element elementor-element-64fbc54 elementor-widget elementor-widget-text-editor')

data_save = {
    'Names' : name,
    'Roles' : roles,
    'PII' : element_PII.text.strip()
}

data.append(data_save)
print('Saving', data_save['Names'])
print( ' ')
# # # Menulis data ke file CSV setelah selesai looping
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(data)


