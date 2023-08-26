import requests
from bs4 import BeautifulSoup
from itertools import zip_longest
import csv


baseurl = 'https://www.cbt.tm/tm/banklar.html'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183'
}

data = []

r = requests.get(baseurl, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

search_table = soup.find('div', id='content')
titles = search_table.find_all('h4')
address_list = search_table.find_all('p', class_='mail')
phone_list = search_table.find_all('p', class_='phone')
fax_list = search_table.find_all('p', class_='fax')
url_list = search_table.find_all('p', class_='net')

# Gunakan zip_longest untuk menggabungkan list, mengisi None untuk elemen yang kurang
for companyName, address, phone, fax, url in zip_longest(titles, address_list, phone_list, fax_list, url_list, fillvalue=None):
    company_Name = companyName.text.strip()
    number_Institutions = companyName.find_next_sibling('p').text.strip()
    address_ = address.text.strip()
    phone_ = phone.text.strip() if phone else ""
    fax_ = fax.text.strip() if fax else ""
    url_ = url.find('a')['href'] if url and url.find('a') else ""

    
    # print(company_Name, number_Institutions, address_, phone_, fax_, url_)

    data_90_2444 = {
        'Company Name' : company_Name,
        'Number Institutions': number_Institutions,
        'Address': address_,
        'Phone Number': phone_,
        'Fax': fax_,
        'Site Urls': url_
    }
    data.append(data_90_2444)
    print('Saving', data_90_2444['Company Name'])

    fields = ['Company Name', 'Number Institutions',  'Address' ,  'Phone Number' , 'Fax' , 'Site Urls']
    filename = '90.2444.csv'

with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(data)
