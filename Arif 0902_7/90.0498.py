import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.bolsasymercados.es/bme-exchange/en/Trading/Participation/Equities-Members'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69'
}

data = []

fields = ['Name' , 'Code' , 'Business Address' , 'Website' , 'Exchange']
filename = '90.0498.csv'

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

find_section = soup.find('div', class_='table-responsive')

find_table = find_section.find('table')

find_tbody_table = soup.find('tbody', {'role':'rowgroup'})
for find_tr in find_tbody_table.find_all('tr'):
    find_td = find_tr.find_all('td')

    if find_td:
        name = find_td[0].text
        code = find_td[1].text
        businessAddress = find_td[2].text.replace('Website','')
        website_element = find_td[2].find('a', href=True)
        website = website_element['href'] if website_element else ""
        exchange_ = find_td[3].text
        
        # print(name)
        # print(code)
        # print(businessAddress)
        # print(website)
        # print(exchange_)

        data_save = {
            'Name' : name,
            'Code' : code,
            'Business Address' : businessAddress,
            'Website' : website,
            'Exchange' :  exchange_
        }
        data.append(data_save)
        print('Saving', data_save['Name'])
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            writer.writerows(data)
