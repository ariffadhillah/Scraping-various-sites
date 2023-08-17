import requests
from bs4 import BeautifulSoup
import csv
import re

url = 'https://www.judicial.ky/judicial-administration/chief-magistrate'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188'
}

data = []

fields = ['Names', 'Roles', 'PII']
filename = '20.1150.csv'

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')


sections = soup.find('div', class_='post-content')

# <h4 style="font-size: 17px; text-transform: uppercase; letter-spacing: 1.2px;">Hon. Valdis Foldats, LLB</h4>

title = sections.find('h2').text.strip()
name = sections.find('h4').text.strip()
description = sections.find('div', class_='fusion-text fusion-text-1').text.strip()

data_20_1150 = {
    'Names' : name,
    'Roles' : title,
    'PII': description.strip()
}
data.append(data_20_1150)
print('Saving', data_20_1150['Names'],data_20_1150['Roles'])
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    for item in data:
        writer.writerow(item) 

# description = description_div.text if description_div else ""

# titles_and_names_seen = set()

# for section in sections:
#     title_divs = section.find_all('div', {'class': ['fusion-text fusion-text-1']})
#     for title_div in title_divs:
#         current_title = title_div.text.strip()

#         name_anchors = title_div.find_all_next('a', {'data-toggle':'collapse'})
#         for name_anchor in name_anchors:
#             name = name_anchor.text
#             description_div = name_anchor.find_next('div', class_='panel-body toggle-content fusion-clearfix')
#             description = description_div.text if description_div else ""

#             title_name_pair = (current_title, name)
#             if title_name_pair not in titles_and_names_seen:
#                 titles_and_names_seen.add(title_name_pair)


