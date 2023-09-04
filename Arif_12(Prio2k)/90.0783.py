import requests
from bs4 import BeautifulSoup
import csv
import time

base_url = 'https://www.mipa.mu/home/members/MF'
# https://www.mipa.mu/home/members/MF?page=2
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69',
    'Cookie' : 'ci_session=8qma1s1c9s92rvo8nsr1c8qcnqr0v656; _ga_9REZKG3J85=GS1.1.1693815633.1.0.1693815633.0.0.0; _ga=GA1.2.1337831557.1693815634; _gid=GA1.2.1458592699.1693815634; _gat_gtag_UA_148796000_1=1'
}

data = []

fields = ['Company Name' , 'Member Since']
filename = '90.0783.csv'

page = 1
max_page = 13
while page <= max_page:
    time.sleep(2)    
    url  = f"{base_url}?page={page}"
    print(url)

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    find_table = soup.find('table', class_='table table-bordered table-striped')
    find_tbody = find_table.find('tbody')

    time.sleep(1)
    for find_tr in find_tbody.find_all('tr')[1:]:
        find_td = find_tr.find_all('td')
        if find_td:
            companyName = find_td[1].text
            member_Since = find_td[2].text
            # print(companyName)
            # print(member_Since)
            # print( )
    
            data_save = {
                'Company Name' : companyName,
                'Member Since' : member_Since
            }
            time.sleep(.5)
            data.append(data_save)
            print('Saving', data_save['Company Name'])
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fields)
                writer.writeheader()
                writer.writerows(data)



    page += 1
