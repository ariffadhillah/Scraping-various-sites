import csv
import requests
from bs4 import BeautifulSoup
import re

baseurl = 'https://www.advokatsamfundet.se/Advokatsamfundet-engelska/Find-a-lawyer/Search-result/?'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82'
}

fields = ['url']
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
            
# print(lawfirmList)


for lawyerslist in lawfirmList:
    r = requests.get(lawyerslist, headers=headers)
    pageLawyerslist = BeautifulSoup(r.content, 'lxml')


    lawyerslistSearchresult = pageLawyerslist.find('div', class_='matrikel')
    listlawyers = lawyerslistSearchresult.find_all('div', class_='grid grid--gutter')

    for lawyers in listlawyers:
        pagelawyers = lawyers.find('a', href=True)
        if pagelawyers:
            pageURL = 'https://www.advokatsamfundet.se' + pagelawyers['href']

            r = requests.get(pageURL, headers=headers)
            soup = BeautifulSoup(r.content, 'lxml')

            # name = soup.find('h1', class_='hero-heading -black -person').text.strip()
            # title = soup.find('div', class_='hero-preamble').text.strip()
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

                    # Extract phone numbers
                    phone_numbers = [div.get_text(strip=True) for div in div_elements if re.match(r'\b\d{2,4}[-\s]?\d{2,4}[-\s]?\d{2,4}\b', div.get_text(strip=True))]

                    # Extract email and site if available
                    for div in div_elements:
                        email_tag = div.find('a', href=lambda href: href and href.startswith('mailto:'))
                        site_tag = div.find('a', href=lambda href: href and not href.startswith('mailto:'))
                        if email_tag:
                            email = email_tag['href'][7:]
                        if site_tag:
                            site = site_tag['href']
                        

            print("url PAGE", pageURL)
            print("Name:", name)
            print("Title:", title)
            print("Phone Numbers:", phone_numbers)
            print("Email:", email)
            print("Site:", site)

            

   