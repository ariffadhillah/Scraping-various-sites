import csv
import requests
from bs4 import BeautifulSoup
import re

baseurl = 'https://sifa.ws/professionals/banks/'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82'
}

fields = ['Banks Name', 'Tel', 'Fax', 'Email', 'Website','Address']
filename = '90.1546.csv'
data = []

r = requests.get(baseurl, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

content_container = soup.find('div', class_='content-container')

elements_text = content_container.select('h3')
bank_name_elements = content_container.select('h3 strong')

for i in range(len(elements_text)):
    h3element = elements_text[i]
    bank_name = bank_name_elements[i].get_text() if i < len(bank_name_elements) else ""

    p_elements = h3element.find_next_sibling('p')
    if p_elements:
        text_ = p_elements.text.strip()

        tel_search = re.search(r'Tel: \((\+\d+)\) (\d+)', text_)
        fax_search = re.search(r'Fax: \((\+\d+)\) (\d+)', text_)
            
        tel = f"{tel_search.group(1)} {tel_search.group(2)}" if tel_search else ""
        fax = f"{fax_search.group(1)} {fax_search.group(2)}" if fax_search else ""

        email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
        found_emails = set(re.findall(email_pattern, text_))

        email = ""
        siteUrl = ""

        for email_ in found_emails:
            email = email_

        for siteURL in p_elements.find_all('a', {'target':'_blank'}):            
            siteUrl = siteURL['href']

    addres = p_elements
    # print(addres)

    data_90_1546 = {
        'Banks Name': bank_name,
        'Email': email.replace('Website',''),
        'Tel': tel,
        'Fax': fax,            
        'Address': addres.text.replace(email,'').replace(siteUrl,'').replace(tel,'').replace(fax, ''),
        'Website': siteUrl
    }
    data.append(data_90_1546)
    print('Saving', data_90_1546['Banks Name'])
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)

