
# data table  
import pandas as pd
import requests
from bs4 import BeautifulSoup
import json
import re
import csv

baseurl = 'https://www.jpx.co.jp/english/markets/equities/suspended/index.html'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43'
}

fields = ['Issue Name', 'Code', 'Date',  'Suspension Time Start', 'Suspension Time End',  'Trading Restart Time' , 'Reason' , 'Trading Halts Title' , 'Trading Halts Notice' , 'Trading Halts Notice URL']
filename = '40.0095.csv'

data = []

r = requests.get(baseurl, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

title = soup.find('h2', class_='heading-title').text.strip()

notice = soup.find('p', class_='component-text').text.strip()


url_element = soup.find('a', class_='link-window')
urlDetail = url_element['href']


table = soup.find('table', class_='widetable')

# # Membaca tabel HTML dengan pandas
df = pd.read_html(str(table))[0]

# Mengganti nama kolom
df.columns = ['IssueName', 'Code', 'Date', 'SuspensionTime_Start', 'SuspensionTime_End', 'TradingRestartTime', 'Reason']

# Menggabungkan baris yang memiliki rowspan
df['IssueName'] = df['IssueName'].fillna(method='ffill')

# Menghapus baris yang memiliki nilai null pada kolom 'Code'
df = df.dropna(subset=['Code'])

# Mengisi data kosong pada kolom 'Date'
df['Date'] = df['Date'].fillna(method='ffill')

# Mengisi data kosong pada kolom 'SuspensionTime_Start', 'SuspensionTime_End', 'TradingRestartTime', dan 'Reason'
df['SuspensionTime_Start'] = df['SuspensionTime_Start'].fillna(method='ffill')
df['SuspensionTime_End'] = df['SuspensionTime_End'].fillna(method='ffill')
df['TradingRestartTime'] = df['TradingRestartTime'].fillna(method='ffill')
df['Reason'] = df['Reason'].fillna(method='ffill')

# Menampilkan data
for _, row in df.iterrows():
    
    issueName = row['IssueName']
    code = row['Code']
    date_ = row['Date']
    suspensionTime_Start = row['SuspensionTime_Start']
    suspensionTime_End = row['SuspensionTime_End']
    tradingRestartTime = row['TradingRestartTime']
    reason = row['Reason']
    print()

    data_40_0095 = {
        'Issue Name': issueName,
        'Code': code,
        'Date': date_ ,
        'Suspension Time Start': suspensionTime_Start,
        'Suspension Time End': suspensionTime_End,
        'Trading Restart Time': tradingRestartTime,
        'Reason': reason,
        'Trading Halts Title': title,
        'Trading Halts Notice': notice,
        'Trading Halts Notice URL': urlDetail 
    }
    print('Saving', data_40_0095['Issue Name'], data_40_0095['Code'], data_40_0095['Date'], data_40_0095['Suspension Time Start'], data_40_0095['Suspension Time End'] , data_40_0095['Trading Restart Time'], data_40_0095['Reason'], data_40_0095['Trading Halts Title'], data_40_0095['Trading Halts Notice'], data_40_0095['Trading Halts Notice URL'] )
    data.append(data_40_0095)
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)

    print(f"Data telah disimpan dalam file {filename}")




