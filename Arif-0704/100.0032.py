import requests
from bs4 import BeautifulSoup
import json
import re
import csv

baseurl = 'https://www.charities.gov.sg/Pages/News-and-Notices/Notices-and-Orders-of-The-Commissioner-of-Charities.aspx'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67'
}

fields = ['Title', 'Links Document', 'Notification']
filename = '100.0032.csv'

r = requests.get(baseurl, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

data = []

searcH = soup.find_all('ol', class_='caption weight-medium list-nogap mar-bot-0')[0]
for itemLINK in searcH:
    for itemURL in itemLINK.find_all('a', href=True):
        url = itemURL['href']
        name = itemURL.text
        data_100_0032 = {
            'Title': name,
            'Links Document' : 'https://www.charities.gov.sg'+url,
            'Notification': 'Fund-Raising Prohibition Orders'            
        }
        print('Saving', data_100_0032['Title'])        
        data.append(data_100_0032)

        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            writer.writerows(data)

        print(f"Save data to file {filename}")
        

