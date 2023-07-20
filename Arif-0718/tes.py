import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.advokatsamfundet.se/Advokatsamfundet-engelska/Find-a-lawyer/Search-result/Person-details/?personid=1795'
# url = 'https://www.advokatsamfundet.se/Advokatsamfundet-engelska/Find-a-lawyer/Search-result/Person-details/?personid=3047'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'html.parser')

name = soup.find('h1', class_='hero-heading -black -person').text.strip()
title = soup.find('div', class_='hero-preamble').text.strip()

phone_numbers = []
email = ''
site = ''

personalinfo = soup.find_all('div', class_='Section-content')[0]
sibling_contact = personalinfo.find('div', string='Contact')

if sibling_contact:
    post_text_div = sibling_contact.find_next_sibling('div', class_='post-text')
    if post_text_div:
        div_elements = post_text_div.find_all('div')

        phone_numbers = [div.get_text(strip=True) for div in div_elements if re.match(r'\b\d{2,4}[-\s]?\d{2,4}[-\s]?\d{2,4}\b', div.get_text(strip=True))]
        
        for div in div_elements:
            email_tag = div.find('a', href=lambda href: href and href.startswith('mailto:'))
            site_tag = div.find('a', href=lambda href: href and not href.startswith('mailto:'))
            if email_tag:
                email = email_tag['href'][7:]
            if site_tag:
                site = site_tag['href']

personal_div = personalinfo.find('div', string='Personal')
if personal_div:
    personal_text_div = personal_div.find_next('div', class_='post-text')
    year_of_birth_tag = personal_text_div.find('span', string='Year of birth: ')
    if year_of_birth_tag:
        year_of_birth = year_of_birth_tag.next_sibling.strip()
        print(year_of_birth)
    
    yearofmembership_tag = personal_text_div.find('span', string='Year of membership: ')
    if yearofmembership_tag:
        yearofmembership = yearofmembership_tag.next_sibling.strip()
        print(yearofmembership)

    status_tag = personal_text_div.find('span', string='Status: ')
    if status_tag:
        status = status_tag.next_sibling.strip()
        print(status)
    
language_div = personalinfo.find('div', string='Language')
if language_div:
    language_text_div = language_div.find_next('div', class_='post-text')    
    if language_text_div:
        texts_Language = list(language_text_div.stripped_strings)
        language = ' , '.join(texts_Language)
        print(language)

data_90_1549 = {
    'Name': name,
    'Title': title,
    'Phone Number': ', '.join(phone_numbers),
    "Email": email,
    "Site": site,
    'Year Of Membership': yearofmembership
}

print('Saving', data_90_1549['Phone Number'])

# with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=fields)
#     writer.writeheader()
#     writer.writerows(data)