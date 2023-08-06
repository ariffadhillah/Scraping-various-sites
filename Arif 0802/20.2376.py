import requests
from bs4 import BeautifulSoup
import csv

url = 'http://www.epal.co.ao/institucional.php'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188'
}

data = []

fields = ['Names', 'Roles']
filename = '20.2376.csv'

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

find_item = soup.find_all('div', class_='team-content')

for info in find_item:
    names = info.find('h3', class_='title').text.strip()
    # print(names)
    roles = info.find('span', class_='post').text.strip()

    data_20_2376 = {
        'Names' : names,
        'Roles': roles
    }
        
    data.append(data_20_2376)
    print('Saving', data_20_2376['Names'],data_20_2376['Roles'] )
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        for item in data:
            writer.writerow(item)   

