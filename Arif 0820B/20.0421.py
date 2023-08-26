import requests
from bs4 import BeautifulSoup
import csv
import re

url = 'https://evers.wi.gov/Pages/Home.aspx'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.54'
}

fields = ['Names', 'Roles', 'PII']
filename = '20.0421.csv'

data = []

list_item = []
processed_urls = set()

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')


find_section = soup.find('div', id='ctl00_PlaceHolderMain_ctl12__ControlWrapper_RichHtmlField')

name = find_section.find_all('span', class_='ms-rteThemeFontFace-1')[4].text.replace('Governor','').strip()
roles = find_section.find_all('span', class_='ms-rteThemeFontFace-1')[4].text.replace(name,'').strip()

title_pii = find_section.find('h3').text if find_section.find('h3') else ""
text_p_elements = find_section.find_all('p')

text_PII_list = [p.text for p in text_p_elements] if text_p_elements else []
text_PII = '\n'.join(text_PII_list)

# combined_text = f"{title_pii}\n{text_PII}"
# pII_ = combined_text.replace(name,'').replace(roles,'').strip()

data_save = {
    'Names' : name,
    'Roles' : roles,
    'PII' : title_pii + " ,  " + text_PII, 

}

data.append(data_save)
print('Saving', data_save['Names'])
print( ' ')
# # # Menulis data ke file CSV setelah selesai looping
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(data)
