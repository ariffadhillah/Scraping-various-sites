import requests
from bs4 import BeautifulSoup
import csv
import re

url = 'https://www.gw.govt.nz/your-council/council-and-councillors/meet-the-councillors/elected-members-register-of-interests/elected-members-statutory-returns-of-pecuniary-interests/'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62'
}

data = []

fields = ['Names' , 'PII' , 'Link PDF']
filename = '20.0718.csv'

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

find_accordion = soup.find('div', class_='accordion')

filePDF = soup.find('a', class_='btn btn-outline-primary btn-round btn-download')['href']
# print('https://www.gw.govt.nz'+filePDF)

find_list_accordion = find_accordion.find_all('div', class_='accordion-item icon-less')

for info_item in find_list_accordion:
    name = info_item.find('h3').text.replace('expand_more','').strip()
    
    element_text_PII = info_item.find('div', class_='accordion-item__content typography')
    text_p_elements = element_text_PII.find_all('p')
    text_PII_ = "\n".join([p.get_text() for p in text_p_elements if not p.find('a')])
    text_PII = re.sub(r'(\d+)\s+', r'\n\1  ', text_PII_)

    # print(name)
    # print(text_PII)
    # print( )
    # print( )

    data_save = {
        'Names' : name,
        'PII': text_PII.strip(),
        'Link PDF' : 'https://www.gw.govt.nz'+filePDF
    }

    data.append(data_save)
    print('Saving', data_save['Names'])
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)