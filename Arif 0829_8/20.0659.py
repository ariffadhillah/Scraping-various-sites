import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.labour.org.nz/party_info'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62'
}

data = []

fields = ['Names', 'Roles', 'Titles']
filename = '20.0659.csv'

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

title = soup.find('h4', class_='h5').text.strip()

find_table = soup.find('table', class_='table table-striped table-responsive mb-4')

for find_tr in find_table.find_all('tr'):
    td_list = find_tr.find_all('td')
    if len(td_list) >= 2:  
        name = td_list[1].text.strip()
        roles = td_list[0].text.strip()

        data_save = {
            'Names' : name,
            'Roles' : roles.replace(':',''),
            'Titles' : title
        }

        data.append(data_save)
        print('Saving', data_save['Names'])
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            writer.writerows(data)
