import requests
from bs4 import BeautifulSoup
import csv
import re

url = 'https://new.nsf.gov/about/leadership#od'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203'
}

fields = ['Names', 'Titles' , 'Biography']
filename = '20.3320.csv'

data = []

list_item = []
processed_urls = set()

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

find_section = soup.find_all('div', class_='palette palette--light-gray layout-container--wrapper nsf-layout nsf-layout--threecol full-browser-width')

for card_ in find_section:
    card_item = card_.find('div', class_='nsf-layout--outer')
    
    for title_element in card_item:
        titleelement = title_element.find('div', class_='text__content text-formatted')
        # print(titleelement)
        for title_elem in titleelement:
            h4_elements = title_elem.find('h2')
            for titleh4 in h4_elements:
                title = titleh4.text.strip()
                print(title)

# for info in find_section:

# for infocardName in find_section:
        
#     cardinfo = infocardName.find_all('div', {'class':['nsf-layout--inner']})
#     nsf-layout--outer
# text__content text-formatted

# for find_card_item in find_section:
#     card_item = find_card_item.find('div', class_='nsf-layout--outer')
#     print(card_item)