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

baseurl = 'http://dos.sunbiz.org/lienlis.html'
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.79',
    'cookie': '_ga=GA1.1.781427645.1688775478; __utmz=91298328.1688775481.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=91298328.781427645.1688775478.1689325870.1689336213.10; __utmc=91298328; __utmt=1; __utmb=91298328.2.10.1689336213; _ga_PFV0FXXNRV=GS1.1.1689336212.11.1.1689337613.0.0.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
}

fields = ['Name Defendant(s)','Summary for Filing' , 'Date Filed' ,'Status' , 'Expires' , 'Pages in all Forms/Attachments' , 'Current Secured Parties' , 'Current Debtors' , 'Events Filed' , 'Serial Number' , 'Assessment Date' , 'Secured Parties Address' , 'Debtor Parties Address' ,'Title' , 'Detail Page URL' ]

filename = '60.0153.csv'
data = []


WAIT_TIME = 60


options = Options()
options.headless = False
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
browser.maximize_window()
browser.get(baseurl)
browser.set_page_load_timeout(10)

send_key = 'Federal Lien Registration List'

input_keys = browser.find_element(By.ID, 'debtor_name')
input_keys.send_keys(send_key)

search_button = WebDriverWait(browser, WAIT_TIME).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="MainContentInquiry"]/form/input[4]')))
search_button.click()

time.sleep(5)

page_source = browser.page_source

soup = BeautifulSoup(page_source, 'html.parser')

seacrtable = soup.find('table', {'summary':'This table displays the name lists for the 5 column headings.'})

for href in seacrtable.find_all('a', class_='list', href=True):
    pageURL =  'https://dos.sunbiz.org/' + href['href']
    print(pageURL)

    
    browser.get(pageURL)
    
    time.sleep(5)
    
    page_source = browser.page_source

    # Gunakan BeautifulSoup untuk mem-parsing HTML
    page = BeautifulSoup(page_source, 'html.parser')


    try:
        title = page.find('span', class_='pagetitle').text.strip()
    except:
        title = ''
    
    print(title)


    try:
        summary_for_Filing = page.find('td', class_='descript', string='Summary for Filing')
        summaryforFiling = summary_for_Filing.find_next_sibling('td', class_='data').get_text(strip=True)
    except:
        summary_for_Filing = ''
        summaryforFiling = ''

    try:
        dateFiled_ = page.find('td', class_='descript', string='Date Filed')
        dateFiled = dateFiled_.find_next_sibling('td', class_='data').get_text(strip=True)
    except:
        dateFiled_ = ''
        dateFiled = ''

    try:
        status_ = page.find('td', class_='descript', string='Status')
        status = status_.find_next_sibling('td', class_='data').get_text(strip=True)
    except:
        status_ = ''
        status = ''

    try:
        expires_ = page.find('td', class_='descript', string='Expires')
        expires = expires_.find_next_sibling('td', class_='data').get_text(strip=True)
    except:
        expires_ = ''
        expires = ''
    

    try:
        pages_in_all_Forms_Attachments = page.find('td', class_='descript', string='Pages in all Forms/Attachments')
        pagesinallFormsAttachments = pages_in_all_Forms_Attachments.find_next_sibling('td', class_='data').get_text(strip=True)
    except:
        pages_in_all_Forms_Attachments = ''
        pagesinallFormsAttachments = ''

    try:
        currentSecuredParties_ = page.find('td', class_='descript', string='Current Secured Parties')
        currentSecuredParties = currentSecuredParties_.find_next_sibling('td', class_='data').get_text(strip=True)
    except:
        currentSecuredParties_ = ''
        currentSecuredParties = ''

    try:
        current_Debtors = page.find('td', class_='descript', string='Current Debtors')
        currentDebtors = current_Debtors.find_next_sibling('td', class_='data').get_text(strip=True)
    except:
        current_Debtors = ''
        currentDebtors = ''    

    try:
        events_Filed = page.find('td', class_='descript', string='Events Filed')
        eventsFiled = current_Debtors.find_next_sibling('td', class_='data').get_text(strip=True)
    except:
        events_Filed = ''
        eventsFiled = ''

    try:
        serial_Number = page.find('td', class_='descript', string='Serial Number')
        serialNumber = serial_Number.find_next_sibling('td', class_='data').get_text(strip=True)
    except:
        serial_Number = ''
        serialNumber = ''    

    try:
        assessment_Date = page.find('td', class_='descript', string='Assessment Date')
        assessmentDate = assessment_Date.find_next_sibling('td', class_='data').get_text(strip=True)
    except:
        assessment_Date = ''
        assessmentDate = ''


    try:
        secured_Parties_Address = page.find('tr', string='Secured Parties Address')
        securedPartiesAddress = secured_Parties_Address.find_next_sibling('tr').find('td', class_='data').get_text(strip=True)
    except:
        secured_Parties_Address = ''
        securedPartiesAddress = ''

    try:
        defendant_ = page.find('tr', string='Debtor Parties Address')
        defendant = defendant_.find_next_sibling('tr').find('td', class_='data')

        defendant_text = defendant.get_text(separator='\n', strip=True)
        split_text = defendant_text.split('\n')

        name = split_text[0].strip()
        address = ' '.join(split_text[1:]).strip()
    except:
        name = ''
        address = ''

    data_60_0153 = {
        'Name': name.replace('  ', ''),
        'Summary for Filing': summaryforFiling,
        'Date Filed': dateFiled,
        'Status':status,
        'Expires': expires,
        'Pages in all Forms/Attachments': pagesinallFormsAttachments,
        'Current Secured Parties': currentSecuredParties,
        'Current Debtors':currentDebtors,
        'Events Filed':eventsFiled,
        'Serial Number': serialNumber,
        'Assessment Date':assessmentDate,
        'Secured Parties Address':securedPartiesAddress,                
        'Debtor Parties Address': address,
        'Title': title,
        'Detail Page URL':pageURL,
    }

    data.append(data_60_0153)
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        for item in data:
            writer.writerow(item)            

browser.quit()

