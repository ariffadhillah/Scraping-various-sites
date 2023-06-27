import requests
from bs4 import BeautifulSoup
import csv

baseurl = 'https://instante.justice.md/ro/incheierile-instantei?Instance=All&Denumirea_dosarului=&Numarul_dosarului=&date=&Tematica_dosarului=&Tipul_dosarului=All&'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.51'
}

fields = ['Denumirea dosarului', 'Instanțe judecătorești' , 'Numărul dosarului' , 'Data înregistrării' , 'Data publicării' , 'Tipul dosarului' , 'Tematica dosarului' , 'Judecător' , 'Links Act judecătoresc / URL PDF' , 'Page Category']
filename = '50.0416.csv'

data = []
page = 0
while True:
    url = f"{baseurl}page={page}"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    title = soup.find('h1').text.strip()

    table = soup.find('table', class_='views-table')
    if table:
        tbody = table.find('tbody')
        if tbody:
            for row in tbody.find_all('tr'):
                instanțejudecătorești = row.find('td', class_='views-field views-field-solr-document-4')
                instanțejudecătorești = instanțejudecătorești.text.strip() if instanțejudecătorești else ''

                număruldosarului = row.find('td', class_='views-field views-field-Numarul-dosarului')
                număruldosarului = număruldosarului	.text.strip() if număruldosarului else ''

                denumireadosarului = row.find('td', class_='views-field views-field-Denumirea-dosarului')
                denumireadosarului = denumireadosarului.text.strip() if denumireadosarului else ''

                dataînregistrării = row.find('td', class_='views-field views-field-solr-document')
                dataînregistrării = dataînregistrării.text.strip() if dataînregistrării else ''

                datapublicării = row.find('td', class_='views-field views-field-solr-document-1')
                datapublicării = datapublicării.text.strip() if datapublicării else ''

                tipuldosarului = row.find('td', class_='views-field views-field-Tipul-dosarului')
                tipuldosarului = tipuldosarului.text.strip() if tipuldosarului else ''

                tematicadosarului = row.find('td', class_='views-field views-field-Tematica-dosarului')
                tematicadosarului = tematicadosarului.text.strip() if tematicadosarului else ''

                judecător = row.find('td', class_='views-field views-field-solr-document-2')
                judecător = judecător.text.strip() if judecător else ''

                urlPDF = row.find('td', class_='views-field views-field-nothing')
                linkPDF = urlPDF.find('a', href=True)
                urlPDF = 'https://instante.justice.md/ro/' + linkPDF['href'] if linkPDF else ''

                data_50_0416 = {
                    'Denumirea dosarului' : denumireadosarului,
                    'Instanțe judecătorești': instanțejudecătorești,
                    'Numărul dosarului': număruldosarului,
                    'Data înregistrării' : "'" + dataînregistrării,
                    'Data publicării':"'" + datapublicării,
                    'Tipul dosarului': tipuldosarului,
                    'Tematica dosarului': tematicadosarului,
                    'Judecător': judecător,		
                    'Links Act judecătoresc / URL PDF': urlPDF,
                    'Page Category': title
                }

                data.append(data_50_0416)
                print('Saving', data_50_0416['Denumirea dosarului'], data_50_0416['Instanțe judecătorești'],
                      data_50_0416['Numărul dosarului'])

            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fields)
                writer.writeheader()
                for item in data:
                    writer.writerow(item)
        else:
            print("No tbody found.")
            break
    else:
        print("No table found.")
        break

    page += 1
