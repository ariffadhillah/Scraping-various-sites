import requests
import time
import csv

base_url = "https://edesk.apps.cssf.lu/search-entities-api/api/v1/entite?"

data = []

fields = ['Name' , 'Type' , 'Code' , 'LEI code' , 'Validity date', 'Address', 'Link to Firm Details']
filename = '90.0792.csv'

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
    url  = f"{base_url}page={page}&size=100&st=advanced&entType=IF&sort=entiteType,asc&sort=entiteName,asc"
    print(url)

    response = requests.request("GET", url, headers=headers, data=payload)

    # print(response.text)

    if response.status_code == 200:
        dataJson = response.json()
        data_API = dataJson['content']
        for info_API in data_API:
            entiteId = info_API['entiteId']
            urlDetail = f"https://edesk.apps.cssf.lu/search-entities-api/api/v1/entite/{entiteId}"

            try:
                responseDetails = requests.request("GET", urlDetail, headers=headers)
                dataDetails = responseDetails.json()

                entiteType = dataDetails.get('entiteType', '')
                if entiteType is None:
                    entiteType = ''

                entiteCode = dataDetails.get('entiteCode', '')
                if entiteCode is None:
                    entiteCode = ''

                entiteName = dataDetails.get('entiteName', '')
                if entiteName is None:
                    entiteName = ''

                leiCode = dataDetails.get('leiCode', '')
                if leiCode is None:
                    leiCode = ''

                entiteAddress = dataDetails.get('entiteAddress', '')
                if entiteAddress is None:
                    entiteAddress = ''

                dtDebValid = dataDetails.get('dtDebValid', '')
                if dtDebValid is None:
                    dtDebValid = ''

                # print(entiteType)
                # print(entiteCode)
                # print(entiteName)
                # print(leiCode)
                # print(dtDebValid)
                # print(entiteAddress)
                # print()
                                
                data_save = {
                    'Name' : entiteName,
                    'Type' : entiteType,           
                    'Code' : entiteCode,           
                    'LEI code' : leiCode,
                    'Validity date' : dtDebValid,
                    'Address' : entiteAddress,
                    'Link to Firm Details' : 'https://edesk.apps.cssf.lu/search-entities/entite/details/' + str(entiteId) + '?lng=en&q=&st=advanced&entType=IF'
                }
                data.append(data_save)
                print('Saving', data_save['Name'])
                print('Saving', data_save['Link to Firm Details'])
                print( )
                with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=fields)
                    writer.writeheader()
                    writer.writerows(data)
                
            except requests.exceptions.RequestException as e:
                print("Requests Error ", e)

            # time.sleep(1)


    else:
        print("Error Status ", response.status_code)

    page += 1

