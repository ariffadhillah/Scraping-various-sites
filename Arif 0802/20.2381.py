import requests
from bs4 import BeautifulSoup
import csv
import re

url = 'https://faa.ao/exe/perfil-exe'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188'
}

data = []

fields = ['Names', 'Cargo', 'Patente' , 'Naturalidade' , 'Data de nascimento' , 'FAPLA']
filename = '20.2381.csv'

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

# data_de_nascimento = find_profil.find_all('h6')[8]
# print(data_de_nascimento.text.strip())

data_de_Nascimento = re.compile(r'Data de Nascimento:\s*')
data_de_Nascimentolabel = soup.find('span', string=data_de_Nascimento)

# Dapatkan sibling berikutnya, yang berisi nilai dari "Patente"
if data_de_Nascimentolabel:
    data_de_nascimento = data_de_Nascimentolabel.find_next_sibling('span').text.strip()    
else:
    data_de_nascimento = ''

fapla = find_profil.find_all('h6')[9]
# print(fapla.text.strip())

data_20_2381 = {
    'Names' : name.text.strip().replace('Nome:','').replace(';',''),
    'Cargo' : cargo.text.strip().replace('Cargo:', '').replace(';',''),
    'Patente' : patente.text.strip().replace('Patente:', '').replace(';',''),
    'Naturalidade' : naturalidade.text.strip().replace('Naturalidade:','').replace(';',''),
    'Data de nascimento' : data_de_nascimento.replace(';',''),
    'FAPLA' : fapla.text.strip()
}

data.append(data_20_2381)
print('Saving', data_20_2381['Names'])
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    for item in data:
        writer.writerow(item)  