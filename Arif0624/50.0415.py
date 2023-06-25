# import requests
# from bs4 import BeautifulSoup
# import json
# import re
# import pandas as pd


# url = 'https://instante.justice.md/ro/hotaririle-instantei?Instance=All&Numarul_dosarului=&Denumirea_dosarului=&date=&Tematica_dosarului=&Tipul_dosarului=All'

# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.51'
# }

# r = requests.get(url, headers=headers)
# soup = BeautifulSoup(r.content, 'lxml')

# table = soup.find('table')
# # # Membaca tabel HTML dengan pandas
# df = pd.read_html(str(table))[0]


# df.columns = ['Courts', 'File Number', 'Name', 'Date of delivery', 'Date of registration', 'Published Date', 'Type of folder', 'Dossier topics', 'Judge', 'Judicial document Link']





import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://instante.justice.md/ro/hotaririle-instantei?Instance=All&Numarul_dosarului=&Denumirea_dosarului=&date=&Tematica_dosarului=&Tipul_dosarului=All'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.51'
}

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

table = soup.find('table')
print(table)
