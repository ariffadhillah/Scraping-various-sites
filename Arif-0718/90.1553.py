import csv
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

baseurl = 'https://www.jamstockex.com/listings/listed-companies/'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82'
}

fields = ['Company Name', 'Symbol', 'Currency', 'Sector', 'Type', 'Website']
filename = '90.1553.csv'
data = []

r = requests.get(baseurl, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

search_table = soup.find('table', class_='tw-mb-0 tw-divide-y tw-divide-gray-200')
for tr in search_table.find_all('tr')[1:]:  
    if tr:
        td_elements = tr.find_all('td')
        if len(td_elements) >= 2:  
            companiesName = td_elements[0].text.strip()
            symbol_ = td_elements[1].text.strip()
            currency_ = td_elements[2].text.strip()
            sector_ = td_elements[3].text.strip()
            type_ = td_elements[4].text.strip()
            website_element = td_elements[5].find('a')
            website_ = website_element['href'] if website_element else ''
            # print(nameCompanies)
            # print(website_)
        else:
            companiesName = ''
            currency_ = ''
            symbol_ = ''
            sector_ = ''
            type_ = ''
            website_ = ''


                
        data_90_1553 = {
            'Company Name' : companiesName,
            'Symbol' : symbol_,
            'Currency': currency_,
            'Sector': sector_,
            'Type': type_,
            'Website': website_.replace('nmcms.php?snippet=services&p=service_details&id=27','').replace('index.php?Section=1&PageId=9901&Flag=','')
        } 

        data.append(data_90_1553)
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            writer.writerows(data)

print(f"Save to {filename}")
