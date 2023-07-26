import requests
from bs4 import BeautifulSoup
import csv

baseurl = 'https://www.surinamestockexchange.com/nl/over-ons/partners'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183'
}

r = requests.get(baseurl, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

data = []

search_table = soup.find_all('table', class_='contentpaneopen')[1]
listItems = search_table.find_all('ul')


for item in listItems:
    company_names = item.find_all('li')
    for company_name in company_names:        

        data_90_2440 = {
            'Company Name' : company_name.text.strip(),
            'Partners' : 'Partners'
        }

        data.append(data_90_2440)
        print('Saving', data_90_2440['Company Name'])

# Write the data to a CSV file
fields = ['Company Name', 'Partners']
filename = '90.2440.csv'

with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(data)