import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.hkex.com.hk/Products/Listed-Derivatives/Equity-Index/Hang-Seng-Index-(HSI)/Hang-Seng-Index-Futures?sc_lang=en#&product=HSI'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69'
}

data = []

fields = ['Company Name' , 'Contact Number' , 'Email']
filename = '90.0748.csv'

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

find_section = soup.find('section', id='pagecontent_0_maincontent_5_TitleContentSection')
find_table = find_section.find('table')

find_tbody_table = find_table.find('tbody')

for find_tr in find_tbody_table.find_all('tr'):
    find_td = find_tr.find_all('td')

    if find_td:
        companyName = find_td[0].text
        contactNumber = find_td[1].text.strip()
        email = find_td[2].text

        # print(companyName.strip())
        # print(contactNumber)
        # print(email.strip())
        # print( )

        data_save = {
            'Company Name' : companyName.strip(),
            'Contact Number' : contactNumber,
            'Email' : email.strip()
        }
        data.append(data_save)
        print('Saving', data_save['Company Name'])
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            writer.writerows(data)