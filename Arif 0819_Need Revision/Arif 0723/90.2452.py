



import time
import requests
from bs4 import BeautifulSoup
import csv

from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = EdgeService(executable_path="msedgedriver.exe")

options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.46')
driver = webdriver.Edge(options=options)

WAIT_TIME = 60

driver.get('https://www.bcu.gub.uy/Servicios-Financieros-SSF/Paginas/emisores_Lst.aspx')
driver.maximize_window()

wait = WebDriverWait(driver, 10)

def process_data_and_save_to_csv(page_soup):
    # Your code to process data


    # time.sleep(10)
    data = []
    time.sleep(5)
    search_table = page_soup.find('table', class_='ms-listviewtable')
    listItems = search_table.find_all('td', class_='ms-vb2')

    url = []

    time.sleep(.5)
    for item in listItems:
        a_tag = item.find('a', onclick='')
        if a_tag:
            href = a_tag.get('href')
            url.append('https://www.bcu.gub.uy' + href)

    name = ''
    title = ''

    for detailsPage in url:
        r = requests.get(detailsPage, )
        soup = BeautifulSoup(r.content, 'lxml')


        try:
            companyName = soup.find('span', class_='BCU_form_label').text.strip()
            find_tables = soup.find_all('table', {'id': ['lstAdministracion', 'lstDirectorio', 'lstSindicatura']})

            for item in find_tables:
                names = item.find_all('span', class_='dirnombre')
                title_staff = item.find_all('span', class_='dircargo')

                for name_, title_ in zip(names, title_staff):
                    name = name_.text
                    title = title_.text

                    data_90_2452 = {
                        'Name': name,
                        'Personal Superior': title,
                        'Company Name': companyName,
                        'Link Page': detailsPage
                    }

                    data.append(data_90_2452)
                    print('Saving', data_90_2452['Name'])

        except:
            companyName = ''

            find_tables = ''




    # Save data to CSV file
    fields = ['Name', 'Personal Superior', 'Company Name', 'Link Page']
    filename = '90.2452.csv'

    # Open file in 'a' mode (append) instead of 'w' mode (write)
    with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)

        # Only write header if file is empty
        if csvfile.tell() == 0:
            writer.writeheader()

        writer.writerows(data)

# Initial processing of the first page
soup = BeautifulSoup(driver.page_source, 'lxml')
process_data_and_save_to_csv(soup)

# Find all the <a> elements within the table row for pagination
pagination_links = driver.find_elements(By.XPATH, "//tr[@class='institucionesPager']//table//a")

# Iterate through the pagination links and process each page
while True:
    current_page_element = driver.find_element(By.XPATH, "//tr[@class='institucionesPager']//table//td//span")
    current_page = int(current_page_element.text.strip())

    next_page_link = None
    for link in pagination_links:
        page_number = link.text.strip()
        if page_number.isdigit() and int(page_number) == current_page + 1:
            next_page_link = link
            break

    if next_page_link:
        next_page_link.click()
        WebDriverWait(driver, WAIT_TIME).until(EC.staleness_of(next_page_link))
        soup = BeautifulSoup(driver.page_source, 'lxml')
        process_data_and_save_to_csv(soup)

        # Update pagination links for the new page
        pagination_links = driver.find_elements(By.XPATH, "//tr[@class='institucionesPager']//table//a")
    else:
        break

driver.quit()