import csv
import requests
from bs4 import BeautifulSoup

baseurl = 'https://fsaseychelles.sc/regulated-entities/capital-markets#tab-investment-advisor'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.79'
}

fields = ['Name' , 'Company Name', 'Phone Number', 'Email', 'Address','List Name']
filename = '90.1194.csv'
data = []

r = requests.get(baseurl, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

panelGroups = soup.find_all('div', class_='panel-group')[6]

for panelGroup in panelGroups:
    cardItem = panelGroup.find_all('div', class_='card')
    
    for cardItem in cardItem:
        company_name = cardItem.find('h5', class_='mb-0').text.strip()

        try:
            user = cardItem.find('span', class_='fas fa-user-tie')
            name = user.find_next_sibling(string=True).strip().strip()
        except:
            user =  ''
            name = ''

        try:
            fa_fa_map = cardItem.find('span', class_='far fa-file-alt')
            address = fa_fa_map.find_next_sibling(string=True).strip().strip().replace('Local Contact:', ',   ')
        except:
            fa_fa_map =  ''
            address = ''

        try:
            fa_fa_phone = cardItem.find('span', class_='fa fa-phone')
            phone_element = fa_fa_phone.find_next_sibling('a')
            phone_number = phone_element.get_text()
        except:
            fa_fa_phone = ''
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
            for unwanted_element in card_body_element.select('p, h5, span.fa.fa-mobile, span.fas fa-user-tie, a'):
                unwanted_element.extract()
            all_text = card_body_element.get_text()
            bd_text = ""
            overseas_Contact_elements = card_body_element.find_all('p', class_='bd')
            for overseasContact in overseas_Contact_elements:
                bd_text += overseasContact.get_text()
            overseas_Contact = all_text.replace(bd_text, '').strip()      
        else:
            overseas_Contact = ''


        data_90_1194 = {
            'Name': name,
            'Company Name': company_name,
            'Phone Number': phone_number,
            'Email': email,
            'Address': 'Local Contact: ' + address + overseas_Contact ,
            # 'Overseas Contact': overseas_Contact,
            'List Name': 'Investment Advisor'
        }


        data.append(data_90_1194)
        print('Saving', data_90_1194['Name'])
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            writer.writerows(data)
        


    
        

