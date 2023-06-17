# import requests
# from bs4 import BeautifulSoup
# import json
# import re

# baseurl = 'https://www.jpx.co.jp/english/markets/equities/suspended/index.html'
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43'
# }

# r = requests.get(baseurl, headers=headers)
# soup = BeautifulSoup(r.content, 'lxml')

# find_table = soup.find('div', id='readArea')
# for title in find_table.find_all('h1', 'h2'): 
#     print(title)


import requests
from bs4 import BeautifulSoup

baseurl = 'https://www.jpx.co.jp/english/markets/equities/suspended/index.html'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43'
}

r = requests.get(baseurl, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

read_area = soup.find('div', id='readArea')

# Cari elemen <h1> dan <h2> di dalam readArea
for title in read_area.find_all(['h1', 'h2']):
    print(title.text.strip())
