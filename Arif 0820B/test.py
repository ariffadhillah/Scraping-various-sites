# import requests
# from bs4 import BeautifulSoup
# import csv
# import re
# import time


# url = 'https://home.chicagopolice.org/about/department-offices/'

# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203'
# }

# fields = ['Names', 'Roles', 'Titles' ]
# filename = '20.0449.csv'

# data = []

# list_item = []
# processed_urls = set()

# r = requests.get(url, headers=headers)
# soup = BeautifulSoup(r.content, 'lxml')

# find_item = soup.find('article', id='post-515')
# print(find_item)

# # time.sleep(.5)

# # find_item = soup.find_all('div', class_='col-12')[4]
# # element_h4 = find_item.find_all('h4')
# # for info_h4 in element_h4:
# #     find_href = info_h4.find('a', href=True)
# #     link_details = 'https://www.chicago.gov' + find_href['href']
# #     print(link_details)



# Teks lengkap paragraf
paragraf = "<p>Cathy Leigh Comer Justice, daughter and only child of Thomas Leigh and Virginia Ruth Comer, was born January 28, 1953 in Beckley, WV and grew up in Prosperity, WV.</p>"

# Mencari posisi koma pertama setelah nama
posisi_koma = paragraf.index(",")

# Mengambil teks dari awal hingga posisi koma
nama = paragraf[3:posisi_koma]

print(nama)
