import requests
from bs4 import BeautifulSoup
import csv
import time

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69'
}

data = []

fields = ['Company Name' , 'REGAFI Identifier' , 'Trade Name' , 'SIREN or Unique Identification Number' , 'LEI' , 'Bank Code' , 'Category' , 'Institution Type' , 'Status' ]
filename = '90.0520.csv'

base_url = 'https://www.regafi.fr/spip.php?page=results&type=advanced&id_secteur=3&lang=en&denomination=&siren=&cib=&bic=&nom=&siren_agent=&num=&cat=42-TBR07&retrait=0'


page = 1
max_page = 1
while page <= max_page:
    time.sleep(2)    
    url  = f"{base_url}&pg={page}"
    print(url)

    time.sleep(1)
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    find_table = soup.find('table', {'summary':'Search results'}, class_='table')

    time.sleep(1)
    for find_tr in find_table.find_all('tr')[1:]:
        find_td = find_tr.find_all('td')
        if find_td:
            identifiantREGAFI = find_td[0].text
            companyName = find_td[1].text
            tradename = find_td[2].text
            siren_or_unique_identification_number = find_td[3].text
            lEI_ = find_td[4].text
            bank_code = find_td[5].text
            category = find_td[6].text
            type_Establishment = find_td[7].text
            nature_of_exercise = find_td[8].text



            data_save = {
                'Company Name' : companyName,
                'REGAFI Identifier' : identifiantREGAFI,
                'Trade Name' : tradename,
                'SIREN or Unique Identification Number' : siren_or_unique_identification_number,
                'LEI' : lEI_,
                'Bank Code' : bank_code,
                'Category' : category,
                'Institution Type' : type_Establishment,
                'Status' : nature_of_exercise
            }
            time.sleep(.5)
            data.append(data_save)
            print('Saving', data_save['Company Name'])
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fields)
                writer.writeheader()
                writer.writerows(data)
            
    page += 1