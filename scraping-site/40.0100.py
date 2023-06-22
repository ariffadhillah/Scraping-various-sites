
import pandas as pd
import requests
from bs4 import BeautifulSoup
import json
import re
import csv


baseurl = 'https://www.jpx.co.jp/english/listing/measures/alert/archives/index.html'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43'
}



fields = ['Issue Name', 'Designation Date', 'Code',  'Market Segment', 'Removal Date', 'Remarks', 'Designation of Securities on Alert', 'URL' ]
filename = '40.0100.csv'

data = []

r = requests.get(baseurl, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

title = soup.find('h2', class_='heading-title-mu').text.strip()


table = soup.find('table')

df = pd.read_html(str(table))[0]

# Mengganti nama kolom
df.columns = ['Designation Date', 'Issue Name', 'Code', 'Market Segment', 'Removal Date', 'Remarks']

df['Designation Date'] = df['Designation Date'].fillna(method='ffill')
df['Issue Name'] = df['Issue Name'].fillna(method='ffill')
df['Code'] = df['Code'].fillna(method='ffill')
df['Market Segment'] = df['Market Segment'].fillna(method='ffill')
df['Removal Date'] = df['Removal Date'].fillna(method='ffill')
df['Remarks'] = df['Remarks'].fillna(method='ffill')

for _, row in df.iterrows():
    designationDate = row['Designation Date']
    issueName = row['Issue Name']
    code = row['Code']
    marketSegment = row['Market Segment']
    removalDate = row['Removal Date']
    remarks = str(row['Remarks']).replace('nan', '')

    data_40_0100 = {
        'Issue Name':issueName,
        'Designation Date': designationDate,
        'Code': code,
        'Market Segment': marketSegment,
        'Removal Date': removalDate,
        'Remarks': remarks,
        'Designation of Securities on Alert': title,
        'URL': baseurl
    }

    print('Saving', data_40_0100['Issue Name'], data_40_0100['Designation Date'])
    data.append(data_40_0100)
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)

    print(f"save file {filename}")