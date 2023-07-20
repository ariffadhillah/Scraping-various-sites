import csv
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd


baseurl = 'https://www.jseza.com/sez-registry/list-of-special-economic-zone-entities-in-jamaica/'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82'
}

fields = ['Name of Entity', 'SEZ Status' ,  'Town/City' , 'Parish']
filename = '90.1550.csv'
data = []

processed_urls = set()
lawfirmList = []

r = requests.get(baseurl, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

data = []


table = soup.find('table', {'width':'717'})
df = pd.read_html(str(table), header=0)[0]
df.columns = ['#', 'Name of Entity', 'SEZ Status', 'Town/City', 'Parish']
# df['Name of Entity'] = df['Name of Entity'].fillna(method='ffill')

for _, row in df.iterrows():
    no = row['#']
    nameofEntity = row['Name of Entity']
    sEZ_Status = row['SEZ Status']
    town_City = row['Town/City']
    parish = row['Parish']

    # print(nameofEntity)



    data_90_1550 = {
        'Name of Entity' : nameofEntity,
        'SEZ Status' : sEZ_Status,
        'Town/City' : town_City,
        'Parish' : parish
    } 



    data.append(data_90_1550)
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)

print(f"Data telah disimpan dalam file {filename}")

