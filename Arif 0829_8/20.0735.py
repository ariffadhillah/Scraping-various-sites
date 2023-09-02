import requests
from bs4 import BeautifulSoup
import csv
import re

url = 'https://www.aucklandcouncil.govt.nz/about-auckland-council/how-auckland-council-works/governing-body-wards-committees/wards/Pages/ward-councillors.aspx'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62'
}

data = []

fields = ['Names','Phone','Email','Roles','Titles']
filename = '20.0735.csv'

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

find_section = soup.find_all('div', class_='s4-wpcell-plain ms-webpartzone-cell ms-webpart-cell-vertical ms-fullWidth')

for info_item in find_section:
    titles = info_item.find_all('h2')
    if titles:
        last_title = titles[-1]
        title_text = last_title.get_text(strip=True)
        
        title = title_text.strip()

    roles_list = info_item.find_all('h3')
    for roles_ in roles_list:
        roles = roles_.get_text(strip=True)
        # print(roles)
        
    info_desc = info_item.find_all('div', class_='info')

    for info_person in info_desc:
        name = info_person.find('h4').text.strip()
        phone = info_person.find_all('p')[0].text.replace('Telephone number','').strip()
        email = info_person.find_all('p')[1].text.replace('Email address','').strip()

        # print(name, roles, title)

        data_save = {
            'Names' : name,
            'Phone' : phone,
            'Email' : email,
            'Roles' : roles,
            'Titles' : title
        }
        data.append(data_save)
        print('Saving', data_save['Names'])
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            writer.writerows(data)



