import requests
from bs4 import BeautifulSoup
import json
import re
import csv

baseurl = 'https://eservices.mas.gov.sg/fid/institution?sector=Banking&'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67'
}

fields = ['Name', 'Company Name', 'Phone Number' , 'Address', 'Url / Site Company', 'Name Link / Page URL']
filename = '90.0948.csv'

data = []


for x in range(1, 100):
    url = f"{baseurl}page={x}"
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    resultList = soup.find('div', class_='result-list resize')
    for item in resultList.find_all('a', class_='', href=True):
        pageUrl = 'https://eservices.mas.gov.sg' + item['href']
        
        r = requests.get(pageUrl, headers=headers)
        soup = BeautifulSoup(r.content, 'lxml')
        # print(pageUrl)

        try:
            companyName = soup.find('h1').text.strip()
        except:
            companyName = ''
            
        find_name = soup.find('div', class_='key-personnel')
        try:
            name = find_name.find_all('td')[1].text
        except:
            name = ''

        description = soup.find('div', class_='description')

        try:
            phoneLink = description.find('a', href=re.compile(r'^tel:'))
            phoneNumber = phoneLink.get('href').split(':')[1]
        except:
            phoneNumber = ''

        try:
            link = description.find('a', class_='font-resize', target='_blank')
            urlsite = link['href']
        except:
            urlsite = ''
        try:
            address = description.find('td', class_='font-resize').text.strip()
        except:
            address = ''

        data_90_0948 = {
            'Name': name,
            'Company Name': companyName,
            'Phone Number': phoneNumber,
            'Address': address,
            'Url / Site Company' : urlsite,
            'Name Link / Page URL' : pageUrl 
        }
        data.append(data_90_0948)
        print('Saving', data_90_0948['Name'], data_90_0948['Company Name'])
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            writer.writerows(data)

print(f"Save data to file {filename}")


