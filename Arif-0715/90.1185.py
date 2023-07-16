import csv
import requests
from bs4 import BeautifulSoup

baseurl = 'https://fsaseychelles.sc/regulated-entities/insurance'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.79'
}

fields = ['Name', 'Phone Number', 'Email', 'Address', 'List Name']
filename = '90.1185.csv'
data = []

r = requests.get(baseurl, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

panelGroups = soup.find_all('div', class_='panel-group')[4]

for panelGroup in panelGroups:
    cardItem = panelGroup.find_all('div', class_='card')
    
    for cardItem in cardItem:
        name = cardItem.find('h5', class_='mb-0').text.strip()
        # print(name)
        try:
            fafamobile = cardItem.find('span', class_='fa fa-phone')
            phone_element = fafamobile.find_next_sibling('a')
            phone_number = phone_element.get_text()
        except:
            phone_element = ''
            phone_number =  ''

        try:
            fafaenvelope = cardItem.find('span', class_='fa fa-envelope')
            email_ = fafaenvelope.find_next_sibling('a')
            email = email_.get_text()
        except:
            email_ = ''
            email =  ''


        card_body_element = cardItem.find('div', class_='card-body')
        if card_body_element:
            for unwanted_element in card_body_element.select('p, h5, span.fa.fa-mobile, a'):
                unwanted_element.extract()
            all_text = card_body_element.get_text()
            bd_text = ""
            addres_elements = card_body_element.find_all('p', class_='bd')
            for addres_element in addres_elements:
                bd_text += addres_element.get_text()
            addres = all_text.replace(bd_text, '').strip()            
        else:
            addres = ''

        # print(name, addres,phone_number, addres, email)


        data_90_1185 = {
            'Name' : name,
            'Address' : addres,
            'Phone Number' : phone_number,
            'Email' : email,
            'List Name': 'Domestic Insurer'
        }

        data.append(data_90_1185)
        print('Saving', data_90_1185['Name'])
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            writer.writerows(data)
        


    
        

