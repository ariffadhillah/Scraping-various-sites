import requests
from bs4 import BeautifulSoup
import csv
import re
import codecs

url = 'https://dfpi.ca.gov/actions-and-orders-listed-by-month/'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203'
}

data = []

fields = ['Month / Year list' ,  'Url PDF']
filename = '40.1638.csv'

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'html.parser')

find_ul_list = soup.find_all('ul', class_='list-standout')

for find_ul in find_ul_list:
    li_elements = find_ul.find_all('li')
    for li in li_elements:
        linkpdf = li.find('a')
        if linkpdf:
            try:
                hrefpdf = linkpdf['href'].replace('https://dfpi.ca.gov','')
                name = linkpdf.get_text()

                data_save = {
                    'Month / Year list' : name,
                    'Url PDF' :'https://dfpi.ca.gov'+hrefpdf
                }

                data.append(data_save)
                print('Saving', data_save['Month / Year list'])
                with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=fields)
                    writer.writeheader()
                    writer.writerows(data)

            except:
                href = ''

