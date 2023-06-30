# import csv
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd

# baseurl = 'https://competition.md/decizii.php?l=en&idc=64&year=&month=&day=&t=/Transparency/Decisions/&'
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.58'
# }

# # fields = ['Liquidator', 'Bank Name', 'Legal Address', 'Contacts', 'Document regarding the appointment as Liquidator', 'Bank Information', 'Date information']
# # filename = '40.1145.csv'
# page = 1
# while True:
#     url = f"{baseurl}page={page}"
#     r = requests.get(baseurl, headers=headers)
#     soup = BeautifulSoup(r.content, 'lxml')

#     data = []
#     setionItem = soup.find_all('div', class_='bg17')[2]

#     listItem = setionItem.find('table')
#     for urlPage in listItem.find_all('a', class_='link_block_title'):
#         urlItem = 'https://competition.md/'+urlPage['href']
#         name = urlPage.text
#         print()
#         print(name, urlItem)
#         print()
#     page += 1



import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd

baseurl = 'https://competition.md/decizii.php?l=en&idc=64&year=&month=&day=&t=/Transparency/Decisions/&'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.58'
}

page = 1
while True:
    url = f"{baseurl}page={page}"
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    print()
    print(url)
    print()

    data = []
    setionItem = soup.find_all('div', class_='bg17')[2]

    listItem = setionItem.find('table')

    if not listItem:
        print("No table found.")
        break
    
    for urlPage in listItem.find_all('a', class_='link_block_title'):
        urlItem = 'https://competition.md/' + urlPage['href']
        name = urlPage.text
        print()
        print(name, urlItem)
        print()

    # Pindahkan peningkatan halaman ke bagian akhir perulangan
    page += 1

    # # Cek apakah halaman berikutnya masih ada dengan mencari konten pada halaman saat ini
    # if not listItem.find_next_sibling():
    #     break
