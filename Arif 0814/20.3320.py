import requests
from bs4 import BeautifulSoup
import csv
import re

url = 'https://new.nsf.gov/about/leadership#od'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203'
}

fields = ['Names', 'Roles', 'Titles' ]
filename = '20.3320.csv'

data = []

list_item = []
processed_urls = set()

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

find_section = soup.find_all('div', {'class':['palette palette--light-gray layout-container--wrapper nsf-layout nsf-layout--threecol full-browser-width','layout-container--wrapper nsf-layout nsf-layout--threecol full-browser-width','layout-container--wrapper nsf-layout nsf-layout--threecol constrained-width']})
# find_section = soup.find_all('div', {'class':['palette palette--light-gray layout-container--wrapper nsf-layout nsf-layout--threecol full-browser-width','layout-container--wrapper nsf-layout nsf-layout--threecol full-browser-width']} class_='palette palette--light-gray layout-container--wrapper nsf-layout nsf-layout--threecol full-browser-width')


for card_ in find_section:
    card_item = card_.find('div', class_='nsf-layout--outer')

    if card_item:
        titleelement = card_item.find_all('div', class_='text__content text-formatted')        
        for info in titleelement:
            h2_element = info.find(['h2', 'h3'])
            if h2_element:
                title = h2_element.text.strip()
                print(title)
        
        cardText = card_.find_all('div', {'class': ['card-dark-blue card-dark-blue--horizontal block block-layout-builder block-inline-blockcomponent-featured-content', 'layout__region layout__region--first', 'layout__region layout__region--second', 'layout__region layout__region--third']})

        # print(cardText)
        
        for text_elem in cardText:
            text_contents = text_elem.find_all('div', {'class': ['card-dark-blue__text', 'text__content text-formatted']})
            for text_content in text_contents:
                info_text = list(text_content.stripped_strings)
                # print(info_text)

                if info_text:
                    # print(info)
                    # print(info_text)
                    # roles = info[0]
                    name = info_text[0]
                    # roles = info_text[1]
                    roles = '\n'.join(info_text) 

                    data_save = {
                        'Names' : name,
                        'Roles' : roles.replace(name,'').replace('Biography','').strip() ,
                        'Titles' : title
                    }
                    data.append(data_save)
                    print('Saving', data_save['Names'])
                    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                        writer = csv.DictWriter(csvfile, fieldnames=fields)
                        writer.writeheader()
                        writer.writerows(data)



