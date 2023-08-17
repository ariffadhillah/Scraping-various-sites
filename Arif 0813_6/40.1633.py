import requests
from bs4 import BeautifulSoup
import csv
import re
import codecs

url = 'https://ww2.arb.ca.gov/enforcement-2018-case-settlements'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203'
}

data = []

fields = ['Case Settlement Name', 'Date Settled', 'Titles']
filename = '40.1633.csv'

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

title = soup.find('div', class_='section-header section-header--page-title').text.strip()

find_table = soup.find('table', class_='data_table')
find_body = find_table.find('tbody')

for find_tr in find_table.find_all('tr'):
    td_list = find_tr.find_all('td')
    if len(td_list) >= 3:  
        date_settled = td_list[0].text.strip()
        case_settlements = td_list[1].text.strip()

        data_save = {
            'Case Settlement Name': case_settlements,
            'Date Settled' :"'"+date_settled,
            'Titles' : title
        }
        data.append(data_save)
        print('Saving', data_save['Case Settlement Name'])
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            writer.writerows(data)






