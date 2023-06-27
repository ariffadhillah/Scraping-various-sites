import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

base_url = 'https://journaldemonaco.gouv.mc'

url = 'https://journaldemonaco.gouv.mc/content/search/(offset)/30?SearchText=&activeFacets[attr_theme_s:Th%C3%A8mes]=Extraits%20Judiciaires&activeFacets[attr_category_s:Cat%C3%A9gories]=Insertions%20l%C3%A9gales%20et%20Annonces&activeFacets[article_jdm/category:Cat%C3%A9gories]=Insertions%20l%C3%A9gales%20et%20Annonces&filter[]=attr_theme_s:%22Extraits%20Judiciaires%22&filter[]=attr_category_s:%22Insertions%20l%C3%A9gales%20et%20Annonces%22&sort=published_desc&page_limit=15'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.58'
}

fields = ['Title Link' , 'Title Summary / Content' , 'Newspaper No' , 'Page No' , 'Date of publication' , 'Content' , 'Links Document' , 'View the journal in PDF format']
filename = '50.0061.csv'

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

data = []
processed_urls = set()
pageItem = []

results_content = soup.find('div', class_='search-results__content')
for item in results_content.find_all('a', class_='result-item'):
    link = item['href']
    
    if link not in processed_urls:
        for TextURLTitle in item.find_all('div', class_="result-item__title"):
            titleLink = TextURLTitle.text.replace('\n', '').replace('  ','')
            pageItem.append((base_url + link, titleLink))
            processed_urls.add(link)

for pageURL, titleLink in pageItem:
    r = requests.get(pageURL, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    subTitle = soup.find('h1').text.strip()

    content = soup.find('div', class_='body').text.strip()

    meta_label = soup.find('li', class_='meta')
    njournal = meta_label.find('span', class_='meta__label', string=re.compile(r'^\s*N° journal\s*$'))    
    if njournal:
        njournal_text = njournal.find_next_sibling('span', class_='meta__value').text.strip()
    else:
        njournal_text = ''

    label_noDepage = soup.find_all('li', class_='meta')[3]
    noDepage = label_noDepage.find('span', class_='meta__label', string=re.compile(r'^\s*N° de page\s*$'))    
    if noDepage:
        noDepage_text = noDepage.find_next_sibling('span', class_='meta__value').text.strip()
    else:
        noDepage_text = ''

    label_Datedepublication = soup.find_all('li', class_='meta')[1]
    dateDepublication = label_Datedepublication.find('span', class_='meta__label', string=re.compile(r'^\s*Date de publication\s*$'))    
    if dateDepublication:
        dateDepublication_text = dateDepublication.find_next_sibling('span', class_='meta__value').text.strip()
    else:
        dateDepublication_text = ''
    
    viewthejournalinPDFformat = soup.find('div', class_='u-halfTabUp')
    urlviewthejournalinPDFformat = viewthejournalinPDFformat.find('a', class_='button-file')
    if urlviewthejournalinPDFformat:
        urlPDF = 'https://journaldemonaco.gouv.mc'+urlviewthejournalinPDFformat['href']
        urlPDF
    

        data_50_0063 = {
            'Title Link' : titleLink,
            'Title Summary / Content' : subTitle,
            'Newspaper No' : njournal_text,
            'Page No' : noDepage_text,
            'Date of publication' : dateDepublication_text,
            'Content' : content,
            'Links Document' : pageURL,
            'View the journal in PDF format' : urlPDF
        }
        
        data.append(data_50_0063)
        print('Saving',data_50_0063['Title Link'], data_50_0063['Title Summary / Content'])
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            for item in data:
                writer.writerow(item)               


# Done