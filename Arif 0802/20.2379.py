import requests
from bs4 import BeautifulSoup
import csv

url = 'https://tribunalconstitucional.ao/pt/juizes/juizes-conselheiros-jubilados/'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188'
}

data = set()

data_save =[]

fields = ['Names', 'Roles']
filename = '20.2379.csv'

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

section_ = soup.find('section', class_='normal-section1')

h4_list = section_.find_all('h4')
for h4_title in h4_list:
    span_title = h4_title.find('span')
    if span_title:
        title = span_title.text.strip()
    else:
        name = h4_title.text.strip()
        data.add((name, title))

profile_info = soup.find_all('div', class_='profile-info')

for info in profile_info:
    h3_name = info.find('h3').text.strip()
    span_title_ = info.find('span').text.strip() if info.find('span') else ''
    data.add((h3_name, span_title_))

for name, title in data:
    data_90_2379 = { 
        'Names' : name,
        'Roles': title 
    }

    data_save.append(data_90_2379)

    print('Saving', data_90_2379['Names'],data_90_2379['Roles'] )
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    for item in data_save:
        writer.writerow(item) 

