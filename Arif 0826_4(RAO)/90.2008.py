import requests
from bs4 import BeautifulSoup
import csv
import re

url = 'https://www.cubatramite.com/entidades-exportadoras-e-importadoras/'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.54'
}

fields = ['Company Name' , 'Phone / Telefono' , 'Mobile Number / Movil' , 'Email' , 'Web / Site URL' , 'Description']
filename = '90.2008.csv'


data = []


r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

find_inside_article = soup.find('div', class_='inside-article')


title_ = find_inside_article.find_all('h3', class_='wp-block-heading')
for strong_ in title_:
    title = strong_.find('strong').text.strip()
    # print(title)


# site_urls = []



h3_elements = find_inside_article.find_all('h3', class_='wp-block-heading')

for h3 in h3_elements:
    title = h3.get_text()
    email_ = ""
    siteUrl = ""
    phone = ""
    movil = ""
    disc__ = []  # Using a list to store multiple descriptions
    ul_sibling = h3.find_next_sibling('ul')
    text_disc = ul_sibling.text  
    if ul_sibling:
        li_elements = ul_sibling.find_all('li')
        for li in li_elements:
            disc__.append(li.text.strip())  # Append each description to the list
            disc = li.text.strip()

            if "www" in disc:
                siteUrl = disc
            
            if "Email" in disc:
                email_ = disc

            if "Teléfono" in disc:
                phone = disc

            if "Móvil" in disc:
                movil = disc

    company_Name =  title
    emaiL_ = email_.replace('\n', '').replace('Email:','').strip()
    phone_numnber = phone.replace('\n', '').replace('Teléfono:','').strip()
    mobile_Number_Movil =  movil.replace('\n', '').replace('Móvil:','').strip()
    web_SiteURL = siteUrl.replace('\n', '').replace('Web:','').strip()

    all_descriptions = "\n".join(disc__)
    # Replace email, siteUrl, and phone in the joined descriptions
    cleaned_descriptions = all_descriptions.replace(email_, '').replace(siteUrl, '').replace(phone, '').replace(movil,'').replace('\n', '\n').strip()
    # print("Description:", cleaned_descriptions)
    # print()

    data_save = {
        'Company Name' : company_Name,
        'Phone / Telefono' : phone_numnber,
        'Mobile Number / Movil' : mobile_Number_Movil,
        'Email': emaiL_,
        'Web / Site URL' : web_SiteURL,
        'Description' : text_disc.replace(email_, '').replace(siteUrl, '').replace(phone, '').replace(movil,'').replace('\n', '\n\n')
    }
    data.append(data_save)
    print('Saving', data_save['Company Name'],  data_save['Description'], data_save['Mobile Number / Movil'])
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)
