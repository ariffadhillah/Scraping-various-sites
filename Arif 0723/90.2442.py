import requests
from bs4 import BeautifulSoup
import csv
import re

baseurl = 'https://www.bancocentral.tl/en/go/financial-institution'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183',
    'Cookie': '_ga=GA1.2.1612263739.1690160978; _gid=GA1.2.1850555160.1690160978; PHPSESSID=ob3t846ajr7fqq5ob29321e605; _gat=1; _ga_NCKWVCM59T=GS1.2.1690244101.3.0.1690244101.0.0.0'
}

r = requests.get(baseurl, headers=headers, verify=False)
soup = BeautifulSoup(r.content, 'lxml')



data = []

def clean_text(text):
    return re.sub(r'\s+', ' ', text.strip())


search_name_banks = soup.find_all('a', class_='documento-cat-link documento-left')
search_table_bank = soup.find_all('div', class_='documentos-cat-body hide')

if len(search_name_banks) == len(search_table_bank):
    for bank, table_bank in zip(search_name_banks, search_table_bank):
        name_banks = bank.text.strip().upper()
        search_table = table_bank.find('table')
        if search_table:
            # Inisialisasi variabel sebelum memproses baris dan kolom
            license_number = ''
            license = ''
            license__ = ''
            license___ = ''
            street_address = ''
            _address = ''
            address = ''
            number_of_mto = ''
            name_of_mto = ''
            telephone = ''
            phone =''
            phone_number =''
            telefax = ''
            swift_code = ''
            email = ''
            email_ = ''
            e_mail = ''
            home_page_ = ''
            _home_page = ''
            date_ = ''
            mobile_number = ''
            site_url = ''
            website_ = ''
            website = ''
            skype = ''
            operatting_office = ''
            director = ''
            facsimile = ''
            ceo = ''
            number_of_ceb = ''
            operating_office = ''
            country_Head =''
            managing_Director = ''
            decision_ =''
            


            rows = search_table.find_all('tr')
            for row in rows:
                columns = row.find_all('td')
                for col in columns:                   
                    if col.text.strip() == "LICENSE NUMBER":
                        license_number = col.find_next('td').text.strip()
                    if col.text.strip() == "LICENSE Nº":
                        license = col.find_next('td').text.strip()

                    if col.text.strip() == "LICENCE\xa0Nº":
                        license__ = col.find_next('td').text.strip()
                        # print(license__)
                    col_text = clean_text(col.text)
                    if col_text == "License Number" or col_text == "License Number \xa0 \xa0 \xa0 \xa0 \xa0 \xa0 \xa0 \xa0 \xa0\xa0":
                        license___ = col.find_next('td').text.strip()
                        # print("Nomor Lisensi:", license___)

                    if col.text.strip() == "Decision":
                        decision_ = col.find_next('td').text.strip()
                    no_license = license_number if license_number else "" + license if license else "" + license___ if license___ else "" + license__ if license__ else "" + decision_ if decision_ else ""

                    if col.text.strip() == "TELEPHONE":
                        telephone = col.find_next('td').text.strip()
                    if col.text.strip() == "Phone":
                        phone = col.find_next('td').text.strip()
                    phone_number = telephone if telephone else "" + phone if phone else ""

                    if col.text.strip() == "TELEFAX":
                        telefax = col.find_next('td').text.strip()

                    if col.text.strip() == "SWIFT CODE":
                        swift_code = col.find_next('td').text.strip()

                    if col.text.strip() == "EMAIL":
                        email_ = col.find_next('td').text.strip()
                    if col.text.strip() == "E-MAIL":
                        e_mail = col.find_next('td').text.strip()
                    email = email_ if email_ else " " + e_mail if e_mail else " "

                    if col.text.strip() == "WEBSITE":
                        website_ = col.find_next('td').text.strip()
                    if col.text.strip() == "Website":
                        site_url = col.find_next('td').text.strip()
                    website = website_ if website_ else " " + site_url if site_url else " "

                    if col.text.strip() == "Skype":
                        skype = col.find_next('td').text.strip()

                    if col.text.strip() == "Chief Executive Officer (CEO)":
                        ceo = col.find_next('td').text.strip()

                    if col.text.strip() == "HOME PAGE":
                        home_page_ = col.find_next('td').text.strip()
                    if col.text.strip() == "Home Page":
                        _home_page = col.find_next('td').text.strip()                
                    homepage = home_page_ if home_page_ else " " + _home_page if _home_page else " "

                    if col.text.strip() == "NUMBER OF MTO":
                        number_of_mto = col.find_next('td').text.strip()

                    if col.text.strip() == "NAME OF MTO":
                        name_of_mto = col.find_next('td').text.strip()

                    if col.text.strip() == "DATE":
                        date_ = col.find_next('td').text.strip()

                    if col.text.strip() == "MOBILE NUMBER":
                        mobile_number = col.find_next('td').text.strip()

                    if col.text.strip() == "OPERATING OFFICE":
                        operatting_office = col.find_next('td').text.strip()

                    if col.text.strip() == "DIRECTOR":
                        director = col.find_next('td').text.strip()

                    if col.text.strip() == "NUMBER OF CEB":
                        number_of_ceb = col.find_next('td').text.strip()

                    if col.text.strip() == "FACSIMILE":
                        facsimile = col.find_next('td').text.strip()

                    if col.text.strip() == "Country Head":
                        country_Head = col.find_next('td').text.strip()

                    if col.text.strip() == "Managing Director":
                        managing_Director = col.find_next('td').text.strip()

                    if col.text.strip() == "STREET ADDRESS":
                        street_address = col.find_next('td').text.strip()
                    if col.text.strip() == "ADDRESS":
                        _address = col.find_next('td').text.strip()
                    if col.text.strip() == "Address":
                        address_ = col.find_next('td').text.strip()
            address =  street_address if street_address else " " + _address if _address else " " + address_ if address_ else " " 

            data_90_2442 = {
                'Companies Name' : name_banks,
                'License Number' : no_license,
                'Date': date_,
                'Facsimile': facsimile,
                'Street Address' : address,
                'Telephone' : phone_number,
                'Mobile Number' : mobile_number,
                'Telefax' : telefax,
                'Swift Code' : swift_code,
                'Email' : email,
                'Website' : website + homepage,
                'Skype' : skype,
                'Chief Executive Officer (CEO)' : ceo,
                'Country Head' : country_Head,
                'Director': director,
                # 'NUMBER OF CEB' :number_of_ceb,
                'OPERATING OFFICE': operatting_office
            }
            data.append(data_90_2442)
            print('Saving', data_90_2442['Companies Name'])

    # Write the data to a CSV file
    fields = ['Companies Name', 'License Number' ,'Date' , 'Swift Code' , 'Telephone' , 'Mobile Number' , 'Telefax' , 'Facsimile' , 'Email' ,  'Website' , 'Skype' , 'Chief Executive Officer (CEO)' , 'Country Head' , 'Director' , 'OPERATING OFFICE','Street Address'] 
    filename = '90.2442.csv'

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)


else:
    print(" ")