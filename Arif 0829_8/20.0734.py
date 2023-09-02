import requests
from bs4 import BeautifulSoup
import csv
import re

url = 'https://wellington.govt.nz/your-council/about-the-council/mayor-and-councillors/office-of-the-mayor'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62'
}

data = []

fields = ['Names', 'Roles','Email','PII']
filename = '20.0734.csv'

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

find_item = soup.find_all('a', {'class':['link-block pb--s landing-item landing-item-imageless','link-block pb--s landing-item']})
indexes_to_display = [0, 1]

urlBio = []

for indexhrefBio in indexes_to_display:
    if indexhrefBio < len(find_item):
        urlBio.append('https://wellington.govt.nz'+find_item[indexhrefBio]['href'])

for item_url in urlBio:
    r = requests.get(item_url, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    h1_element = soup.find('h1', class_='pt--s mb--xs')

    if h1_element:
        # Menghapus elemen <span> dari elemen <h1>
        for span_name in h1_element.find_all('span'):
            span_name.decompose()
        
        # Mengambil teks dari elemen <h1> setelah menghapus elemen <span>
        name = h1_element.get_text(strip=True)
        
    roles = soup.find('p', class_='type-introduction').text.strip()

    div_richtext_text = soup.find('figure', {'class':['richtext__image richtext__image-floatleft','richtext__image richtext__image-leftwithoutenlargement']})

    if div_richtext_text:
        sibling_figcaption = div_richtext_text.find_next_sibling('div', class_='richtext__text')
        
        if sibling_figcaption:
            textsibling = sibling_figcaption
            # desc = soup.find('div', class_='rich-text-wrapper')
            text_p_elements = textsibling.find_all('p')

            text_PII = "\n\n".join([p.get_text() for p in text_p_elements if not p.find('a')])

    email_siblings = soup.find_all(['strong', 'th'], string=['Email:', 'Email'])

    for sibling in email_siblings:
        next_sibling = sibling.find_next_sibling()
        if next_sibling:
            if next_sibling.name == 'a':
                email = next_sibling.get('href').replace('mailto:', '')
                # print("Email:", email)
            elif next_sibling.name == 'td':
                email = next_sibling.get_text(strip=True)
                # print("Email:", email)

        # print(name, email)        
        # print(text_PII)
        # print()
        # print()
        # print()
        # print()
        # print()

    data_save = {
        'Names' : name,
        'Roles' : roles,
        'Email': email,
        'PII': text_PII,
    }

    data.append(data_save)
    print('Saving', data_save['Names'])
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)