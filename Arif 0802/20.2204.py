import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.ec.or.ug/party/alliance-national-transformation-ant'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188'
}

data = []

fields = ['Names', 'Address' , 'Political Name', 'Date of Registration']
filename = '20.2204.csv'

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

find_article = soup.find('section', id='post-content')

political_name_element = find_article.find('div', string='Political Name:\xa0')

if political_name_element:
    political_name = political_name_element.find_next_sibling('div').text.strip()
    
else:
    political_name = ''


name_element = find_article.find('div', string='The Representative to National Consultative Forum (NCF):\xa0')

if name_element:
    name = name_element.find_next_sibling('div').text.strip()    
else:
    name = ''

address_element = find_article.find('div', string='Address:\xa0')
if address_element:
    address = address_element.find_next_sibling('div').text.strip()    
else:
    address = ''

date_of_Registration_element = find_article.find('div', string='Date of Registration:\xa0')
if date_of_Registration_element:
    date_of_Registration = date_of_Registration_element.find_next_sibling('div').text.strip()    
else:
    date_of_Registration = ''


data_20_2204 = {
    'Names' : name,
    'Address' : address,
    'Political Name' : political_name,
    'Date of Registration' : date_of_Registration
}

data.append(data_20_2204)
print('Saving', data_20_2204['Names'])
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    for item in data:
        writer.writerow(item)   



