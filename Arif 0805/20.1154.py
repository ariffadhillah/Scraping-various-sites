import requests
import json
from bs4 import BeautifulSoup
import csv

def find_key_recursive(data, target_key):
    results = []
    
    if isinstance(data, dict):
        for key, value in data.items():
            if key == target_key:
                results.append(value)
            else:
                results.extend(find_key_recursive(value, target_key))
    elif isinstance(data, list):
        for item in data:
            results.extend(find_key_recursive(item, target_key))
    
    return results

url = "https://www.gov.ky/_cache_a50b/pages/604.json"

headers = {
    'Cookie': 'JSESSIONID=Qd3WlQtflJYGviL-PD41pdGSYuCJ0O6NFGFV1fQD87AhomIG2Ejs!-1117414379; sticky=be7970e3b4089720'
}

fields = ["Governor's Appointees"]
filename = '20.1154.csv'

data_saave = []

response = requests.get(url, headers=headers)

if response.status_code == 200:
    dataAPI = response.json()

    target_key = "userText"

    user_text_data = find_key_recursive(dataAPI, target_key)

    if len(user_text_data) >= 4:
        third_user_text = user_text_data[4]
        
        soup = BeautifulSoup(third_user_text, 'html.parser')
        ul_li_elements = soup.find_all('ul', recursive=True)[2]
        
        for ul_li in ul_li_elements.find_all('li'):
            name = ul_li.text

            data_20_1154 = {
                "Governor's Appointees" :  name
            }
            data_saave.append(data_20_1154)
            print('Saving', data_20_1154["Governor's Appointees"])
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fields)
                writer.writeheader()
                writer.writerows(data_saave)
    else:
        print(" ")
else:
    print(" ", response.status_code)
