import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

baseurl = 'https://dos.sunbiz.org/jlilist.html'
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.79',
    'cookie': '_ga=GA1.1.781427645.1688775478; __utmz=91298328.1688775481.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=91298328.781427645.1688775478.1689325870.1689336213.10; __utmc=91298328; __utmt=1; __utmb=91298328.2.10.1689336213; _ga_PFV0FXXNRV=GS1.1.1689336212.11.1.1689337613.0.0.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
}


fields = ['Name Defendant(s)' , 'Document Number' , 'Status' , 'Case Number' , 'Name of Court'  , 'File Date' ,'Date of Entry' ,'Expiration Date' , 'Amount Due' , 'Interest Rate' , 'Name And Address of Judgment Creditor (Plaintiff)'  , 'Address of Judgment Debtor(s) (Defendant(s))','Processed Thru' , 'Detail Page URL' ]

filename = '60.0152.csv'
data = []


WAIT_TIME = 60


options = Options()
options.headless = False
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
browser.maximize_window()
browser.get(baseurl)
browser.set_page_load_timeout(10)

send_key = 'Judgment Lien Name List'

input_keys = browser.find_element(By.ID, 'debtor_name')
input_keys.send_keys(send_key)

search_button = WebDriverWait(browser, WAIT_TIME).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="MainContentInquiry"]/form/input[3]')))
search_button.click()

# Wait for a few seconds for the page to load
time.sleep(5)

# Get the HTML content of the loaded page
page_source = browser.page_source

# Use BeautifulSoup to parse the HTML
soup = BeautifulSoup(page_source, 'html.parser')

seacrtable = soup.find('table', {'summary':'This table displays the name lists for the 3 column headings.'})

for href in seacrtable.find_all('a', href=True):
    pageURL =  'https://dos.sunbiz.org/' + href['href']
    print(pageURL)

    # Buka halaman URL menggunakan Selenium
    browser.get(pageURL)

    # Tunggu beberapa detik untuk halaman terload sepenuhnya
    time.sleep(5)

    # Dapatkan konten HTML dari halaman yang terload
    page_source = browser.page_source

    # Gunakan BeautifulSoup untuk mem-parsing HTML
    page = BeautifulSoup(page_source, 'html.parser')

#     # Lakukan apa yang Anda inginkan dengan halaman tersebut
#     title = page.find('span', class_='pagetitle')
#     print(title)


# url = 'https://dos.sunbiz.org/scripts/jlidet.exe?action=DETLIST&inquiry_number=J13000489808&inquiry_date=048686400804000000&return_number=J04900013668&return_date=045920736000200000'

# r = requests.get(url, headers=headers)
# page = BeautifulSoup(r.content, 'lxml')


    try:
        title = page.find('span', class_='pagetitle').text.strip()
    except:
        title = ''


    try:
        document_Number = page.find('td', class_='descript', string='Document Number')
        documentNumber = document_Number.find_next_sibling('td', class_='data').get_text(strip=True)
    except:
        document_Number = ''
        documentNumber = ''

    try:
        status_ = page.find('td', class_='descript', string='Status')
        status = status_.find_next_sibling('td', class_='data').get_text(strip=True)
    except:
        status_ = ''
        status = ''

    try:
        case_Number = page.find('td', class_='descript', string='Case Number')
        caseNumber = case_Number.find_next_sibling('td', class_='data').get_text(strip=True)
    except:
        case_Number = ''
        caseNumber = ''

    try:
        name_of_Court = page.find('td', class_='descript', string='Name of Court')
        nameofCourt = name_of_Court.find_next_sibling('td', class_='data').get_text(strip=True)
    except:
        name_of_Court = ''
        nameofCourt = ''


    try:
        file_Date = page.find('td', class_='descript', string='File Date')
        fileDate = file_Date.find_next_sibling('td', class_='data').get_text(strip=True)
    except:
        file_Date = ''
        fileDate = ''

    try:
        dateofEntry_ = page.find('td', class_='descript', string='Date of Entry')
        dateofEntry = dateofEntry_.find_next_sibling('td', class_='data').get_text(strip=True)
    except:
        dateofEntry_ = ''
        dateofEntry = ''

    try:
        expiration_Date = page.find('td', class_='descript', string='Expiration Date')
        expirationDate = expiration_Date.find_next_sibling('td', class_='data').get_text(strip=True)
    except:
        expiration_Date = ''
        expirationDate = ''

    try:
        amount_Due = page.find('td', class_='descript', string='Amount Due')
        amountDue = amount_Due.find_next_sibling('td', class_='data').get_text(strip=True)
    except:
        amount_Due = ''
        amountDue = ''

    try:
        interest_Rate = page.find('td', class_='descript', string='Interest Rate')
        interestRate = interest_Rate.find_next_sibling('td', class_='data').get_text(strip=True)
    except:
        interest_Rate = ''
        interestRate = ''
        
    try:
        plaintiff_ = page.find('tr', string='Name And Address of Judgment Creditor (Plaintiff)')
        plaintiff = plaintiff_.find_next_sibling('tr').find('td').text.strip()

    except:
        plaintiff_ = ''
        plaintiff = ''

    try:
        processed_Thru = page.find('span', class_='descript', string='Processed Thru')
        processedThru = processed_Thru.find_next_sibling('span', class_='data').get_text(strip=True)
    except:
        processed_Thru = ''
        processedThru = ''


    try:
        defendant_ = page.find('tr', string='Name And Address of Judgment Debtor(s) (Defendant(s))')
        defendant = defendant_.find_next_sibling('tr').find('td', class_='data')

        defendant_text = defendant.get_text(separator='\n', strip=True)
        split_text = defendant_text.split('\n')

        name = split_text[0].strip()
        address = ' '.join(split_text[1:]).strip()
    except:
        name = ''
        address = ''


    data_60_0152 = {
        'Name Defendant(s)': name.replace('  ', ''),
        'Document Number': documentNumber,
        'Status': status,
        'Case Number': "'"+ caseNumber,
        'Name of Court':nameofCourt,
        'File Date':fileDate,
        'Date of Entry':dateofEntry,
        'Expiration Date': expirationDate,
        'Amount Due': amountDue,
        'Interest Rate': interestRate,
        'Name And Address of Judgment Creditor (Plaintiff)':plaintiff,
        'Address of Judgment Debtor(s) (Defendant(s))': address,
        'Processed Thru': processedThru,
        'Detail Page URL':pageURL,
    }

    data.append(data_60_0152)
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        for item in data:
            writer.writerow(item)            

browser.quit()

