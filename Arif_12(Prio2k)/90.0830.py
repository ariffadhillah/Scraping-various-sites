import requests
import csv

url = "https://fmaregister-api.fma-li.li/api/v1/search?query=&registerNumber=&category=72&category=22&searchType=active&sortColumn=name&ascending=true&page=0"

payload = {}
headers = {
		'authority': 'fmaregister-api.fma-li.li',
		'accept': 'application/json, text/plain, */*',
		'accept-language': 'en-US,en;q=0.9',
		'cache-control': 'no-cache',
		'dnt': '1',
		'origin': 'https://fmaregister.fma-li.li',
		'pragma': 'no-cache',
		'referer': 'https://fmaregister.fma-li.li/',
		'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Microsoft Edge";v="116"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-site',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69'
}

response = requests.request("GET", url, headers=headers, data=payload)

save_data = []
fields = ['Name' , 'National ID' , 'Adresse' , 'Phone' , 'Email' , 'Registration Details' , 'Art' , 'Erteilt']
filename = '90.0830.csv'

if response.status_code == 200:
	dataJson = response.json()
	data_API = dataJson['data']

	for info in data_API:
		name = info['description']
		crmId = info['crmId']
		# phone = info['phone']

		phone = info.get('phone', '')
		if phone is None:
			phone = ''

		email = info.get('email', '')
		if email is None:
			email = ''

		# website = info['website']
		address = info['address']

		grants = info['grants']
		for info_grants in grants:
			restrictionsDe = info_grants.get('restrictionsDe', '')
			if restrictionsDe is None:
				restrictionsDe = ''

			registeredTextDe = info_grants.get('registeredTextDe', '')
			if registeredTextDe is None:
				registeredTextDe = ''

			grantType = info_grants['grantType']			
			if grantType:
				descriptionGerman = grantType.get('descriptionGerman', '')
				if descriptionGerman is None:
					descriptionGerman = ''

		data_save = {
			'Name' : name,
			'National ID' : crmId,
			'Adresse' : address,
			'Phone' : phone,
			'Email': email,
			'Registration Details' : restrictionsDe,
			'Art' : descriptionGerman,
			'Erteilt' : registeredTextDe
		}
		save_data.append(data_save)
		print('Saving', data_save['Name'])
		with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
			writer = csv.DictWriter(csvfile, fieldnames=fields)
			writer.writeheader()
			writer.writerows(save_data)


else:
	print("Error Status ", response.status_code)