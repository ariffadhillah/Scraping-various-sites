import requests
from bs4 import BeautifulSoup
import csv
import re

url = 'https://statetreasurer.wi.gov/Pages/About/Treasurer.aspx'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.54'
}

fields = ['Names', 'Roles', 'PII']
filename = '20.0425.csv'

data = []

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')


find_section = soup.find('div', class_='container pl-2')
names = find_section.find('h1').text.replace('State Treasurer ','').strip()
name = names
roles = find_section.find('h1').text.replace(name,'').strip()

text_PII = find_section.find('div', id='ctl00_PlaceHolderMain_ctl02__ControlWrapper_RichHtmlField').text.strip()

data_save = {
    'Names' : name,
    'Roles' : roles,
    'PII' : text_PII, 

}

data.append(data_save)
print('Saving', data_save['Names'])
print( ' ')
# # # Menulis data ke file CSV setelah selesai looping
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(data)

