import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.onenation.org.au/team'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62'
}

data = []

fields = ['Names', 'PII']
filename = '20.0655.csv'

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

find_item = soup.find_all('div', class_='col-lg-4 my-3')

list_item_url = []

for list_a in find_item:
    find_a = 'https://www.onenation.org.au' + list_a.find('a', class_='')['href']
    list_item_url.append(find_a)

for item_url in list_item_url:
    
    r = requests.get(item_url, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')


    # find_content = soup.find('main', id='content')

    name = soup.find('h2', class_='headline mb-3').text.strip()


    desc = soup.find('div', {'class': ['col-12 col-lg-9 mx-auto','col-12 col-lg-10 mx-auto']} )
    text_p_elements = desc.find_all('p')
    text_PII = "\n\n".join([p.get_text() for p in text_p_elements if not p.find('a')])

    # print(item_url)
    # print(name)
    # print(text_PII.replace('Do you like this page?',''))
    # print( )

    data_save = {
        'Names' : name,
        'PII': text_PII.replace('Do you like this page?','')
    }
    data.append(data_save)
    print('Saving', data_save['Names'])
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)

