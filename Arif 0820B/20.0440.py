from bs4 import BeautifulSoup
import requests
import json
import csv

baseurl = 'https://www.nyc.gov/site/nypd/about/leadership/leadership-landing.page'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.54'
}

data = []

r = requests.get(baseurl, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

find_table = soup.find('div', class_='span6 about-description')

tr_elements = find_table.find_all('tr')

data_list = []

# Loop melalui setiap elemen <tr> dan ambil informasi yang diinginkan
for tr in tr_elements:
    td_elements = tr.find_all('td')
    if len(td_elements) == 2:
        data_label = td_elements[0].get('data-label').replace('Bureau Chiefs','Chiefs')
        roles = td_elements[0].get_text()
        name = td_elements[1].get_text()
        data_list.append([name, roles, data_label])
    elif len(td_elements) == 1:
        data_label = td_elements[0].get('data-label')
        name = td_elements[0].get_text()
        data_list.append([name, "", data_label])

# Menyimpan data ke dalam file CSV
csv_filename = '20.0440.csv'
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Name', 'Roles', 'Title'])  # Menulis header
    csv_writer.writerows(data_list)  # Menulis data

print(f"Data telah disimpan dalam file {csv_filename}")