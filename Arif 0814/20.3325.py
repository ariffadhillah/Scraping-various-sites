import requests
from bs4 import BeautifulSoup
import csv
import re

url = 'https://www.sec.gov/about/commissioners'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203'
}

fields = ['Names', 'Roles', 'Since' ,'Term Exp' ]
filename = '20.3325.csv'

data = []

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

find_card = soup.find_all('div', {'class':['small colspan-3','small colspan-3','small-4 colspan-3','small-4 colspan-3','small-4 colspan-3 last']})

for p_element in find_card:
    info = list(p_element.stripped_strings)

    if len(info) >= 3:
        # print(info)
        term_exp = info[-1]
        since = info[-2]
        roles = info[-3]
        info_name = '\n'.join(info) 

        data_save = {
            'Roles' : roles,
            'Term Exp' : term_exp.replace('Term exp.',''),
            'Since' : since.replace('since',''),
            'Names' : info_name.replace(roles,'').replace(term_exp,'').replace(since,'').replace('\n',' ').strip(),
        }
        data.append(data_save)
        print('Saving', data_save['Names'])
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            writer.writerows(data)
