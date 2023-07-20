import csv
import requests
from bs4 import BeautifulSoup
import re

baseurl = 'https://sifa.ws/professionals/other-services/'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82'
}

fields = ['Banks Name', 'Tel', 'Email', 'Instagram', 'Description']
filename = '90.1547.csv'
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
        instagram_search = re.search(r'Instagram page:(.+) ', text_)

        tel = f"{tel_search.group(1)} {tel_search.group(2)}" if tel_search else ""
        instagram = instagram_search.group(1) if instagram_search else ""

        email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
        found_emails = set(re.findall(email_pattern, text_))

        email = ""

        for email_ in found_emails:
            email = email_

        description = p_elements.get_text().replace(email, '').replace(instagram, '')

        data_90_1547 = {
            'Banks Name': bank_name,
            'Email': email.strip().replace('Tel',''),
            'Tel': tel.strip(),
            'Instagram': instagram.strip(),
            'Description': description.strip()
        }
        data.append(data_90_1547)
        print('Saving', data_90_1547['Banks Name'])

# Write all the data to a CSV file
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(data)

