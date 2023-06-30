import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd

baseurl = 'https://www.bnm.md/en/content/liquidators-banks-process-liquidation'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.58'
}

fields = ['Liquidator', 'Bank Name', 'Legal Address', 'Contacts', 'Document regarding the appointment as Liquidator', 'Bank Information', 'Date information']
filename = '60.009.csv'

r = requests.get(baseurl, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

title = soup.find('h1', class_='title').text.strip()
datePage = soup.find('div', class_='date-info full-date-info').text.strip()

data = []

table = soup.find('table')
# df = pd.read_html(str(table), header=0)[0]  # Menggunakan header=0 untuk memuat header dari indeks ke-0
# df = df.iloc[2:, :]  # Memulai dari indeks ke-2 untuk menghindari header

df = pd.read_html(str(table), header=0)[0] 
df.columns = ['No.', 'Liquidator', 'Bank Name', 'Legal Address', 'Contacts', 'Document regarding the appointment as Liquidator']
df['Liquidator'] = df['Liquidator'].fillna(method='ffill')
df = df.dropna(subset=['Bank Name'])

df['Legal Address'] = df['Legal Address'].fillna(method='ffill')
df['Contacts'] = df['Contacts'].fillna(method='ffill')
df['Document regarding the appointment as Liquidator'] = df['Document regarding the appointment as Liquidator'].fillna(method='ffill')

for _, row in df.iterrows():
    liquidator = row['Liquidator']
    bankName = row['Bank Name']
    legalAddress = row['Legal Address']
    contacts = row['Contacts']
    documentLiquidator = row['Document regarding the appointment as Liquidator']

    data_60_009 = {
        'Liquidator': liquidator.replace('Liquidator', ''),
        'Bank Name': bankName.replace('Bank Name', ''),
        'Legal Address': legalAddress.replace('Legal Address', ''),
        'Contacts': contacts.replace('Contacts', ''),
        'Document regarding the appointment as Liquidator': documentLiquidator.replace('Document regarding the appointment as Liquidator', ''),
        'Bank Information': title,
        'Date information': datePage
    }

    data.append(data_60_009)

with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(data)

print(f"Data telah disimpan dalam file {filename}")
