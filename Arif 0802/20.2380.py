import requests
from bs4 import BeautifulSoup
import csv

url = 'https://faa.ao/fan/comandante_fan'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188'
}

data = []

fields = ['Names', 'Cargo', 'Patente' , 'Naturalidade' , 'Data de nascimento' , 'Data de incorporação nas ex-FAPLA']
filename = '20.2380.csv'

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

find_profil = soup.find('div', class_='team-box')


patente = find_profil.find_all('h6')[0]
# print(patente.text.strip())

cargo = find_profil.find_all('h6')[2]
# print(cargo.text.strip())

name = find_profil.find_all('h6')[4]
# print(name.text.strip())

naturalidade = find_profil.find_all('h6')[6]
# print(naturalidade.text.strip())

data_de_nascimento = find_profil.find_all('h6')[8]
# print(data_de_nascimento.text.strip())

fapla = find_profil.find_all('h6')[10]
# print(fapla.text.strip())

data_20_2380 = {
    'Names' : name.text.strip().replace('Nome:','').replace(';',''),
    'Cargo' : cargo.text.strip().replace('Cargo:', ''),
    'Patente' : patente.text.strip().replace('Patente:', ''),
    'Naturalidade' : naturalidade.text.strip().replace('Naturalidade:',''),
    'Data de nascimento' : data_de_nascimento.text.strip().replace('Data de nascimento:',''),
    'Data de incorporação nas ex-FAPLA' : fapla.text.strip().replace('Data de incorporação nas ex-FAPLA:','')
}

data.append(data_20_2380)
print('Saving', data_20_2380['Names'])
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    for item in data:
        writer.writerow(item)  