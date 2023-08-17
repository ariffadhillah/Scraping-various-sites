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

driver.get('https://www.gov.ky/chiefofficers')
driver.maximize_window()

wait = WebDriverWait(driver, 10)


fields = ['Names', 'Roles 1','Roles 2' ]
filename = '20.1155.csv'

data = []
time.sleep(10)
soup = BeautifulSoup(driver.page_source, 'lxml')

search_section = soup.find('div', id='right-col')
card_ = search_section.find_all('div', {'class':['sl-three-columns-left','sl-three-columns-center','sl-three-columns-right']})

datalist1 = []
datalist2 = []
datalist3 = []

for cardBody in card_:
    info = cardBody.find_all('div', class_='scs-paragraph-text')
    
    for item in info:
        strong_text = item.find('strong')
        if strong_text:
            name = strong_text.get_text(strip=True)
            text_elements = item.find_all(string=True)
            text_lines = [element.strip() for element in text_elements if element.strip()]
            
            if len(text_lines) >= 3:
                datalist1.append(text_lines[0])
                datalist2.append(text_lines[1])
                datalist3.append(text_lines[2])

# Menampilkan data satu per satu
for i in range(len(datalist1)):
    name = datalist1[i]
    roles1 = datalist2[i]
    roles2 = datalist3[i]

    data_20_1155 = {
        'Names' : name, 
        'Roles 1' : roles1,
        'Roles 2' : roles2
    }
    data.append(data_20_1155)
    print('Saving', data_20_1155['Names'])
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)

driver.quit()
