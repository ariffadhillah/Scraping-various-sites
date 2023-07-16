import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv

baseurl = 'https://find-and-update.company-information.service.gov.uk/advanced-search/get-results?companyNameIncludes=&companyNameExcludes=&registeredOfficeAddress=&incorporationFromDay=&incorporationFromMonth=&incorporationFromYear=&incorporationToDay=&incorporationToMonth=&incorporationToYear=&status=receivership&status=liquidation&status=administration&status=insolvency-proceedings&status=voluntary-arrangement&sicCodes=&dissolvedFromDay=&dissolvedFromMonth=&dissolvedFromYear=&dissolvedToDay=&dissolvedToMonth=&dissolvedToYear='
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.79'
}

# for x in range(1, 510):
#     url = f"{baseurl}&page={x}"
#     r = requests.get(url, headers=headers)
#     soup = BeautifulSoup(r.content, 'lxml')

#     table = soup.find('table', class_='govuk-table')

#     if table:
#         for listItemresult in table.find_all('a', class_='govuk-link', href=True):
#             pageresultURL = 'https://find-and-update.company-information.service.gov.uk' + listItemresult['href']


#     else:
#         break



url = 'https://find-and-update.company-information.service.gov.uk/company/02553124/'

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')


companyName = soup.find('p', class_='heading-xlarge').text.strip()
print(companyName)