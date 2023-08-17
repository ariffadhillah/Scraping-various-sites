import requests
from bs4 import BeautifulSoup
import csv
import re

url = 'http://www.courtswv.gov/supreme-court/docs/fall2001/'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.200'
}

data = []

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

with open('50.1143.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Date Filed', 'Case No', 'Case Name', 'Link Pdf']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    # Tulis header
    writer.writeheader()

    find_table = soup.find('table', id='opinions')
    find_tbody = find_table.find('tbody')

    for find_tr in find_table.find_all('tr'):
        td_list = find_tr.find_all('td')
        if len(td_list) >= 3:  
            dateFiled = td_list[0].text
            caseNo = td_list[1].text
            caseName_td = td_list[2]
            caseName_a = caseName_td.find('a')
            if caseName_a:
                caseName = caseName_a.text
                caseName_url = caseName_a['href']
            else:
                caseName = caseName_td.text
                caseName_url = None

            if caseName_url:
                caseNameUrl = 'www.courtswv.gov/supreme-court/docs/fall2001/' + caseName_url.replace('.htm','.pdf')

            writer.writerow({
                'Date Filed':"'"+dateFiled,
                'Case No': caseNo.replace('&amp',' & '),
                'Case Name': caseName.replace('&amp',' & '),                
                'Link Pdf':  caseNameUrl
            })

print("Data successfully saved in CSV file.")