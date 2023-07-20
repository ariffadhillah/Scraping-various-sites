import csv
import requests
from bs4 import BeautifulSoup

baseurl = 'https://fsaseychelles.sc/regulated-entities/capital-markets#tab-investment-advisor'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.79'
}

fields = ['Name' ,'Securities Dealer accredited','Phone Number', 'Mobile Number', 'List Name']
filename = '90.1193.csv'
data = []

r = requests.get(baseurl, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

panelGroups = soup.find_all('div', class_='panel-group')[4]

for panelGroup in panelGroups:
    cardItem = panelGroup.find_all('div', class_='card')
    
    for cardItem in cardItem:
        name_of_the_person = cardItem.find('h5', class_='mb-0').text.strip()

        try:
            securitiesDealerAccredited_ = cardItem.find('span', class_='far fa-file-alt')
            securities_Dealer_accredited = securitiesDealerAccredited_.find_next_sibling(string=True).strip().replace('Securities Dealer accredited with:','').replace('Securities Dealers Representative accredited with:','').replace('Securities Dealer Representative accredited with:','').replace("Securities Dealer's Representative accredited with:",'').replace("Securities Dealer Representative with:",'').replace("Securities Dealer Accredited with:",'').replace("Securities Dealer Representative accredited with",'')
            
        except:
            securitiesDealerAccredited_ = ''            
            securities_Dealer_accredited =  ''

        try:
            securitiesDealerAccredited_1 = cardItem.find('span', class_='fas fa-user-tie')
            securities_Dealer_accredited_ = securitiesDealerAccredited_1.find_next_sibling(string=True).strip().replace('Securities Dealer accredited with:','').replace('Securities Dealer Representative accredited with','')
            
        except:
            securitiesDealerAccredited_1 = ''            
            securities_Dealer_accredited_ =  ''

        try:
            fa_fa_map = cardItem.find('span', class_='fa fa-map')
            map_dealer = fa_fa_map.find_next_sibling(string=True).strip().strip().replace('Securities Dealer accredited with:','')
            
        except:
            fa_fa_map =  ''
            map_dealer = ''            
 
        try:
            fa_faskype = cardItem.find('span', class_='fa fa-skype')
            faskype = fa_faskype.find_next_sibling(string=True).strip().replace('Securities Dealer accredited with:','').replace('Securities Dealer accredited with:','')
            
        except:
            fa_faskype =  ''
            faskype = ''            

        try:
            fa_fa_phone = cardItem.find('span', class_='fa fa-phone')
            phone_element = fa_fa_phone.find_next_sibling('a')
            phone_number = phone_element.get_text()
        except:
            fa_fa_phone = ''
            phone_number =  ''

        try:
            fa_fa_mobile = cardItem.find('span', class_='fa fa-mobile')
            mobile_element = fa_fa_mobile.find_next_sibling('a')
            mobile_number = mobile_element.get_text()
        except:
            mobile_element = ''
            mobile_number =  ''

        data_90_1193 = {
            'Name': name_of_the_person,
            'Securities Dealer accredited':faskype + map_dealer + securities_Dealer_accredited + securities_Dealer_accredited_.replace(name_of_the_person, ''),
            'Phone Number': phone_number,
            'Mobile Number': mobile_number,
            'List Name': 'Securities Dealer Representative'
        }


        data.append(data_90_1193)
        print('Saving', data_90_1193['Name'])
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            writer.writerows(data)
        


    
        

