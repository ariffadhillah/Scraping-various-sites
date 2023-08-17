import requests
from bs4 import BeautifulSoup
import csv
import re
import codecs

url = 'https://www.rree.go.cr/?sec=misiones&cat=deCR&cont=525&id=86&pais=AT'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.200'
}

data = []

fields = ['Names', 'Titles', 'Diplomatic Mission Leadership']
filename = '20.2961.csv'


r = requests.get(url, headers=headers, verify=False)
soup = BeautifulSoup(r.content, 'lxml')

pageDetalis = []

find_section = soup.find('article', class_='article animated fadeIn')
diplomaticMissionLeadership = find_section.find('h1').text.strip()
infoboxes = soup.find_all('div', class_='infobox')
for infobox in infoboxes:
    name = infobox.find('span', class_='metaTitle').text.strip()
    title = infobox.find('span', class_='metaQuote').text.strip()

    dataDiplomatic = {
        'Names': name,
        'Titles' : title,
        'Diplomatic Mission Leadership' : diplomaticMissionLeadership
    }

    data.append(dataDiplomatic)
    print('Saving', dataDiplomatic['Names'], dataDiplomatic['Titles'])
    with codecs.open(filename, 'w', encoding='latin-1') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)





