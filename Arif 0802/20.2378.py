import requests
from bs4 import BeautifulSoup
import csv

url = 'https://tribunalconstitucional.ao/pt/juizes/composicao-e-designacao/'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188'
}

data = []

fields = ['Names', 'Roles']
filename = '20.2378.csv'

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

find_modal_body = soup.find_all('div', class_='modal-body')

for info in find_modal_body:
    name = info.find('h6').text.strip()
    title = info.find('span').text.strip()

    data_20_2378 = {
        'Names' : name,
        'Roles': title
    }
        
    data.append(data_20_2378)
    print('Saving', data_20_2378['Names'],data_20_2378['Roles'] )
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        for item in data:
            writer.writerow(item)   

    


    


