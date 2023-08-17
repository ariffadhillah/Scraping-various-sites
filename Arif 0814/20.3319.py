import requests
from bs4 import BeautifulSoup
import csv
import re

url = 'https://www.nlrb.gov/about-nlrb/who-we-are/the-board'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203'
}

fields = ['Names', 'Titles' , 'Biography']
filename = '20.3319.csv'

data = []

list_item = []
processed_urls = set()

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

find_section = soup.find('div', class_='flex-row')
print(find_section)


# for linkItem in find_section.find_all('a',  href=True):
#     urlbio = linkItem['href'].replace('/about-nlrb/who-we-are/board/','')
#     # print(urlbio)
#     urldetail = 'https://www.nlrb.gov/bio/' + urlbio

#     if urldetail not in processed_urls:
#         list_item.append((urldetail))  
#         processed_urls.add(urldetail)
# print(list_item)