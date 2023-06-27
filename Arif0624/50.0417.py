import requests
from bs4 import BeautifulSoup
import csv

baseurl = 'https://instante.justice.md/ro/citatii-publice?Instance=All&Numarul_dosarului=&solr_document_3=&PersoanaCitata=&solr_document_2=&'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.51'
}

fields = ['Denumirea dosarului', 'Instanțe judecătorești', 'Numărul dosarului', 'Obiectul cauzei', 'Data ședinței',
          'Ora ședinței', 'Persoana citată', 'Sala ședinței', 'Judecător', 'Data publicării',
          'Links Act judecătoresc / URL PDF', 'Page Category']
filename = '50.0417.csv'

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
                instanțejudecătorești = row.find('td', class_='views-field views-field-solr-document-5')
                instanțejudecătorești = instanțejudecătorești.text.strip() if instanțejudecătorești else ''

                număruldosarului = row.find('td', class_='views-field views-field-Numarul-dosarului')
                număruldosarului = număruldosarului.text.strip() if număruldosarului else ''

                denumireadosarului = row.find('td', class_='views-field views-field-solr-document-4')
                denumireadosarului = denumireadosarului.text.strip() if denumireadosarului else ''

                obiectulcauzei = row.find('td', class_='views-field views-field-Tematica-dosarului')
                obiectulcauzei = obiectulcauzei.text.strip() if obiectulcauzei else ''

                dataședinței = row.find('td', class_='views-field views-field-solr-document')
                dataședinței = dataședinței.text.strip() if dataședinței else ''

                oraședinței = row.find('td', class_='views-field views-field-solr-document-1')
                oraședinței = oraședinței.text.strip() if oraședinței else ''

                persoanacitată = row.find('td', class_='views-field views-field-solr-document-2')
                persoanacitată = persoanacitată.text.strip() if persoanacitată else ''

                salaședinței = row.find('td', class_='views-field views-field-solr-document-6')
                salaședinței = salaședinței.text.strip() if salaședinței else ''

                judecător = row.find('td', class_='views-field views-field-solr-document-8')
                judecător = judecător.text.strip() if judecător else ''

                datapublicării = row.find('td', class_='views-field views-field-solr-document-3')
                datapublicării = datapublicării.text.strip() if datapublicării else ''

                urlPDF = row.find('td', class_='views-field views-field-nothing')
                linkPDF = urlPDF.find('a', href=True)
                urlPDF = 'https://instante.justice.md/ro/' + linkPDF['href'] if linkPDF else ''

                data_50_0417 = {
                    'Denumirea dosarului': denumireadosarului,
                    'Instanțe judecătorești': instanțejudecătorești,
                    'Numărul dosarului': număruldosarului,
                    'Obiectul cauzei': obiectulcauzei,
                    'Data ședinței': "'" + dataședinței,
                    'Ora ședinței': oraședinței,
                    'Persoana citată': persoanacitată,
                    'Sala ședinței': salaședinței,
                    'Judecător': judecător,
                    'Data publicării':"'" + datapublicării,
                    'Links Act judecătoresc / URL PDF': urlPDF,
                    'Page Category': title
                }
                data.append(data_50_0417)
                print('Saving', data_50_0417['Denumirea dosarului'], data_50_0417['Instanțe judecătorești'],
                      data_50_0417['Numărul dosarului'])

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
