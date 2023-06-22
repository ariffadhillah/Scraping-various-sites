from requests_html import HTMLSession
import csv
import requests
from bs4 import BeautifulSoup

baseurl = 'https://www.sc.com.my/regulation/enforcement/actions'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43'
}

fields = ['Name', 'Nature of Offence', 'Facts of Case', 'Compound Imposed', 'Name Document', 'Links Document']
filename = '40.0291.csv'

r = requests.get(baseurl, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

data = []
processed_urls = set()
casesCompounded = soup.find_all('li', class_='st-item')[2]

search_Ul = casesCompounded.find('ul')

urlCase = []
for itemLINK in search_Ul:
    for itemURL in itemLINK.find_all('a', href=True):
        url = itemURL['href']
        if url not in urlCase:
            urlCase.append(url)


for link in urlCase:
    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    titleCase = soup.find('div', {'data-so-type': 'txt;1'}).text.strip()

    