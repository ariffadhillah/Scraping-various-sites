import time
import requests
from bs4 import BeautifulSoup
import csv


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.200',
    'Cookie' : 'rps_csrf_cookie_rps=a307f4210c310b9f733cd473c8854511; _gid=GA1.2.1517858707.1691682723; _clck=1wctg8c|2|fe1|0|1312; visited=yes; _ga=GA1.1.965369947.1691278792; rps_session=66d1ccf3e33e03dd1a5e2e300453f0620fbfb80f; _clsk=ijlhqh|1691683307278|4|1|x.clarity.ms/collect; _ga_MGVSKKS86Y=GS1.1.1691682722.6.1.1691683311.60.0.0'
}

url = 'https://www.rcips.ky/about/police-officer/'

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

fields = ['Names', 'Office' , 'Roles' , 'Phone Number' , 'Email' , 'Police Station Address' , 'PII']
filename = '20.1156.csv'

data = []
processed_urls = set()
listPageURL = []

find_section = soup.find('section', class_='inner_section community_page police_officer_page')

team_info = find_section('div', class_='team_info')

for pageInfo in team_info:
    for pageUrl in pageInfo.find_all('a', href=True):
        url = pageUrl['href']
        if url not in processed_urls:
            listPageURL.append(url)
            processed_urls.add(url)

for details in listPageURL:
    r = requests.get(details, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    search_info = soup.find('div', class_='info')
    name = search_info.find('h2').text.strip()
    location = search_info.find('span', class_='location').text.strip()
    position = search_info.find('div', class_='position').text.strip().replace(location, '').replace('\n', '')

    phoneinfo = soup.find_all('div', class_='info_box fl')[0].text.strip().replace('Phone:', '').replace('\n', '')
    emailinfo = soup.find_all('div', class_='info_box fl')[1].text.strip().replace('Email:', '').replace('\n', '')
    policeStationAddress = soup.find('div', class_='plc_add').text.strip().replace('Police Station Address:', '')
    pII = soup.find('div', class_='content').text.strip()

    data_20_1156 = {
        'Names': name,
        'Office' : location,
        'Roles' : position,
        'Phone Number' :   phoneinfo,
        'Email' : emailinfo,
        'Police Station Address' : policeStationAddress,
        'PII' : pII
    }
    
    data.append(data_20_1156)
    print('Saving', data_20_1156['Names'])
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)