import csv
import requests
from bs4 import BeautifulSoup

baseurl = 'https://fsaseychelles.sc/regulated-entities/insurance'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.79'
}

fields = ['Name' ,'Company Name', 'Phone Number' , 'Fax Number' , 'Email' , 'Address', 'List Name']
filename = '90.1186.csv'
data = []

r = requests.get(baseurl, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

panelGroups = soup.find_all('div', class_='panel-group')[5]

for panelGroup in panelGroups:
    cardItem = panelGroup.find_all('div', class_='card')
    
    for cardItem in cardItem:
        company_name = cardItem.find('h5', class_='mb-0').text.strip()
        # print(name)
        try:
            fas_fa_user_tie = cardItem.find('span', class_='fas fa-user-tie')
            name_of_the_person = fas_fa_user_tie.find_next_sibling(string=True).strip()
            # name_of_the_person = user.get_text()
        except:
            fas_fa_user_tie = ''
            # user = ''
            name_of_the_person =  ''

        try:
            fafamobile = cardItem.find('span', class_='fa fa-phone')
            phone_element = fafamobile.find_next_sibling('a')
            phone_number = phone_element.get_text()
        except:
            phone_element = ''
            phone_number =  ''

        try:
            facfafamobile = cardItem.find('span', class_='fa fa-fax')
            fax_element = facfafamobile.find_next_sibling('a')
            fax = fax_element.get_text()
        except:
            fax_element = ''
            fax =  ''

        try:
            fafaenvelope = cardItem.find('span', class_='fa fa-envelope')
            email_ = fafaenvelope.find_next_sibling('a')
            email = email_.get_text()
        except:
            email_ = ''
            email =  ''


        card_body_element = cardItem.find('div', class_='card-body')
        if card_body_element:
            for unwanted_element in card_body_element.select('p, h5, span.fa.fa-mobile, span.fas fa-user-tie, a'):
                unwanted_element.extract()
            all_text = card_body_element.get_text()
            bd_text = ""
            addres_elements = card_body_element.find_all('p', class_='bd')
            for addres_element in addres_elements:
                bd_text += addres_element.get_text()
            addres = all_text.replace(bd_text, '').strip()            
        else:
            addres = ''

        data_90_1186 = {
            'Name' : name_of_the_person,
            'Company Name' : company_name,
            'Phone Number' : phone_number,
            'Fax Number' : fax,
            'Email' : email,
            'Address' : addres,
            'List Name': 'Non-Domestic Insurer'
        }

        data.append(data_90_1186)
        print('Saving', data_90_1186['Company Name'])
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            writer.writerows(data)
        


    
        

