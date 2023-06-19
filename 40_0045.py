# import requests
# from bs4 import BeautifulSoup
# import json
# import re
# import csv

# baseurl = 'https://www.sfc.hk/en/Regulatory-functions/Enforcement/Upcoming-hearings-calendar'
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43'
# }

# r = requests.get(baseurl, headers=headers)
# soup = BeautifulSoup(r.content, 'lxml')

# find_table_script = soup.find_all('script')[13]
# find_table_text = find_table_script.text.strip()

# # Temukan data JSON menggunakan regex
# search_data = re.compile(r'var data = (\[.*?\]);', re.DOTALL)
# dataMatch = search_data.search(find_table_text)
# json_data = dataMatch.group(1)
# data = json.loads(json_data)
# name =  data['id']
# print(name)

# if dataMatch:
# else:
#     print("No JSON")


import requests
from bs4 import BeautifulSoup
import json
import re

baseurl = 'https://www.sfc.hk/en/Regulatory-functions/Enforcement/Upcoming-hearings-calendar'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43'
}

r = requests.get(baseurl, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

find_table_script = soup.find_all('script')[13]
find_table_text = find_table_script.text.strip()

# Temukan data JSON menggunakan regex
search_data = re.compile(r'var data = (\[.*?\]);', re.DOTALL)
data_match = search_data.search(find_table_text)

if data_match:
    json_data = data_match.group(1)
    data = json.loads(json_data)
    
    if data:
        for item in data:
            # id = item['id']
            display_date = item['display-date']
            status = item['status']
            offence = item['offence'].replace('<br/><br/>', '\n')
            defendent = item['defendent']
            
            # print("ID:", id)
            print("Display Date:", display_date)
            print("Status:", status)
            print("Offence:", offence)
            print("Defendent:", defendent)
            print("-------------------")
    else:
        print("Data tidak ditemukan dalam JSON.")
else:
    print("Tidak ada data JSON yang ditemukan.")
