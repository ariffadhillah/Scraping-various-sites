import csv
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

baseurl = 'https://bahrainob.atlassian.net/wiki/spaces/BH/pages/1031012353/Compliance+Status'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82'
}

fields = ['Bank Name']
filename = '90.1558.csv'
data = []

r = requests.get(baseurl, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

search_list = soup.find('div', class_='ak-renderer-document')

listItems = search_list.find_all('ol', class_='ak-ol')

if listItems:
    li_elements = []
    for listItem in listItems:
        li_elements.extend(listItem.find_all('li'))

    for li in li_elements:
        bankname = li.text.strip()

        
        data_90_1558 = {
            'Bank Name': bankname
        }

        data.append(data_90_1558)
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            writer.writerows(data)

    print(f"Save to {filename}")

        
