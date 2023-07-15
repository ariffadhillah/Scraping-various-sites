import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv

baseurl = 'https://www.lbr.lu/mjrcs/jsp/DisplayCourtOrderActionNotSecured.action?FROM_MENU=true&time=1573659740828&currentMenuLabel=menu.item.courtorder'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67'
}

fields = ['Type of statement', 'Period', 'Updated on', 'Statement of court']
filename = '60.0007.csv'
data = []


r = requests.post(baseurl, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')


search = soup.find('table', {'commonTable'})
tbody = search.find('tbody')
titleBankruptcies = tbody.find_all('tr', class_='odd')[1]

th_elements = titleBankruptcies.find_all('td')

for statement in th_elements[0]:
    statement.text

for period in th_elements[1]:
    period.text

for updated  in th_elements[2]:
    updated.text

data_60_0007 = {
    'Type of statement': statement,
    'Period' : "'"+period,
    'Updated on' : updated,
    'Statement of court' : 'Statement of court and administrative dissolution rulings filed with the RCS'    
}

data.append(data_60_0007)
print('Saving', data_60_0007['Type of statement'])
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(data)
                    
