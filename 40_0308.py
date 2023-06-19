from requests_html import HTMLSession
import csv
import requests
from bs4 import BeautifulSoup

baseurl = 'https://www.sc.com.my/regulation/enforcement/actions'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43'
}

fields = ['Name', 'Nature of Offence', 'Facts of Case', 'Compound Imposed', 'Name Document', 'Links Document']
filename = '40.0308.csv'

r = requests.get(baseurl, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

data = []
processed_urls = set()
casesCompounded = soup.find_all('li', class_='st-item')[3]

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

    s = HTMLSession()
    r = s.get(link)

    table = r.html.find('table')[0]
    tabledata = []

    rows = table.find('tr')

    for row in rows[1:]:
        cells = row.find('td')

        # Membaca hanya baris dengan tepat 5 sel
        if len(cells) != 5:
            continue

        dataCels = {
            'No.': cells[0].text,
            'Nature of Offence': cells[1].text,
            'Offender(s)': cells[2].text,
            'Facts of Case': cells[3].text if len(cells) > 3 else '',
            'Compound Imposed': cells[4].text if len(cells) > 4 else '',
        }

        tabledata.append(dataCels)

    for dataItem in tabledata:
        offender_s = dataItem['Offender(s)']
        NatureofOffence = dataItem['Nature of Offence']
        factsofCase = dataItem['Facts of Case']
        compoundImposed = dataItem['Compound Imposed']

        data_40_0308 = {
            'Links Document': link,
            'Name Document': titleCase,
            'Name': offender_s,
            'Nature of Offence': NatureofOffence,
            'Facts of Case': factsofCase,
            'Compound Imposed': compoundImposed
        }

        print('Saving', data_40_0308['Name'], data_40_0308['Name Document'])
        data.append(data_40_0308)

        # Menulis data ke dalam file CSV
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            writer.writerows(data)

        print(f"Data telah disimpan dalam file {filename}")
