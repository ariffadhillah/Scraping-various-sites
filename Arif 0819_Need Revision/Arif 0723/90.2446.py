import requests
from bs4 import BeautifulSoup
import csv
import re

baseurl = 'https://www.bcu.gub.uy/Servicios-Financieros-SSF/Paginas/casas_Financieras_Lst.aspx'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183',
    'Cookie': '_ga=GA1.2.1612263739.1690160978; _gid=GA1.2.1850555160.1690160978; PHPSESSID=ob3t846ajr7fqq5ob29321e605; _gat=1; _ga_NCKWVCM59T=GS1.2.1690244101.3.0.1690244101.0.0.0'
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
                
                data_90_2446 = {
                    'Name' : name,
                    'Personal Superior' : title,
                    'Company Name' : companyName,
                    'Link Page' : detailsPage
                }

                data.append(data_90_2446)
                print('Saving', data_90_2446['Name'])

                fields = ['Name', 'Personal Superior' , 'Company Name' , 'Link Page']
                filename = '90.2446.csv'

                with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=fields)
                    writer.writeheader()
                    writer.writerows(data)
                    
    except:
        companyName = ''
        find_tables = ''








