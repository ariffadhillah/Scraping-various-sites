import requests
from bs4 import BeautifulSoup
import json
import re
import csv

baseurl = 'https://www.sfc.hk/en/Regulatory-functions/Enforcement/Upcoming-hearings-calendar'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43'
}

fields = ['Date of Hearing / court', 'Status', 'Offence', 'Defendent']
filename = '40.0045.csv'

data = []

r = requests.get(baseurl, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

find_table_script = soup.find_all('script')[13]
find_table_text = find_table_script.text.strip()

# Temukan data JSON menggunakan regex
search_data = re.compile(r'var data = (\[.*?\]);', re.DOTALL)
data_match = search_data.search(find_table_text)

if data_match:
    json_data = data_match.group(1)
    dataSearch = json.loads(json_data)
    
    if dataSearch:
        for itemData in dataSearch:
            # id = item['id']
            display_date = itemData['display-date']
            status = itemData['status']
            offence = itemData['offence'].replace('<br/><br/>', '\n')
            defendent = itemData['defendent']

            data_40_0045 = {
                'Date of Hearing / court': display_date,
                'Status': status,
                'Offence': offence,
                'Defendent': defendent,

            }

            print('Saving', data_40_0045['Date of Hearing / court'], data_40_0045['Status'])
            data.append(data_40_0045)

            # Menulis data ke dalam file CSV
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fields)
                writer.writeheader()
                writer.writerows(data)

            print(f"Data telah disimpan dalam file {filename}")


    else:
        print("Data tidak ditemukan dalam JSON.")
else:
    print("Tidak ada data JSON yang ditemukan.")
