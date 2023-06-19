import csv
import requests
from bs4 import BeautifulSoup, Tag

baseurl = 'https://www.sc.com.my/regulation/enforcement/actions'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43'
}

r = requests.get(baseurl, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

data = []
processed_urls = set()
casesCompounded = soup.find_all('li', class_='st-item')[2]

search_Ul = casesCompounded.find('ul')

urlCase = []
for item in search_Ul:
    for itemURL in item.find_all('a', href=True):
        url = itemURL['href']
        if url not in urlCase:
            urlCase.append(url)


for link in urlCase:
    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    table_ = soup.find('table', class_='tab_format table-with-header table-with-border table-vertical-border table-horizontal-border')    
    for tbody in table_.find_all('tbody'):
        if isinstance(tbody, Tag): 
            for tr in tbody.find_all('tr'):
              
                try:
                    cells = tr.find_all('td')
                    if len(cells) == 5:
                        offender_s = cells[2].text.strip()
                    elif len(cells) == 5:
                        offender_s = cells[2].text.strip()
                    else:
                        continue
                except:
                    continue
              
                try:
                    cells = tr.find_all('td')
                    if len(cells) == 5:
                        factsofCase = cells[3].text.strip()
                    elif len(cells) == 5:
                        factsofCase = cells[3].text.strip()
                    else:
                        continue

                except:
                    continue
                try:
                    natureofOffence = tr.find_all('td')[1].text.strip()
                except:
                    continue

                try:
                    cells = tr.find_all('td')
                    if len(cells) >= 1:
                        DateCharged = cells[-1].text.strip().replace('  ', '')
                        print(DateCharged)
                except:
                    continue

                print(offender_s,natureofOffence, factsofCase, DateCharged)

             