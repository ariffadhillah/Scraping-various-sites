import requests
from bs4 import BeautifulSoup
import csv

url = 'https://mirempet.gov.ao/ao/ministerios/ministerio-dos-recursos-minerais-petroleo-e-gas/'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188'
}

data = []

fields = ['Names', 'Roles']
filename = '20.2370.csv'

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

find_table = soup.find_all('div', class_='bg-white pb-4 mb-3')[3]

tbody_elements = find_table.find_all('tbody')

for tbody in tbody_elements:
    tr_elements = tbody.find_all('tr')

    for tr in tr_elements:
        td_elements = tr.find_all('td')

        # Pastikan ada setidaknya dua elemen td sebelum mengambil nilai teks dari elemen pertama dan kedua
        if len(td_elements) >= 2:
            roles = td_elements[0].text.strip()
            name = td_elements[1].text.strip()

            data_20_2370 = {
            'Names' : name,
            'Roles' : roles
            }

            data.append(data_20_2370)
            print('Saving', data_20_2370['Names'])
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fields)
                writer.writeheader()
                for item in data:
                    writer.writerow(item)   