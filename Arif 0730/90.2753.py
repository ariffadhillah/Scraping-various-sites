import requests
from bs4 import BeautifulSoup
from itertools import zip_longest
import csv

baseurl = 'https://www.cbp.gov/about/contact/find-broker-by-port/3512'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188'
}

fields = ['Broker Names', 'Broker Filer Code', 'Address', 'Phone', 'Details Page Link']
filename = '90.2753.csv'

data = []

page = 0
while True:
    produclinks = []
    url = f"{baseurl}?page={page}"
    print(url)

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    search_table = soup.find('table', class_='usa-table views-table views-view-table cols-2')
    
    if search_table is None:
        break
    
    listItems = search_table.find_all('td', class_='views-field views-field-title-1')

    if len(listItems) == 0:
        break

    for itemLINK in listItems:
        itemURL = itemLINK.find('a', href=True)
        url_page_Details = 'https://www.cbp.gov' + itemURL['href']
        name = itemURL.text

        r = requests.get(url_page_Details, headers=headers)
        soup = BeautifulSoup(r.content, 'lxml')

        try:
            address = soup.find('p', class_='address').text.strip().replace('\n', '  ')        
        except:
            address = ''    
        
        try:
            phones = soup.find('td', class_='views-field views-field-field-phone').text.strip()
        except:
            phones = ''

        broker_filer_code = url_page_Details.split("/")[-1]
        if broker_filer_code[0].isdigit(): 
            broker_filer_code = "'" + broker_filer_code

        data_90_2753 = {
            'Broker Names': name,
            'Broker Filer Code': broker_filer_code,
            'Address': address,
            'Phone': phones,
            'Details Page Link': url_page_Details
        }
        
        data.append(data_90_2753)
        print('Saving', data_90_2753['Broker Names'], data_90_2753['Broker Filer Code'])
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            for item in data:
                writer.writerow(item)   

    
    page += 1            
