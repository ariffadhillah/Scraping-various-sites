from requests_html import HTMLSession
import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd

baseurl = 'https://www.sc.com.my/regulation/enforcement/actions'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43'
}

fields = ['Offender(s)', 'Nature of Offence', 'Facts of Case', 'Compound Imposed', 'Name Document', 'Links Document']
filename = 'coba.csv'
# filename = '40.0291.csv'

r = requests.get(baseurl, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

data = []
processed_urls = set()
casesCompounded = soup.find_all('li', class_='st-item')[2]

search_Ul = casesCompounded.find('ul')

urlCase = []
for itemLINK in search_Ul:
    for itemURL in itemLINK.find_all('a', href=True):
        url = itemURL['href']
        if url not in urlCase:
            urlCase.append(url)


for link in urlCase:
    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    titleCase = soup.find('div', {'data-so-type': 'txt;1'}).text.strip()

    table = soup.find('table', class_='tab_format')

    df = pd.read_html(str(table))[0]

    df.columns = ['No.', 'Nature of Offence', 'Offender(s)', 'Facts of Case', 'Compound Imposed']

    df['No.'] = df['No.'].fillna(method='ffill')

    df = df.dropna(subset=['Nature of Offence'])

    df['Offender(s)'] = df['Offender(s)'].fillna(method='ffill')

    df['Facts of Case'] = df['Facts of Case'].fillna(method='ffill')
    df['Compound Imposed'] = df['Compound Imposed'].fillna(method='ffill')

    for _, row in df.iterrows():
        # no =  str(row['No.']).replace('.0', '.')
        natureofOffence = row['Nature of Offence']
        offender_s = row['Offender(s)']
        factsofCase = row['Facts of Case']
        compoundImposed =  row['Compound Imposed']
        print( natureofOffence, offender_s, factsofCase, compoundImposed)
        print ( )
            
        data_40_0291 = {
            'Links Document': link,
            'Name Document': titleCase,
            'Offender(s)': offender_s,
            'Nature of Offence': natureofOffence,
            'Facts of Case': factsofCase,
            'Compound Imposed': compoundImposed
        }

        print('Saving', data_40_0291['Offender(s)'], data_40_0291['Name Document'])
        data.append(data_40_0291)

            # Menulis data ke dalam file CSV
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            writer.writerows(data)

        print(f"Data telah disimpan dalam file {filename}")


