import requests
from bs4 import BeautifulSoup
import csv

baseurl = 'http://www.fsmlaw.org/fsm/decisions/index.htm'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43'
}

r = requests.get(baseurl, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

data = []

tabel = soup.find('table')
listItems = tabel.find_all('li')
for item in listItems:
    a_tag = item.find('a')
    if a_tag:
        href = a_tag.get('href')
        title = a_tag.text.strip().replace('\n', '').replace('New', 'New ').replace('New', 'New ')
        url = 'http://fsmlaw.org/fsm/decisions/' + href

        data_50_042 = {
            'Title': title.replace('\t', ' ').replace('.', '.').replace('             ',''),
            'Link Page': url.replace('http://fsmlaw.org/fsm/decisions/http://www.fsmlaw.org/fsm/decisions/', 'http://fsmlaw.org/fsm/decisions/').replace('http://fsmlaw.org/fsm/decisions/http://fsmlaw.org/fsm/decisions/','http://fsmlaw.org/fsm/decisions/')
        }
        data.append(data_50_042)
        print('Saving', data_50_042['Title'], data_50_042['Link Page'])

# Write the data to a CSV file
fields = ['Title', 'Link Page']
filename = '50.042.csv'

with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(data)
