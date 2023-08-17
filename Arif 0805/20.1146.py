import requests
from bs4 import BeautifulSoup
import csv
import re

url = 'https://www.judicial.ky/judicial-administration/chief-justice'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188'
}

data = []

fields = ['Names', 'Roles', 'PII']
filename = '20.1146.csv'

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

find_section = soup.find('div', class_='post-866 page type-page status-publish hentry')
h3_elements_name = soup.find_all('h3', class_='p1')

for name_ in h3_elements_name:
    name = name_.text.strip()
#     # description
# print(name)
roleS = find_section.find_all('h2', class_='fusion-title-heading title-heading-left fusion-responsive-typography-calculated')
# roles2 = find_section.find_all('h4', class_='panel-title toggle')
for roles_ in roleS:
    roles = roles_.text.strip()

# print(roles)


discription_ = find_section.find_all('div', {'class':'fusion-text fusion-text-2'})

for desc_element in discription_:
    description = desc_element.text.strip()
    # description



data_20_1146 = {
    'Names' : name,
    'Roles' : roles,
    'PII': description
}

data.append(data_20_1146)
print('Saving', data_20_1146['Names'])
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    for item in data:
        writer.writerow(item) 



