import requests
from bs4 import BeautifulSoup
import csv
import re

url = 'https://www.stb.gov/about-stb/board-members/'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203'
}

fields = ['Names', 'Titles' , 'Biography']
filename = '20.3329.csv'

data = []

list_item = []
processed_urls = set()

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

title = soup.find('div', class_='omsc-box-inner').text.strip()

print(title)

find_section = soup.find('div', class_='stb-post')


if find_section:
    names = find_section.find_all('h4')
    
    for idx, name in enumerate(names):
        name_ = name.text.strip()
        
        biography_text = ""
        siblings_biography = name.find_next_siblings()
        for sibling_biography in siblings_biography:
            if sibling_biography.name == 'div' and 'omsc-divider' in sibling_biography.get('class', []):
                break
            elif sibling_biography.name == 'p':
                biography_text += sibling_biography.text.strip() + '\n\n' 
                
        # print(biography_text.strip())
        
        data_save = {
            'Names' : name_.replace('Chairman –','').replace('Member –','').strip(),
            'Titles' : name_.replace('– Martin J. Oberman','').replace('– Patrick J. Fuchs','').replace('– Michelle A. Schultz','').replace('– Robert E. Primus','').replace('– Karen J. Hedlund',''), 
            'Biography' : biography_text,
        }

        data.append(data_save)
        print('Saving', data_save['Names'], data_save['Titles'])
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            writer.writerows(data)
