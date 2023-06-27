import requests
from bs4 import BeautifulSoup
import csv

baseurl = 'https://instante.justice.md/ro/hotaririle-instantei?Instance=All&Numarul_dosarului=&Denumirea_dosarului=&date=&Tematica_dosarului=&Tipul_dosarului=All&'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.51'
}

fields = ['Denumirea dosarului', 'Instanțe judecătorești', 'Numărul dosarului', 'Data pronunțării', 'Data înregistrării', 'Data publicării', 'Tipul dosarului', 'Tematica dosarului', 'Judecător', 'Links Act judecătoresc / URL PDF', 'Page Category']
filename = '50.0415.csv'

data = []
page = 0

while True:
    url = f"{baseurl}page={page}"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.find('h1').text.strip()

    table = soup.find('table', class_='views-table')
    if not table:
        print("No table found.")
        break

    tbody = table.find('tbody')
    if not tbody:
        print("No tbody found.")
        break

    for row in tbody.find_all('tr'):
        courts = row.find('td', class_='views-field views-field-solr-document-5')
        courts = courts.text.strip() if courts else ''

        filenumber = row.find('td', class_='views-field views-field-Numarul-dosarului')
        filenumber = filenumber.text.strip() if filenumber else ''

        nameofdossier = row.find('td', class_='views-field views-field-Denumirea-dosarului')
        nameofdossier = nameofdossier.text.strip() if nameofdossier else ''

        dateofdelivery = row.find('td', class_='views-field views-field-solr-document-1')
        dateofdelivery = dateofdelivery.text.strip() if dateofdelivery else ''

        dateofregistration = row.find('td', class_='views-field views-field-solr-document')
        dateofregistration = dateofregistration.text.strip() if dateofregistration else ''

        publishedDate = row.find('td', class_='views-field views-field-solr-document-2')
        publishedDate = publishedDate.text.strip() if publishedDate else ''

        typeoffolder = row.find('td', class_='views-field views-field-Tipul-dosarului')
        typeoffolder = typeoffolder.text.strip() if typeoffolder else ''

        dossiertopics = row.find('td', class_='views-field views-field-Tematica-dosarului')
        dossiertopics = dossiertopics.text.strip() if dossiertopics else ''

        judge = row.find('td', class_='views-field views-field-solr-document-3')
        judge = judge.text.strip() if judge else ''

        urlPDF = row.find('td', class_='views-field views-field-nothing')
        linkPDF = urlPDF.find('a', href=True)
        urlPDF = 'https://instante.justice.md/ro/' + linkPDF['href'] if linkPDF else ''

        data_50_0415 = {
            'Denumirea dosarului': nameofdossier,
            'Tematica dosarului': dossiertopics,
            'Tipul dosarului': typeoffolder,
            'Numărul dosarului': filenumber,
            'Data înregistrării': "'" + dateofregistration,
            'Data publicării': "'" + publishedDate,
            'Data pronunțării': "'" + dateofdelivery,
            'Instanțe judecătorești': courts,
            'Judecător': judge,
            'Links Act judecătoresc / URL PDF': urlPDF,
            'Page Category': title
        }
        data.append(data_50_0415)
        print('Saving', data_50_0415['Denumirea dosarului'], data_50_0415['Instanțe judecătorești'], data_50_0415['Judecător'], data_50_0415['Numărul dosarului'], data_50_0415['Tematica dosarului'])

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)

    page += 1
