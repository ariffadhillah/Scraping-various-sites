import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import csv

baseurl = 'https://ipsearch.saip.gov.sa/wopublish-search/public/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

WAIT_TIME = 80

fields = ['Applicant', 'Original Filing Number', 'Filing Date', 'Details Page URL']
filename = '80.0006.csv'
data = []

def process_page(url):
    options = Options()
    options.headless = False
    options.add_argument("--start-maximized")  # Menambahkan argumen untuk memperbesar jendela browser
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    browser.maximize_window()
    browser.get(url)

    search_button_basic = WebDriverWait(browser, WAIT_TIME).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Basic')]"))
    )
    search_button_basic.click()

    time.sleep(6)

    # Menggunakan browser.page_source untuk mendapatkan HTML dari halaman saat ini
    soup = BeautifulSoup(browser.page_source, 'lxml')

    searchTable = soup.find('table', id='dataTable')

    # Periksa apakah elemen <tbody> ada
    if searchTable.find('tbody'):
        searchTableitems = searchTable.find('tbody').find_all('tr')
    else:
        searchTableitems = searchTable.find_all('tr')

    for item in searchTableitems:
        if 'id' in item.attrs:
            item_id = item['id']
            detail_url = urljoin(baseurl, f'detail/patents?id={item_id}')
            print(detail_url)

            # Cari elemen <span> dengan kelas rs-AFNB_ORI di dalam elemen item
            original_Filing_Number = item.find('span', class_='rs-AFNB_ORI')
            if original_Filing_Number:
                originalFilingNumber = original_Filing_Number.text
                

            # Cari elemen dengan kelas date di dalam elemen item
            filling_date = item.find(class_='rs-AFDT')
            if filling_date:
                fillingDate = filling_date.text
                

            # # Cari elemen dengan kelas date di dalam elemen item
            theApplicant = item.find(class_='rs-APNA')
            if theApplicant:
                applicant = theApplicant.text
            
            data_80_0006 = {
                'Applicant' : applicant,
                'Original Filing Number': originalFilingNumber,
                'Filing Date': fillingDate,
                'Details Page URL': detail_url,
            }
            data.append(data_80_0006)
            print('Saving', data_80_0006['Details Page URL'])
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fields)
                writer.writeheader()
                writer.writerows(data)
                    
                
    try:
            
        current_page = 1
        next_link = soup.find('a', title='Go to page {}'.format(current_page + 1))
    except:
        next_link = ''

    while next_link:
        current_page += 1
        next_url = urljoin(baseurl, next_link['href'])
        r_next = requests.get(next_url, headers=headers)
        print(next_url)

        soup_next = BeautifulSoup(r_next.content, 'lxml')

        time.sleep(6)
        next_button = WebDriverWait(browser, WAIT_TIME).until(
            EC.element_to_be_clickable((By.LINK_TEXT, str(current_page + 1)))
        )
        next_button.click()

        soup_next = BeautifulSoup(browser.page_source, 'lxml')

        time.sleep(6)
        searchTable_next = soup_next.find('table', id='dataTable')
        searchtbody_next = searchTable_next.find('tbody') 
        searchTableitems_next = searchtbody_next.find_all('tr')

        for item_next in searchTableitems_next:
            if 'id' in item_next.attrs:
                item_id_next = item_next['id']
                detail_url_next = urljoin(baseurl, f'detail/patents?id={item_id_next}')
                

            originalFilingNumber_next = item_next.find('span', class_='rs-AFNB_ORI')
            if originalFilingNumber_next:
                originalFilingNumberNext = originalFilingNumber_next.text
                

            # Cari elemen dengan kelas date di dalam elemen item
            filling_date_next = item_next.find(class_='rs-AFDT')
            if filling_date_next:
                fillingDate_next = filling_date_next.text
            
            theApplicant_next = item_next.find(class_='rs-APNA')
            if theApplicant_next:
                applicant_next = theApplicant_next.text

                data_80_0006_next = {
                    'Applicant' : applicant_next,
                    'Original Filing Number': originalFilingNumberNext,
                    'Filing Date': fillingDate_next,
                    'Details Page URL': detail_url_next,
                }
                data.append(data_80_0006_next)
                print('Saving', data_80_0006_next['Details Page URL'])
                with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=fields)
                    writer.writeheader()
                    writer.writerows(data)
                    

        time.sleep(6)

        next_link = soup_next.find('a', title='Go to page {}'.format(current_page + 1))

    browser.quit()  # Menutup browser setelah selesai

try:
# Mulai dengan halaman pertama
    start_url = urljoin(baseurl, 'patents?1&lang=en&query=*:*')
    process_page(start_url)
except:
    start_url = ''




# import requests
# from bs4 import BeautifulSoup
# from urllib.parse import urljoin
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# import time
# import csv

# baseurl = 'https://ipsearch.saip.gov.sa/wopublish-search/public/'

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
# }

# WAIT_TIME = 80

# fields = ['Applicant', 'Original Filing Number', 'Filing Date', 'Details Page URL']
# filename = '80.0006.csv'
# data = []

# def process_page(url):
#     options = Options()
#     options.headless = False
#     options.add_argument("--start-maximized")  # Menambahkan argumen untuk memperbesar jendela browser
#     browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
#     browser.maximize_window()
#     browser.get(url)

#     search_button_basic = WebDriverWait(browser, WAIT_TIME).until(
#         EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'بحث سريع')]"))
#     )
#     search_button_basic.click()

#     time.sleep(6)

#     while True:
#         # Menggunakan browser.page_source untuk mendapatkan HTML dari halaman saat ini
#         soup = BeautifulSoup(browser.page_source, 'lxml')

#         searchTable = soup.find('table', id='dataTable')

#         # Periksa apakah elemen <tbody> ada
#         if searchTable.find('tbody'):
#             searchTableitems = searchTable.find('tbody').find_all('tr')
#         else:
#             searchTableitems = searchTable.find_all('tr')

#         for item in searchTableitems:
#             if 'id' in item.attrs:
#                 item_id = item['id']
#                 detail_url = urljoin(baseurl, f'detail/patents?id={item_id}')
#                 # print(detail_url)

#                 original_Filing_Number = item.find('span', class_='rs-AFNB_ORI')
#                 if original_Filing_Number:
#                     originalFilingNumber = original_Filing_Number.text

#                 filling_date = item.find(class_='rs-AFDT')
#                 if filling_date:
#                     fillingDate = filling_date.text

#                 theApplicant = item.find(class_='rs-APNA')
#                 if theApplicant:
#                     applicant = theApplicant.text

#                 data_80_0006 = {
#                     'Applicant': applicant,
#                     'Original Filing Number': originalFilingNumber,
#                     'Filing Date': fillingDate,
#                     'Details Page URL': detail_url,
#                 }
#                 data.append(data_80_0006)
#                 print('Saving', data_80_0006['Details Page URL'])

#         with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
#             writer = csv.DictWriter(csvfile, fieldnames=fields)
#             writer.writeheader()
#             writer.writerows(data)
#         next_button = soup.find('a', title=lambda x: x and x.startswith('Go to page '))
#         if next_button:
#             next_url = urljoin(baseurl, next_button['href'])
#             browser.get(next_url)
#             time.sleep(6)
#         else:
#             break


#     browser.quit()  # Menutup browser setelah selesai


# # Mulai dengan halaman pertama
# start_url = urljoin(baseurl, 'patents?1&lang=ar&query=*:*')
# process_page(start_url)
