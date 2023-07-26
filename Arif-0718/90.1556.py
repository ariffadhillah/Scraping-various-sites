import csv
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

baseurl = 'https://www.mnse.me/code/navigate.asp?Id=935'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82'
}

fields = ['Bank Name', 'Phone' , 'Fax' , 'Mobile Number' , 'Email' , 'Website']
filename = '90.1556.csv'
data = []

r = requests.get(baseurl, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

search_list = soup.find_all('div', class_='block')
if search_list:
    for listbanks in search_list:
        namebanks_ = listbanks.find('p').text.strip()
        namebanks = namebanks_.replace('Custody','').replace(' - ','').replace(' – ','')

        phone_label = listbanks.find(string=re.compile(r'Phone:'))
        phone = phone_label.replace('Phone:','') if phone_label else ''  

        fax_label = listbanks.find(string=re.compile(r'Fax:'))
        fax = fax_label.replace('Fax:','') if fax_label else ''  
        
        mob_label = listbanks.find(string=re.compile(r'Mob:'))
        mob = mob_label.replace('Mob:','') if mob_label else ''  

        email_label = listbanks.find('a', href=lambda href: href and href.startswith('mailto:'))
        email = email_label['href'][7:] if email_label else "Email Not Found"

        # Extract the website URL
        website_label = listbanks.find('a', href=lambda href: href and href.startswith('http://'))
        website = website_label['href'] if website_label else "Website Not Found"

        data_90_1556 = {
            'Bank Name': namebanks,
            'Phone' : phone,
            'Fax' : fax,           
            'Mobile Number': mob,
            'Email' : email,
            'Website': website,
        }
        data.append(data_90_1556)
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            writer.writerows(data)

print(f"Save to {filename}")


