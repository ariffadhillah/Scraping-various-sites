# import csv
# import requests
# from bs4 import BeautifulSoup

# baseurl = 'https://competition.md/decizii.php?l=en&idc=64&year=&month=&day=&t=/Transparency/Decisions/&'
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.58'
# }

# fields = ['Title' , 'Links Document']
# filename = '40.1145.csv'


# for x in range(1, 13):
#     url = f"{baseurl}page={x}"
#     r = requests.get(url, headers=headers)
#     soup = BeautifulSoup(r.content, 'lxml')
#     print()
#     print(url)
#     print()

#     data = []
#     setionItem = soup.find_all('div', class_='bg17')[2]

#     listItem = setionItem.find('table')

#     if not listItem:
#         print("No table found.")
#         break
    
#     for urlPage in listItem.find_all('a', class_='link_block_title'):
#         urlItem = 'https://competition.md/' + urlPage['href']
#         name = urlPage.text
#         print()
#         print(name, urlItem)
#         print()
#         data_40_1145 = {
#             'Title' : name,
#             'Links Document' : urlItem
#         }
#         data.append(data_40_1145)
#     writer.writerows(data)
#     # with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
#     #     writer = csv.DictWriter(csvfile, fieldnames=fields)
#     #     writer.writeheader()
#     #     writer.writerows(data)





import csv
import requests
from bs4 import BeautifulSoup

baseurl = 'https://competition.md/decizii.php?l=en&idc=64&year=&month=&day=&t=/Transparency/Decisions/&'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.58'
}

fields = ['Title', 'Links Document']
filename = '40.1145.csv'

with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()

    for x in range(1, 13):
        url = f"{baseurl}page={x}"
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.content, 'lxml')
        print()
        print(url)
        print()

        data = []
        setionItem = soup.find_all('div', class_='bg17')[2]
        listItem = setionItem.find('table')

        if not listItem:
            print("No table found.")
            break

        for urlPage in listItem.find_all('a', class_='link_block_title'):
            urlItem = 'https://competition.md/' + urlPage['href']
            name = urlPage.text
            print()
            print(name, urlItem)
            print()
            data_40_1145 = {
                'Title': name.replace('\n',''),
                'Links Document': urlItem
            }
            data.append(data_40_1145)

        writer.writerows(data)
