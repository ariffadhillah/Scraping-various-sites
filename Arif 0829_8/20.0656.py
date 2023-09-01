import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.parliament.nz/en/mps-and-electorates/members-financial-interests/mps-financial-interests/2023-register-of-pecuniary-and-other-specified-interests-of-members-of-parliament-and-amendments/'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62'
}

data = []

fields = [ 'Names' , 'Originally published' , 'Last updated' , 'PII' , 'Link PDF']
filename = '20.0656.csv'

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')


find_section = soup.find('div', class_='section--border-bottom-desktop')

filePDF = find_section.find('a', class_='related-links__link theme__link')
# print(urlPDF['href'])

originally_published_strong = soup.find('strong', string='Originally published:')
if originally_published_strong:
    originally_published_text = originally_published_strong.next_sibling.strip()
    
last_updated_strong = soup.find('strong', string='Last updated:')
if last_updated_strong:
    last_updated_text = last_updated_strong.next_sibling.strip()

text_PII = soup.find('div', class_='lede').text.strip()

data_save = {
    'Names' : filePDF.text.replace('(pdf 1.1MB)','').strip(),
    'Originally published' :"'"+originally_published_text,
    'Last updated' : "'"+last_updated_text,
    'PII': text_PII,
    'Link PDF' : 'https://www.parliament.nz' + filePDF['href']
}

data.append(data_save)
print('Saving', data_save['Names'])
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(data)

