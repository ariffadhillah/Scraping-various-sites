# import pandas as pd
# import requests
# from bs4 import BeautifulSoup
# import json
# import re
# import csv

# baseurl = 'https://www.consob.it/web/consob-and-its-activities/warnings?viewId=ultime_com_tutela'
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.51'
# }

# fields = ['Contains info', 'Warnings CONSAB' , 'Warning URL' , 'PAGE URL']
# filename = '40.0167.csv'

# data = []

# r = requests.get(baseurl, headers=headers)
# soup = BeautifulSoup(r.content, 'lxml')

# sectionWarning = soup.find('ul', class_='ultimecomtutela')
# for elementLi in sectionWarning.find_all('li'):
#     try:
#         titleHeader = elementLi.find('div', class_='header').text.strip().replace('\n', ' ')
#         print(titleHeader)
#     except:
#         titleHeader = ''

#     for textP in elementLi.find_all('div', class_='documentContent consobContent'):
#         # print(textP.text.strip())
#         for anchor in textP.find_all('a'):
#             url = anchor.get('href')

#             data_40_0291 = {
#                 'Contains info' : textP.text.strip(),
#                 'Warnings CONSAB': titleHeader,
#                 'Warning URL': 'https://www.consob.it' + url,
#                 'PAGE URL' : baseurl
#             }
#             data.append(data_40_0291)
#             print('Saving', data_40_0291['Warnings CONSAB'])

#             with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
#                 writer = csv.DictWriter(csvfile, fieldnames=fields)
#                 writer.writeheader()
#                 writer.writerows(data)

#         print(f"Data telah disimpan dalam file {filename}")




# import pandas as pd
# import requests
# from bs4 import BeautifulSoup
# import json
# import re
# import csv

# baseurl = 'https://www.consob.it/web/consob-and-its-activities/warnings?viewId=ultime_com_tutela'
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.51'
# }

# fields = ['Contains info', 'Warnings CONSAB', 'Warning URL', 'PAGE URL']
# filename = '40.0167.csv'

# data = []

# r = requests.get(baseurl, headers=headers)
# soup = BeautifulSoup(r.content, 'lxml')

# sectionWarning = soup.find('ul', class_='ultimecomtutela')
# for elementLi in sectionWarning.find_all('li'):
#     try:
#         titleHeader = elementLi.find('div', class_='header').text.strip().replace('\n', ' ')
#         print(titleHeader)
#     except:
#         titleHeader = ''

#     for textP in elementLi.find_all('div', class_='documentContent consobContent'):
#         # print(textP.text.strip())
#         try:
#             for anchor in textP.find_all('a'):
#                 url = anchor.get('href')
#         except:
#             None
#             # if url is not None:
#         data_40_0291 = {
#             'Contains info': textP.text.strip(),
#             'Warnings CONSAB': titleHeader,
#             'Warning URL': 'https://www.consob.it' + url,
#             'PAGE URL': baseurl
#         }
#         data.append(data_40_0291)
#         print('Saving', data_40_0291['Warnings CONSAB'])

# with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=fields)
#     writer.writeheader()
#     writer.writerows(data)


# print(f"Data telah disimpan dalam file {filename}")



# import pandas as pd
# import requests
# from bs4 import BeautifulSoup
# import json
# import re
# import csv

# baseurl = 'https://www.consob.it/web/consob-and-its-activities/warnings?viewId=ultime_com_tutela'
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.51'
# }

# fields = ['Contains info', 'Warnings CONSAB', 'Warning URL', 'PAGE URL']
# filename = '40.0167.csv'

# data = []

# r = requests.get(baseurl, headers=headers)
# soup = BeautifulSoup(r.content, 'lxml')

# sectionWarning = soup.find('ul', class_='ultimecomtutela')
# for elementLi in sectionWarning.find_all('li'):
#     try:
#         titleHeader = elementLi.find('div', class_='header').text.strip().replace('\n', ' ')
#         print(titleHeader)
#     except:
#         titleHeader = ''

#     for textP in elementLi.find_all('div', class_='documentContent consobContent'):
#         url_list = [] 
#         try:
#             for anchor in textP.find_all('a'):
#                 url = anchor.get('href')
#                 if url is not None:
#                     url_list.append(url)
#         except:
#             pass
            
#         data_40_0291 = {
#             'Contains info': textP.text.strip(),
#             'Warnings CONSAB': titleHeader,
#             'Warning URL': url_list.replace("['",'').replace("']",'') ,  
#             'PAGE URL': baseurl
#         }
#         data.append(data_40_0291)
#         print('Saving', data_40_0291['Warnings CONSAB'])

# with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=fields)
#     writer.writeheader()
#     writer.writerows(data)

# print(f"Data telah disimpan dalam file {filename}")


import pandas as pd
import requests
from bs4 import BeautifulSoup
import json
import re
import csv

baseurl = 'https://www.consob.it/web/consob-and-its-activities/warnings?viewId=ultime_com_tutela'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.51'
}

fields = ['Contains info', 'Warnings CONSAB', 'Warning URL', 'PAGE URL']
filename = '40.0167.csv'

data = []

r = requests.get(baseurl, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

sectionWarning = soup.find('ul', class_='ultimecomtutela')
for elementLi in sectionWarning.find_all('li'):
    try:
        titleHeader = elementLi.find('div', class_='header').text.strip().replace('\n', ' ')
        print(titleHeader)
    except:
        titleHeader = ''

    for textP in elementLi.find_all('div', class_='documentContent consobContent'):
        url_list = [] 
        try:
            for anchor in textP.find_all('a'):
                url = anchor.get('href')
                if url is not None:
                    url_list.append(url)
        except:
            pass
            
        data_40_0291 = {
            'Contains info': textP.text.strip(),
            'Warnings CONSAB': titleHeader,
            'Warning URL': ', '.join(url_list).replace(',' , '\n'),
            'PAGE URL': baseurl
        }
        data.append(data_40_0291)
        print('Saving', data_40_0291['Warnings CONSAB'])

with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(data)

print(f"Data telah disimpan dalam file {filename}")
