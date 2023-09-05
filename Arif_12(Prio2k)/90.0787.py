import requests
from bs4 import BeautifulSoup
import csv
import time

url = 'https://www.mcci.org/en/membership/members-directory/?alph=All#pos'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69'
}

data = []

fields = ['Names' , 'Company Name' , 'Tel' , 'Fax' , 'Email' , 'Website' ,'Description', 'Address' , 'Brand Name', 'Titles']
filename = '90.0787.csv'

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')
time.sleep(.5)
find_item = soup.find_all('div', class_='offer', id='offernew')

for info in find_item:

    title = info.find('div', class_='offercat').text.strip()
    companyName = info.find('div', class_='offertxtt').text.strip()
    time.sleep(.5) 

    try:
        name = info.find('div', class_='offerpep').text.strip()
    except:
        name = ''

    try:
        address = info.find('div', class_='offermap').text.strip()
    except:
        address = ''

    try:
        desc_element = info.find('div', class_='alltxt').text.strip()
    except:
        desc_element = ''       

    try:
        brand = info.find('p', id='brand').text.strip()
    except:
        brand = ''

    try:
        tel = info.find('div', class_='offertel').text.strip()
    except:
        tel = ''

    try:
        fax = info.find('div', class_='offerfaxx').text.strip()
    except:
        fax = ''

    try:
        email = info.find('a', class_='offeremail').text.strip()
    except:
        email = ''

    try:
        website = info.find('a', class_='offerweb').text.strip()
    except:
        website = ''
    
    time.sleep(.5)

    data_save = {
        'Names' : name,
        'Company Name' : companyName,
        'Brand Name' : brand,
        'Address' : address,
        'Tel' : tel,
        'Fax' : fax,
        'Email' : email,
        'Website' : website,
        'Description' : desc_element.replace('Year Established','Year Established\n').replace('Lines','\n\nLines\n').replace('Brand Name','').replace(brand,'').strip(),
        'Titles' : title,
    }
    data.append(data_save)
    print('Saving', data_save['Names'])
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)


