import requests
from bs4 import BeautifulSoup
import csv
import re

url = 'https://evers.wi.gov/ltgov/Pages/default.aspx'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.54'
}

fields = ['Names', 'Roles', 'PII']
filename = '20.0422.csv'

data = []

list_item = []
processed_urls = set()

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')


find_section = soup.find('div', id='ctl00_PlaceHolderMain_ctl12__ControlWrapper_RichHtmlField')

img_element = find_section.find('img', alt=True)
if img_element:
    text_name = img_element.find_next('div').text.strip()
    name = text_name.replace('Lt. Gov. ','')
    roles = text_name.replace(name,'').replace('Lt. Gov.','Lt. Gov')


title_pii = find_section.find('h3').text if find_section.find('h3') else ""
element_p = find_section.find('span', class_='ms-rteThemeFontFace-1')
if element_p:
    text_pII = element_p.find_next('div').text.strip()

    # combined_text = f"{title_pii}\n{text_pII}"
    # pII_ = combined_text



data_save = {
    'Names' : name,
    'Roles' : roles,
    'PII' : title_pii + " ,  " + text_pII, 

}

data.append(data_save)
print('Saving', data_save['Names'])
print( ' ')
# # # Menulis data ke file CSV setelah selesai looping
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(data)
