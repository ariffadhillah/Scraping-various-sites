import requests
from bs4 import BeautifulSoup
import csv
import re

url = 'https://new.nsf.gov/about/leadership'

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

find_section = soup.find_all('div', class_='palette palette--light-gray layout-container--wrapper nsf-layout nsf-layout--threecol full-browser-width')

for info in find_section:
    titleelement = info.find_all('div', class_='text__content text-formatted')
    
    for title_elem in titleelement:
        h4_elements = title_elem.find_all('h2')
        for titleh4 in h4_elements:
            title = titleh4.text.strip()
            print(title)

