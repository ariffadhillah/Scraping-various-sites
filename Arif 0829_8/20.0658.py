import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.parliament.nz/en/mps-and-electorates/members-of-parliament/'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62'
}

data = []

fields = ['Names' , 'Party' , 'Electorate' , 'Title']
filename = '20.0658.csv'

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

title = soup.find('a', class_='tab__menu-link js-tab__link').text.strip()

find_table = soup.find('table', class_='table--list')

for find_tr in find_table.find_all('tr'):
    td_list = find_tr.find_all('td')
    if len(td_list) >= 4:  
        name = td_list[1].text.strip()
        party = td_list[2].text.strip()
        electorate = td_list[3].text.strip()

        data_save = {
            'Names' : name,
            'Party' : party,
            'Electorate' : electorate,
            'Title' : title
        }

        data.append(data_save)
        print('Saving', data_save['Names'])
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            writer.writerows(data)
