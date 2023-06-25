import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = 'https://journaldemonaco.gouv.mc'

url = 'https://journaldemonaco.gouv.mc/content/search?SearchText=&filter%5b%5d=attr_theme_s:%22Licenciements%22&activeFacets%5battr_theme_s:Th%C3%A8mes%5d=Licenciements&activeFacets%5barticle_jdm/category:Cat%C3%A9gories%5d=Avis%20et%20Communiqu%C3%A9s&sort=published_desc&page_limit=15'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.58'
}

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
            title = TextURLTitle.text.replace('\n', '').replace('  ','')
            pageItem.append((base_url + link, title))
            processed_urls.add(link)

for pageURL, title in pageItem:
    r = requests.get(pageURL, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    print(pageURL, title)
