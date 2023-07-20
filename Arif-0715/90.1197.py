import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv
import re

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

baseurl = 'https://www.cbs.sc/Financial/BureaudeChange1.html'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.79'
}

WAIT_TIME = 10

options = Options()
options.headless = False
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
browser.maximize_window()
browser.get(baseurl)
browser.set_page_load_timeout(10)

time.sleep(6)

fields = ['Company Name','Phone Number', 'Email' , 'Address', 'List Name']
filename = '90.1197.csv'
data = []

all_page_data = []
while True:
    soup = BeautifulSoup(browser.page_source, 'lxml')
    banklist = soup.find_all('div', class_='banklist')

    for item in banklist:
        listItemBanks  = item.find_all('div', class_='col-md-6 bank ng-binding ng-scope')

        for listItemBanks in listItemBanks:
            try:
                company_name = listItemBanks.find('strong', class_='ng-binding').text.strip()
                company_name = company_name.lstrip('1234567890. ')
            except:
                company_name = ''
            

            text_content = listItemBanks.get_text()
            try:

                phone_numbers = re.findall(r'\(\+\d+\) [\d /]+', text_content)

                phone_numbers_str = ', '.join(phone_numbers)
            except:
                phone_numbers = ''
                phone_numbers_str = ''
            
            try:
                email_link = listItemBanks.find('a', href=lambda href: href and href.startswith('mailto:'))
                email = email_link.get_text().strip() if email_link else None
            except:
                email_link = ''
                email = ''
            
            # try:
            #     site_link = listItemBanks.find('a', href=lambda href: href and (href.startswith('http://') or href.startswith('https://')))
            #     siteURL = site_link.get_text().strip() if site_link else None
            # except:
            #    site_link = ''
            #    siteURL = ''     
            
            # try:
            # address =  listItemBanks.text.replace(phone_numbers_str,'').replace(company_name,'').replace(siteURL,'').replace(email,'').strip()
            # address = address.lstrip('1234567890. ')

            # address = re.sub(r'\n\s*\n', ', ', address)
            # address = re.sub(r',\s+', ', ', address)
            # address = re.sub(r'\s+,', ', ', address)
            # except:
            #     address = ''            
            address = listItemBanks.get_text().strip()
                
                # Cek apakah variabel-variabel berisi None atau string kosong sebelum menggunakan replace
            if phone_numbers_str:
                address = address.replace(phone_numbers_str, ' ')
            if company_name:
                address = address.replace(company_name, ' ')
            # if siteURL:
            #     address = address.replace(siteURL, ' ')
            if email:
                address = address.replace(email, ' ')

                # Menghapus karakter angka di awal
            address = address.lstrip('1234567890. ')

                # Menghapus spasi ganda dan baris kosong dalam teks alamat
            address = re.sub(r'\n\s*\n', ', ', address)
            address = re.sub(r',\s+', ', ', address)
            address = re.sub(r'\s+,', ', ', address)



            data_90_1197 = {
                'Company Name': company_name,
                'Phone Number': phone_numbers_str,
                'Email': email,
                'Address': address.replace('  ','').strip().replace(phone_numbers_str, '').replace(', P',' P'),                
                'List Name': 'Class B Bureaux de Change'
            }
            data.append(data_90_1197)
            print('Saving', data_90_1197['Company Name'])
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fields)
                writer.writeheader()
                writer.writerows(data)
   

    next_button = WebDriverWait(browser, WAIT_TIME).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Next')]")))
    is_disabled = next_button.get_attribute('disabled')
    if is_disabled and is_disabled.lower() == 'true':
        break

    next_button.click()
    time.sleep(6)

    soup_next = BeautifulSoup(browser.page_source, 'lxml')

browser.quit()
