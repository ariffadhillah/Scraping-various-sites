import requests
from bs4 import BeautifulSoup
import csv

baseUrl = 'https://www.bnm.md'

url = 'https://www.bnm.md/en/content/authorized-banks-republic-moldova'


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67'
}

fields = ['Name', 'Link Page', 'Date Information']
filename = '40.1147.csv'


r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

data = []
pageRedirect = []
menuAll = soup.find_all('div', {'class':'sub-nav'})[3]
subMenu = menuAll.find_all('div', class_='sub-nav-menu')[6]
for redirectPage in subMenu.find_all('a', href=True)[1:]:
    page = redirectPage['href']
    pageRedirect.append(baseUrl+page)

for pageItem in pageRedirect:
    r = requests.get(pageItem, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    item = []    
    widgetList = soup.find_all('div', class_='views-field-title')
    for widgetList in widgetList:
        itemUrl = widgetList.find('a')
        if itemUrl:
            # name = itemUrl.text 
            url = baseUrl+itemUrl['href']
            item.append(url)
   
    for link in item:
        r = requests.get(link, headers=headers)
        soup = BeautifulSoup(r.content, 'lxml')

        dateInfo = soup.find('div', class_='date-info full-date-info').text.strip()
        name = soup.find('h1', class_='title').text.strip()

        data_40_1147 = {
            'Name': name,
            'Link Page': link,
            'Date Information': dateInfo
        }
        data.append(data_40_1147)
        print('Saving..', data_40_1147['Name'] , data_40_1147['Link Page'])
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            for item in data:
                writer.writerow(item) 
