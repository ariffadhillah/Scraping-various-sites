import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.parliament.nz/en/mps-and-electorates/members-financial-interests/mps-financial-interests/2014-additional-information/'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62'
}

data = []

fields = ['Names' , 'Roles' , 'Titles' , 'Originally published' , 'Last updated' , 'PII' , 'Description']
filename = '20.0657.csv'

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

title =  soup.find('h1').text.strip()

find_body = soup.find('div', class_='body-text section--border-bottom-mobile push--top-mobile')
paragraphs = find_body.find_all('p')[:2]

desc = ' '.join([p.get_text() for p in paragraphs])

originally_published_strong = soup.find('strong', string='Originally published:')
if originally_published_strong:
    originally_published_text = originally_published_strong.next_sibling.strip()
    
last_updated_strong = soup.find('strong', string='Last updated:')
if last_updated_strong:
    last_updated_text = last_updated_strong.next_sibling.strip()

find_section = soup.find_all('div', class_='section')
for info in find_section:
    name = info.find('h4').text.strip()
    roles = info.find_all('tr')[0].text.strip()
    text_PII = info.find_all('tr')[1].text.strip()

    data_save = {
        'Names' : name,
        'Roles' : roles.replace('10','').replace('7','').strip(),
        'Titles' : title,
        'Originally published' : "'"+originally_published_text,
        'Last updated' : "'"+last_updated_text,
        'PII' : text_PII,
        'Description' : desc
    }

    data.append(data_save)
    print('Saving', data_save['Names'])
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)
