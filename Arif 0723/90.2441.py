import requests
from bs4 import BeautifulSoup
import csv

baseurl = 'https://www.surinamestockexchange.com/nl/bedrijven'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183'
}

r = requests.get(baseurl, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

data = []

search_table = soup.find_all('table', class_='contentpaneopen')[1]
listItems = search_table.find_all('li')
for item in listItems:
    a_tag = item.find('a')
    if a_tag:
        href = a_tag.get('href')
        # print(href)
        company_name = a_tag.text.strip()
        url = 'https://www.surinamestockexchange.com' + href

        data_90_2441 = {
            'Company Name' : company_name,
            'Link Slotkoers' : url
        }

        data.append(data_90_2441)
        print('Saving', data_90_2441['Company Name'])

# Write the data to a CSV file
fields = ['Company Name', 'Link Slotkoers']
filename = '90.2441.csv'

with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(data)