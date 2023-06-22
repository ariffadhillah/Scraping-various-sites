import csv
import requests
from bs4 import BeautifulSoup

baseurl = 'https://acpr.banque-france.fr/en/sanctions/jurisprudence'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43'
}

r = requests.get(baseurl, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

data = []

title = soup.find('h1', class_='titre').text.strip()

tab_list = soup.find('div', class_='field-collection-container clearfix')
tabs_years = tab_list.find('div', class_='item-list')

list_years = []
for years in tabs_years.find_all('a'):
    list_years.append(years.text)

list_content = soup.find('div', class_='field-collection-container clearfix')
content = list_content.find_all('div', class_='field-item even rich-text')


with open('40.0113.csv', 'w', newline='' , encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Name','Links Document', 'Month', 'Year', 'Document Name' ])

    for index, year in enumerate(list_years):
        names = content[index].find_all('li')

        for name in names:
            name_text = name.text.strip()
            link = name.find('a')['href']
            links_Document = 'https://acpr.banque-france.fr' + link 
            month = name.find_previous('h2').text.strip()
            # date_of_order = "'" + month + ' - ' +  year

            fileName_40_0113 = {
                "Name": name_text,
                "Links Document": links_Document.replace('https://acpr.banque-france.frhttps://acpr.banque-france.fr/','https://acpr.banque-france.fr/'),
                # "Date of Order": date_of_order,
                "Month": month,
                "Year": year,
                "Document Name": title,
            }
            data.append(fileName_40_0113)
            print('Saving', fileName_40_0113['Name'])

            writer.writerow([fileName_40_0113['Name'],  fileName_40_0113['Links Document'], fileName_40_0113['Month'], fileName_40_0113['Year'], fileName_40_0113['Document Name'] ])
