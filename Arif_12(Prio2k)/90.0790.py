import requests
import time
import csv

base_url = "https://edesk.apps.cssf.lu/search-entities-api/api/v1/entite?"

data = []

fields = ['Type' , 'Code' , 'Name' , 'LEI code' , 'Address']
filename = '90.0790.csv'

payload = {}
headers = {
		'Accept': 'application/json;charset=UTF-8',
		'Accept-Language': 'en-US,en;q=0.9',
		'Cache-Control': 'no-cache',
		'Connection': 'keep-alive',
		'DNT': '1',
		'Pragma': 'no-cache',
		'Sec-Fetch-Dest': 'empty',
		'Sec-Fetch-Mode': 'cors',
		'Sec-Fetch-Site': 'same-origin',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69',
		'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Microsoft Edge";v="116"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"'
}

page = 0
max_page = 1
while page <= max_page:
    time.sleep(2)    
    url  = f"{base_url}page={page}&size=100&st=advanced&entType=B&sort=entiteType,asc&sort=entiteName,asc"
    print(url)

    response = requests.request("GET", url, headers=headers, data=payload)

    # print(response.text)

    if response.status_code == 200:
        dataJson = response.json()
        data_API = dataJson['content']
        # entite_code = data['content'][0]['entiteCode']

        for info_API in data_API:
            entiteType = info_API['entiteType']
            entiteCode = info_API['entiteCode']
            entiteName = info_API['entiteName']
            leiCode = info_API['leiCode']
            entiteAddress = info_API['entiteAddress']

            time.sleep(1)

            data_save = {
                'Type' : entiteType,           
                'Code' : entiteCode,           
                'Name' : entiteName,
                'LEI code' : leiCode,
                'Address' : entiteAddress
            }
            data.append(data_save)
            print('Saving', data_save['Name'])
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fields)
                writer.writeheader()
                writer.writerows(data)

    else:
        print("Error Status ", response.status_code)

    page += 1
