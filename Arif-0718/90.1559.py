import csv
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd


def decode_email(encoded_email):
    email = ""
    key = int(encoded_email[:2], 16)

    for i in range(2, len(encoded_email)-1, 2):
        char_code = int(encoded_email[i:i+2], 16) ^ key
        email += chr(char_code)

    return email


baseurl = 'https://www.bursamalaysia.com/listing/lfx/listing_sponsors_list'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82',
    'Cookie':'_locomotiveapp_session=L21Sa1JvZFJtakZyaVF6ZW5BcUV2N2h6eXl4RzFPcklmY1FDc0MxL3I4V0R0dU9qUTd3VzhsdytGS1NveXFlSTNBalFUOXFxZnovdE5MMzZkK2ppZDU3U1lZYkg0aWlyOWhYNEdRa0IwR2p5RDhWSDc5TkJrWXJ1L3JjTTMwNFUyRnZ2UjZWRld0cVIvUCt5Vmc5UmFBPT0tLWQybUQ0Y3QrRmk1TlB6SGJLUHgvbUE9PQ%3D%3D--f9be5a6564d1343d8f4e9872b1b965d1b646d686; path=/; HttpOnly;Secure;'
}

fields = ['Bank Name', 'Licence No', 'Telephone No', 'Fax No',  'Contact Person', 'Email', 'Website', 'Address']
filename = '90.1559.csv'
data = []

r = requests.get(baseurl, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

search_list = soup.find('div', id='content-col')
item_ = search_list.find_all('div', class_='col')

for item in item_:
    license_ = item.find_all('strong')[0]
    licenceNo =  license_.text.replace('Licence No. : ', '')
    
    nameBank_ = item.find_all('strong')[1]
    nameBank =  nameBank_.text
    
    telephone_label = item.find(string=re.compile(r'Telephone No.'))
    telephone = telephone_label.replace('Telephone No. : ','')    

    fax_label = item.find(string=re.compile(r'Fax No.'))
    fax = fax_label.replace('Fax No. : ','')
 
    contactPerson_label = item.find(string=re.compile(r'Contact Person'))
    contact_Person = contactPerson_label.replace('Contact Person : ','')
    # print(contact_Person)    

    email_label = item.select_one('span.__cf_email__')
    if email_label:
        email = decode_email(email_label['data-cfemail'])
    else:
        email = ""
    
    website_label = item.find('a', href=lambda href: href and href.startswith('http://'))
    if website_label:
        website = website_label['href']
    else:
        website = ""
    
    address = item.text.replace(website,'').replace(email,'').replace(fax,'').replace(telephone,'').replace(nameBank,'').replace(licenceNo,'').replace('Website','').replace(':','').replace('Email','').replace('Fax No. ','').replace('Licence No.  ','').replace('Contact Person  ','').replace('Telephone No.','').strip().replace('  ',' ').replace('[','').replace(']','').replace('email','').replace('protected','').replace(contact_Person,'')
    
    data_90_1559 = {
        'Bank Name': nameBank,
        'Licence No': licenceNo,
        'Telephone No' : telephone,
        'Fax No' : fax,
        'Contact Person': contact_Person,
        'Email' : email,
        'Website': website,
        'Address':  address,
    }
    data.append(data_90_1559)
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)

print(f"Save to {filename}")

        

