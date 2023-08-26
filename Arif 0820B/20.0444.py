import requests
from bs4 import BeautifulSoup
import csv
import re
import time


url = 'https://www.chicago.gov/city/en/about/wards.html'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203'
}

fields = ['Names', 'Roles', 'Titles' , 'Ward Office' , 'Phone' , 'Fax' , 'Email' , 'City Hall Office' ]
filename = '20.0444.csv'

data = []

list_item = []
processed_urls = set()

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

time.sleep(.5)

find_item = soup.find_all('div', class_='col-12')[4]
element_h4 = find_item.find_all('h4')
for info_h4 in element_h4:
    find_href = info_h4.find('a', href=True)
    link_details = 'https://www.chicago.gov' + find_href['href']

    if link_details not in processed_urls:
        list_item.append(link_details)
        processed_urls.add(link_details)

for page_details in list_item:
    r = requests.get(page_details, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    print(page_details)

    find_section = soup.find('div', class_='row page-description my-3')

    names = find_section.find('h3').text.replace('Alderman','').strip()
    name = names
    title = soup.find('h1', class_='page-heading').text.strip()

    roles = find_section.find('h3').text.replace(name,'').strip()

    ward_office_element = soup.find(['td','p'], string='Ward Office:')
    if ward_office_element:
        ward_office_text = ward_office_element.find_next('td').get_text(separator=' ').strip()

    email_element = soup.find(['td','p'], string='Email:')
    if email_element:
        email_text = email_element.find_next('td').get_text(separator=' ').strip()

    
    # fax_elements = soup.find_all('td', string='Fax:')
    # for fax_element in fax_elements:
    #     fax_text = fax_element.find_next('td').get_text(separator=' ').strip()
    fax_elements = soup.find_all('td', string='Fax:')
    fax_texts = []

    for fax_element in fax_elements:
        fax_sibling = fax_element.find_next('td')
        if fax_sibling:
            fax_text = fax_sibling.get_text(separator=' ').strip()
            fax_texts.append(fax_text)
        else:
            fax_texts.append("")

    # Menggabungkan teks fax_texts jika perlu
    combined_fax_text = ' , '.join(fax_texts)
    fax_number = combined_fax_text


    phone_elements = soup.find_all(['td', 'p'], string='Phone:')
    phone_texts = []

    for phone_element in phone_elements:
        phone_text = phone_element.find_next('td').get_text(separator='  ,  ').strip()
        phone_texts.append(phone_text)

    combined_phone_text = '  ,  '.join(phone_texts)
    # print(combined_phone_text)

    city_Hall_Office_element = soup.find(['td','p'], string='City Hall Office:')
    if city_Hall_Office_element:
        city_Hall_Office_text = city_Hall_Office_element.find_next('td').get_text(separator=' ').strip()


    # print(fax_text)
    # print(name)
    # print(roles)
    # print(title)
    # print(ward_office_text.strip())
    # print(email_text)
    
    # print(combined_phone_text.replace('  ,  ,  ','  ,  '))
    # print(city_Hall_Office_text)
    # print( )
    # print( )

    data_save = {
        'Names' : name,
        'Roles' : roles, 
        'Titles' : title, 
        'Ward Office' : ward_office_text.strip(), 
        'Phone' : combined_phone_text.replace('  ,  ,  ','  ,  '),
        'Fax' :  fax_number,
        'Email' : email_text,
        'City Hall Office' : city_Hall_Office_text,
    }

    data.append(data_save)
    print('Saving', data_save['Names'], data_save['Fax'])
    print( ' ')
    # # # Menulis data ke file CSV setelah selesai looping
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)
