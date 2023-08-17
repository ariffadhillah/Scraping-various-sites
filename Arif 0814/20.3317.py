import requests
from bs4 import BeautifulSoup
import csv
import re

url = 'https://www.archives.gov/about/organization/senior-staff'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203'
}

fields = ['Names', 'Roles', 'Email', 'Titles']
filename = '20.3317.csv'

data = []

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

find_section = soup.find('section', id='block-system-main')
title = find_section.find('h2').text.strip()

find_list_item = find_section.find_all('div', class_='nwidget nlayout ncolumns row make-eq')[:6]
for item in find_list_item:
    p_elements = item.find_all('p')
    for p_element in p_elements:
        info = list(p_element.stripped_strings)

        if len(info) >= 2:
            # print(info)
            # roles = info[0]
            name = info[-2]
            email = info[-1]
            info_combined = '\n'.join(info) 
            
            # # print("Roles:", roles)
            # print("Name:", name)
            # print("Email:", email)
            # print("Info:", info_combined.replace(name,'').replace(email,'').replace('\n', '  ').strip())
            # # print(info_combined)
            # print()

            data_save = {
                'Names' : name,
                'Roles' : info_combined.replace(name,'').replace(email,'').replace('\n', '  ').strip(),
                'Email' : email,
                'Titles' : title
            }
            data.append(data_save)
            print('Saving', data_save['Names'])
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fields)
                writer.writeheader()
                writer.writerows(data)






