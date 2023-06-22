import pandas as pd
import requests
from bs4 import BeautifulSoup

# Simpan URL halaman HTML
url = 'https://www.jpx.co.jp/english/markets/derivatives/suspended/index.html'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43'
}

# Mengirim permintaan HTTP ke URL dan mendapatkan konten HTML
response = requests.get(url, headers=headers)
html_content = response.content

# Parsing HTML menggunakan BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Mencari semua tabel dalam HTML
tables = soup.find_all('table')

# List untuk menyimpan semua baris
data = []

# Loop melalui setiap tabel
for table in tables:
    # Membaca tabel HTML dengan pandas
    df = pd.read_html(str(table))[0]

    # Mengubah nama kolom
    df.columns = ['Label', 'Value']

    # Mengubah baris menjadi kolom
    table_data = df.set_index('Label').T.to_dict('records')[0]

    # Menambahkan data ke dalam list
    data.append(table_data)

# Membuat DataFrame dari list data
df = pd.DataFrame(data)

# Menyimpan DataFrame ke dalam file CSV dengan pengkodean UTF-8
filename = '40.0094.csv'
df.to_csv(filename, index=False, encoding='utf-8')

print(f"Data berhasil disimpan dalam file {filename}")
