from requests_html import HTMLSession
import csv
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd


baseurl = 'https://www.sc.com.my/regulation/enforcement/actions'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43'
}

fields = ['Parties Involved', 'Nature of Misconduct', 'Brief Description Of Misconduct', 'Action Taken', 'Date Of Action' , 'Name Document',  'Links Document' ]
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

        
    table = soup.find('table', class_='tab_format')

    # Membaca tabel HTML dengan pandas
    df = pd.read_html(str(table))[0]

    # Menghapus baris yang memiliki semua kolom kosong
    df = df.dropna(how='all')

    # Menyesuaikan jumlah kolom yang diharapkan
    expected_columns = ['No', 'Nature of Misconduct', 'Parties Involved',  'Brief Description Of Misconduct',  'Action Taken', 'Date Of Action']

    # Menambahkan kolom kosong jika jumlah kolom aktual kurang dari yang diharapkan
    if len(df.columns) < len(expected_columns):
        diff = len(expected_columns) - len(df.columns)
        df = pd.concat([df, pd.DataFrame(columns=expected_columns[-diff:])], axis=1)

    # Mengganti nama kolom
    df.columns = expected_columns

    # Menampilkan data
    for _, row in df.iterrows():
        if any(row[expected_columns]):
            no = row['No']
            partiesInvolved = row['Parties Involved']
            natureofMisconduct = row['Nature of Misconduct']
            briefdescriptionofmisconduct = row['Brief Description Of Misconduct']
            actionTaken = row['Action Taken']
            dateofAction = row['Date Of Action'] if pd.notna(row['Date Of Action']) else ' '

            print()            

            data_40_0308 = {
                'Links Document': link,
                'Name Document': titleCase,
                'Parties Involved': partiesInvolved,
                'Nature of Misconduct': natureofMisconduct,
                'Brief Description Of Misconduct': briefdescriptionofmisconduct,
                'Action Taken': actionTaken,
                'Date Of Action':dateofAction,
            }

            print('Saving', data_40_0308['Parties Involved'], data_40_0308['Name Document'])

            data.append(data_40_0308)

    # Menulis data ke dalam file CSV
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(data)

print(f"Saving file {filename}")

