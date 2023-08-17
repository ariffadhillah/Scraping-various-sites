# import requests
# from bs4 import BeautifulSoup
# import csv
# import re

# url = 'https://osc.gov/Pages/Leadership.aspx'

# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203'
# }

# fields = ['']
# filename = '20.3322.csv'

# data = []

# r = requests.get(url, headers=headers)
# soup = BeautifulSoup(r.content, 'lxml')

# listbio = []
# processed_urls = set()

# find_section = soup.find('div', id='DeltaPlaceHolderMain')
# print(find_section)




import requests
import re
from bs4 import BeautifulSoup
import json
import html
import csv



url = "https://osc.gov/Pages/Leadership.aspx"

payload = {}
headers = {
		'authority': 'osc.gov',
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		'accept-language': 'en-US,en;q=0.9',
		'cache-control': 'no-cache',
		'cookie': 'ai_user=Ud4rY|2023-08-15T21:52:33.275Z; WSS_FullScreenMode=false; ai_session=/ruLU|1692169583364.5|1692169583364.5',
		'dnt': '1',
		'pragma': 'no-cache',
		'sec-ch-ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
		'sec-fetch-dest': 'document',
		'sec-fetch-mode': 'navigate',
		'sec-fetch-site': 'none',
		'sec-fetch-user': '?1',
		'upgrade-insecure-requests': '1',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203'
}

r = requests.get(url, headers=headers, data=payload)
soup = BeautifulSoup(r.content, 'html.parser')

data = []

fields = ['Names','Roles','Biography']
filename = '20.3322.csv'

# <script type="text/javascript">
scaript = soup.find_all('script')[62].text.strip()[9405:-7068] + '}'

# print(scaript)

data_json = json.loads(scaript)

dataraw =  data_json['Row']

for info in dataraw:
    name = info['FullName']
    jobTitle = info['JobTitle']
    bio_html = info['Bio']  
    
    
    soup = BeautifulSoup(bio_html, 'html.parser')
    
    
    bio_text = html.unescape(soup.get_text())

    data_save = {
        'Names' : name.strip(),
        'Roles' : jobTitle.strip(),
        'Biography' : bio_text.strip()
    }
    data.append(data_save)
    print('Saving', data_save['Names'])
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)


