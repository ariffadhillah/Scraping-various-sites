import requests
from bs4 import BeautifulSoup
import csv
import re

url = 'https://orc.govt.nz/our-council-our-region/our-council/your-councillors'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62'
}

data = []

fields = ['Names' , 'Email' , 'Phone'  , 'Roles' , 'Titles' , 'PII']
filename = '20.0731.csv'

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

urlPage = []

processed_urls = set()

find_body = soup.find('div', class_='body-copy')

find_item = find_body.find_all('div', {'class':['col-sm-6','c-card c-card--band']})


for urlDetail in find_item:
    hrefDetail = 'https://orc.govt.nz' + urlDetail.find('a')['href']
    if hrefDetail not in processed_urls:
        urlPage.append(hrefDetail)
        processed_urls.add(hrefDetail)

for pageDetails in urlPage:
    r = requests.get(pageDetails, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    # print(pageDetails)
    
    findBody = soup.find('div', class_='body-copy')

    email_element = findBody.find('p')
    if email_element:
        p_text = email_element.get_text(strip=True)
        a_element_mail = email_element.find('a')        
        if a_element_mail:
            email_text = a_element_mail.get_text(strip=True)

    phone_element = findBody.find_all('p')[1]
    if phone_element:
        p_text_phone = phone_element.get_text(strip=True)
        a_element_phone = phone_element.find('a')        
        if a_element_phone:
            phone_text = a_element_phone.get_text(strip=True)
        else:
            phone_text = ''





    name = findBody.find('h1').text.strip()
    roles_element = findBody.find(['h2','h3'])
    title = findBody.find(['h2','h3']).text.strip()

    if roles_element:
        roles_text = roles_element.get_text().split('-')
    
        if len(roles_text) > 0:
            roles = roles_text[0].strip()

    text_p_elements = findBody.find_all('p')

    text_PII = "\n\n".join([p.get_text() for p in text_p_elements if not p.find('a')])


    # print(name)
    # print(roles)
    # print()
    # print(email_text)
    # print(phone_text)
    # print()
    # print( )

    data_save = {
        'Names' : name,
        'Roles' : roles,
        'Titles' : title.replace(roles,'').replace('-','').strip(),
        'Email': email_text,
        'Phone': phone_text,
        'PII': text_PII.strip(),
    }

    data.append(data_save)
    print('Saving', data_save['Names'])
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)