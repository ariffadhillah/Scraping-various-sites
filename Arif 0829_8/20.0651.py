import requests
from bs4 import BeautifulSoup
import csv

url = 'https://alp.org.au/about/national-executive/'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62'
}

data = []

fields = ['Names', 'Titles']
filename = '20.0651.csv'

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

find_section = soup.find('div', class_='col-md-8 col-xs-12 main rich-text-wrapper')

title = find_section.find('h3').text

find_ul = find_section.find('ul')

for find_li in find_ul.find_all('li'):
    name = find_li.text.strip()

    data_save = {
        'Names' : name,
        'Titles' : title
    }
    data.append(data_save)
    print('Saving', data_save['Names'])
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)

