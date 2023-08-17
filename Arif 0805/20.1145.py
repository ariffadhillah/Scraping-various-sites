import time
import requests
from bs4 import BeautifulSoup
import csv

from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = EdgeService(executable_path="./Don-Osterloh\Arif 0805/msedgedriver.exe")

options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.200')
driver = webdriver.Edge(options=options)

WAIT_TIME = 10

driver.get('https://www.otp.gov.ky/#key-people-block-slot')
driver.maximize_window()

wait = WebDriverWait(driver, 10)

fields = ['Names' ,  'Address' , 'Telephone' , 'Web Address' , 'Office Hours']
filename = '20.1145.csv'

data = []
time.sleep(10)

soup = BeautifulSoup(driver.page_source, 'lxml')
find_ul = soup.find_all('ul' , {'class' : ['Office-Register']})

office_adjust = soup.find_all('li', class_='office line-adjust')[0].text.strip()
address_office1 = soup.find('li', class_='pad-address office').text.strip()
address_office2 = soup.find_all('li', class_='office line-adjust')[1].text.strip()
address_office3 = soup.find_all('li', class_='office line-adjust')[2].text.strip()
telephone = soup.find_all('li', class_='office line-adjust')[3].text.strip().replace('Telephone:','')
webAddress = soup.find_all('li', class_='office line-adjust')[4].text.strip().replace('Web Address:','')
officeHours = soup.find_all('li', class_='office line-adjust')[5].text.replace('Office Hours:','')

address_office = office_adjust + address_office1 + address_office2 + address_office3

data_20_1145 = {
    'Names' : 'OFFICE OF THE PREMIER',
    'Address' : address_office,
    'Telephone' : telephone,
    'Web Address' : webAddress,
    'Office Hours' : officeHours
}
data.append(data_20_1145)
print('Saving', data_20_1145['Names'])
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(data)

driver.quit()