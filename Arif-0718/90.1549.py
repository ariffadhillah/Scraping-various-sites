import csv
import requests
from bs4 import BeautifulSoup
import re

baseurl = 'https://www.advokatsamfundet.se/Advokatsamfundet-engelska/Find-a-lawyer/Search-result/?'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82'
}

fields = ['Lawyers Name' , 'Lawyers Title' , 'Phone Numbers Lawyers' , 'Email Lawyers' , 'Site Lawyers' , 'Year of birth Lawyers' , 'Year of membership' , 'Status' , 'Area of law Lawyers' , 'Page URL Details Lawyers' , 'Company Firms' , 'Area of law Firms' , 'Language Firms' , 'Telephone Firms' , 'Fax Firms' , 'Email Firms' , 'Site URL Firms' , 'Visiting address Firms' , 'Postal address Firms' , 'Local office Firms' , 'Page URL Details Firms']

filename = '90.1549.csv'
data = []

processed_urls = set()
lawfirmList = []

r = requests.get(baseurl, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

itemSearchresult = soup.find('div', class_='matrikel')

itemList = itemSearchresult.find_all('div', class_='grid grid--gutter')

for lawFirm in itemList:
    linkItem = lawFirm.find('a', href=True)  
    if linkItem:
        url = 'https://www.advokatsamfundet.se' + linkItem['href']
        if url not in processed_urls:
            lawfirmList.append(url)
            processed_urls.add(url)

for lawyerslist in lawfirmList:
    r = requests.get(lawyerslist, headers=headers)
    pageLawyerslist = BeautifulSoup(r.content, 'lxml')

    # print(lawyerslist)

    telephone_law = '' 
    fax_law = ''
    email_law = ''
    site_law = ''
    area_of_law_text = ''
    language_law_text = ''
    visiting_address_text_law = ''
    postal_address_lav_text = ''
    local_office_lav_text = ''

    name_firms = pageLawyerslist.find('h1', class_='hero-heading -black -firm').text.strip()
    # print(name_firms)

    lawFirms = pageLawyerslist.find_all('div', class_='Section-content')[0]
    area_of_law_div = lawFirms.find('div', string='Area of law')

    if area_of_law_div:
        # Find the next sibling <div> that contains the text you want to extract
        area_of_law_text = area_of_law_div.find_next_sibling('div').get_text(strip=True)

    language_law_div = lawFirms.find('div', string='Language')

    if language_law_div:
        # Find the next sibling <div> that contains the text you want to extract
        language_law_text = language_law_div.find_next_sibling('div').get_text(strip=True)


    lawFirms = pageLawyerslist.find_all('div', class_='Section-content')[1]

    contact_div_law = pageLawyerslist.find('div', string='Contact')

    if contact_div_law:
        # Find the next occurrence of <div> after the element with "Contact"
        contact_info_law_div = contact_div_law.find_next('div')

        # Extract phone and fax
        telephone_tag = contact_info_law_div.find('span', string='Telephone: ')
        fax_tag = contact_info_law_div.find('span', string='Fax: ')
        telephone_law = telephone_tag.next_sibling.strip() if telephone_tag else ''
        fax_law = fax_tag.next_sibling.strip() if fax_tag else ''

        # Extract email and site if available
        email_tag = contact_info_law_div.find('a', href=lambda href: href and href.startswith('mailto:'))
        site_tag = contact_info_law_div.find('a', href=lambda href: href and not href.startswith('mailto:'))
        email_law = email_tag['href'][7:] if email_tag else ''
        site_law = site_tag['href'] if site_tag else ''

        visiting_address_law_div = lawFirms.find('div', string='Visiting address')
        if visiting_address_law_div:
            visiting_address_text_law = visiting_address_law_div.find_next_sibling('div').get_text(separator=' , ')

        postal_address_lav_div = lawFirms.find('div', string='Postal address')
        if postal_address_lav_div:
            postal_address_lav_text = postal_address_lav_div.find_next_sibling('div').get_text(separator=' , ')

        local_office_lav_div = lawFirms.find('div', string='Local office')
        if local_office_lav_div:
            local_office_lav_text = local_office_lav_div.find_next_sibling('div').get_text(separator=' , ')



    lawyerslistSearchresult = pageLawyerslist.find('div', class_='matrikel')
    listlawyers = lawyerslistSearchresult.find_all('div', class_='grid grid--gutter')

    for lawyers in listlawyers:
        pagelawyers = lawyers.find('a', href=True)
        if pagelawyers:
            pageURL = 'https://www.advokatsamfundet.se' + pagelawyers['href']

            r = requests.get(pageURL, headers=headers)
            souplawyers = BeautifulSoup(r.content, 'lxml')

            # print(pageURL)

            name_Lawyers = souplawyers.find('h1', class_='hero-heading -black -person').text.strip()
            title_Lawyers = souplawyers.find('div', class_='hero-preamble').text.strip()

            phone_numbers_Lawyers = []
            email_lawyers = ''
            site_lawyers = ''
            area_of_law_lawyers = ''
            language_lawyers = ''
            status_lawyers =''

            personalinfo = souplawyers.find_all('div', class_='Section-content')[0]
            sibling_contact = personalinfo.find('div', string='Contact')

            if sibling_contact:
                post_text_div = sibling_contact.find_next_sibling('div', class_='post-text')
                if post_text_div:
                    div_elements = post_text_div.find_all('div')

                    phone_numbers_Lawyers = [div.get_text(strip=True) for div in div_elements if re.match(r'\b\d{2,4}[-\s]?\d{2,4}[-\s]?\d{2,4}\b', div.get_text(strip=True))]
                    
                    for div in div_elements:
                        email_tag = div.find('a', href=lambda href: href and href.startswith('mailto:'))
                        site_tag = div.find('a', href=lambda href: href and not href.startswith('mailto:'))
                        if email_tag:
                            email_lawyers = email_tag['href'][7:]
                        if site_tag:
                            site_lawyers = site_tag['href']

            personal_div = personalinfo.find('div', string='Personal')
            if personal_div:
                personal_text_div = personal_div.find_next('div', class_='post-text')
                year_of_birth_tag = personal_text_div.find('span', string='Year of birth: ')
                if year_of_birth_tag:
                    year_of_birth = year_of_birth_tag.next_sibling.strip()
                    # print(year_of_birth)
                
                yearofmembership_tag = personal_text_div.find('span', string='Year of membership: ')
                if yearofmembership_tag:
                    yearofmembership = yearofmembership_tag.next_sibling.strip()
                    # print(yearofmembership)

                status_tag = personal_text_div.find('span', string='Status: ')
                if status_tag:
                    status_lawyers = status_tag.next_sibling.strip()
                    # print(status)
                
            language_div = personalinfo.find('div', string='Language')
            if language_div:
                language_text_div = language_div.find_next('div', class_='post-text')    
                if language_text_div:
                    texts_Language = list(language_text_div.stripped_strings)
                    language_lawyers = ' , '.join(texts_Language)
                    # print(language)
                
            area_of_law_div = personalinfo.find('div', string='Area of law')
            if area_of_law_div:
                area_of_law_text_div = area_of_law_div.find_next('div', class_='post-text')    
                if area_of_law_text_div:
                    text_area_of_law_text_div = list(area_of_law_text_div.stripped_strings)
                    area_of_law_lawyers = ' , '.join(text_area_of_law_text_div)

            # print(title_Lawyers,title_Lawyers, email,site, phone_numbers_Lawyers,year_of_birth, yearofmembership,   area_of_law)

        data_90_1549 = {
            'Lawyers Name' : name_Lawyers,
            'Lawyers Title' : title_Lawyers,
            'Phone Numbers Lawyers': ' , ' .join(phone_numbers_Lawyers),
            'Email Lawyers': email_lawyers,
            'Site Lawyers': site_lawyers,
            'Year of birth Lawyers': year_of_birth,
            'Year of membership': yearofmembership,
            'Status': status_lawyers,
            'Area of law Lawyers': area_of_law_lawyers,
            'Page URL Details Lawyers':pageURL,
            'Company Firms': name_firms,
            'Area of law Firms': area_of_law_text,
            'Language Firms' : language_law_text,
            'Telephone Firms': telephone_law,
            'Fax Firms': fax_law,
            'Email Firms': email_law,
            'Site URL Firms': site_law,
            'Visiting address Firms': visiting_address_text_law.strip(),
            'Postal address Firms': postal_address_lav_text.strip(),
            'Local office Firms': local_office_lav_text.strip(),
            'Page URL Details Firms': lawyerslist
        }

        data.append(data_90_1549)
        print('Saving : ' , data_90_1549['Visiting address Firms'] , data_90_1549['Page URL Details Lawyers'] )
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            writer.writerows(data)

print(f"Save to {filename}")
