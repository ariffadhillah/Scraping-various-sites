import requests
from bs4 import BeautifulSoup
import csv
import re

baseurl = 'https://www.bcu.gub.uy/Servicios-Financieros-SSF/Paginas/fudi_Prof.aspx'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183',
    'Cookie': 'ckpersistweb-20480=ENBEABAKFAAA; _gid=GA1.3.2137570847.1690193291; WSS_FullScreenMode=false; _ga=GA1.3.301577954.1690193289; _gat_gtag_UA_32096954_1=1; _ga_M4Q8MD19NL=GS1.1.1690380766.9.1.1690386334.0.0.0'
}

r = requests.get(baseurl, headers=headers, verify=False)
soup = BeautifulSoup(r.content, 'lxml')

data = []

search_table = soup.find('table', class_='ms-listviewtable')
listItems = search_table.find_all('td', class_='ms-vb2')

url = []

for item in listItems:
    a_tag = item.find('a', onclick ='')
    if a_tag:
        href = a_tag.get('href')
        url.append('https://www.bcu.gub.uy' + href)

name = ''
title = ''

for detailsPage in url:
    r = requests.get(detailsPage, headers=headers , verify=False)
    soup = BeautifulSoup(r.content, 'lxml')

    try:

        companyName = soup.find('span', class_='BCU_form_label').text.strip()

        find_tables = soup.find_all('table', {'id': ['lstAdministracion', 'lstDirectorio', 'lstSindicatura']})

        for item in find_tables:
            names = item.find_all('span', class_='dirnombre')
            title_staff = item.find_all('span', class_='dircargo')

            for name_, title_ in zip(names, title_staff):
                name = name_.text
                title = title_.text
                
                data_90_2454 = {
                    'Name' : name,
                    'Personal Superior' : title,
                    'Company Name' : companyName,
                    'Link Page' : detailsPage
                }

                data.append(data_90_2454)
                print('Saving', data_90_2454['Name'])

                fields = ['Name', 'Personal Superior' , 'Company Name' , 'Link Page']
                filename = '90.2454.csv'

                with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=fields)
                    writer.writeheader()
                    writer.writerows(data)


    except:
        companyName = ''
        find_tables = ''







