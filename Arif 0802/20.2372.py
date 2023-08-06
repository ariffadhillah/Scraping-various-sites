import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.bodiva.ao/governacao-corporativa'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188'
}

data = []

fields = ['Names', 'Roles', 'Biography']
filename = '20.2372.csv'

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

find_modal = soup.find_all('div', class_='modal-body')
for info in find_modal:
    name = info.find('h5').text
    roles = info.find('li').text

    biography = info.find('div', class_='btn-group_2').text.strip()    

    data_20_2372 = {
        'Names' : name,
        'Roles': roles,
        'Biography' : biography

    }
        
    data.append(data_20_2372)
    print('Saving', data_20_2372['Names'],data_20_2372['Roles'] )
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        for item in data:
            writer.writerow(item)   



    