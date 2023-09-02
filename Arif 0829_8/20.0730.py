import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.ecan.govt.nz/about/your-council/our-team/leadership-team/'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62'
}

data = []

fields = ['Names', 'Roles'  , 'Email' , 'PII']
filename = '20.0730.csv'

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

find_section = soup.find('div', id='main')

find_item = find_section.find_all('div', class_='row listpage-item')
# print(find_item)

for info_item in find_item:
    name = info_item.find('h3').text.strip()
    roles = info_item.find('div', class_='listpage-item__subtitle').text.strip()
    
    email_link = info_item.find('a', href=True)
    if email_link and email_link['href'].startswith('mailto:'):
        email_href = email_link['href'].replace('mailto:', '').replace('?subject=Website%20enquiry','')

    element_text_PII = info_item.find('div', class_='listpage-item__text')
    text_p_elements = element_text_PII.find_all('p')

    text_PII = "\n\n".join([p.get_text() for p in text_p_elements if not p.find('a')])

    data_save = {
        'Names' : name,
        'Roles' : roles,
        'Email' : email_href,
        'PII': text_PII,
    }

    data.append(data_save)
    print('Saving', data_save['Names'])
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)