import requests
import time
import csv

url = "https://clientportal.jse.co.za/_vti_bin/JSE/CustomerRoleService.svc/GetAllIssuers"

data = []
fields = ['Name' , 'ISN Number' , 'Registration No' , 'Tell' , 'Fax' , 'Email' , 'Website' , 'Postal Address' , 'Physical Address' , 'Status']
filename = '90.0496.csv'

payload = "{\"filterLongName\":\"\",\"filterType\":\"Equity Issuer\"}"
headers = {
		'authority': 'clientportal.jse.co.za',
		'accept': 'application/json, text/javascript, */*; q=0.01',
		'accept-language': 'en-US,en;q=0.9',
		'cache-control': 'no-cache',
		'content-type': 'application/json;',
		'cookie': '__cf_bm=R1PkJWHtUQ8KUI.IersFqPz6oNoENLwJsxjqi7shsjw-1693732988-0-AfSFpWCHjSQfzWBBhyZBtm9QI+WGqYCilC60ZXtRt+XdKZNB8YtFouwLYWk6C16JMRSD47B1A/3nbb5eVjjIg9Y=; _gid=GA1.3.865336066.1693732988; WSS_FullScreenMode=false; _ga_4BW00CB80P=GS1.3.1693732988.1.1.1693733235.0.0.0; _ga_W5730Z4MGN=GS1.1.1693732987.1.1.1693733572.60.0.0; _ga=GA1.3.1528096912.1693732988; _gat_UA-221280167-1=1; _gat_gtag_UA_1233571_1=1; __cf_bm=A_OxfdRNEsr7E0KqCmLMxysT7aIK3Hm4TZBcLbOSBxo-1693733754-0-AY3bbSllUJxYlWCPpN56OT/Y1xlLgjLquJWJkcRm/ZwEGY3fQ2WDYsbOc0HFfOXjw435ZLv8qJ1v9h4JobFSLlA=',
		'dnt': '1',
		'origin': 'https://clientportal.jse.co.za',
		'pragma': 'no-cache',
		'referer': 'https://clientportal.jse.co.za/companies-and-financial-instruments',
		'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Microsoft Edge";v="116"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69',
		'x-requested-with': 'XMLHttpRequest'
}



try:
    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code == 200:
        data_api = response.json()

        for info_API in data_api:
            companyName = info_API["LongName"]
            telephoneNumber = info_API["TelephoneNumber"]
            faxNumber = info_API["FaxNumber"]
            emailAddress = info_API["EmailAddress"]
            website = info_API["Website"]
            registrationNumber = info_API["RegistrationNumber"]
            postalAddress = info_API["PostalAddress"]
            physicalAddress = info_API["PhysicalAddress"]
            status = info_API["Status"]            

            master_id = info_API["MasterID"]
            urlDetail = "https://clientportal.jse.co.za/_vti_bin/JSE/SharesService.svc/GetAllInstrumentsForIssuer"
            payloadDetails = {"issuerMasterId": master_id}

            try:
                responseDetails = requests.request("POST", urlDetail, headers=headers, json=payloadDetails)

                if responseDetails.status_code == 200:
                    api_PageDetails = responseDetails.json()
                    try:
                        isin = api_PageDetails['GetAllInstrumentsForIssuerResult'][0]['ISIN']
                    except:
                        isin = ''
                    
                    # Menampilkan setiap detail
                    # print("Name:", companyName)
                    # print("ISIN:", isin)
                    # print("Status:", status)
                    # print("No registrationNumber:", registrationNumber)
                    # print("Email Address:", emailAddress)
                    # print("Fax Number:", faxNumber)
                    # print("Physical Address:", physicalAddress)
                    # print("Postal Address:", postalAddress)
                    # print()
                    
                    time.sleep(1)

                    data_save = {
                        'Name' : companyName,
                        'ISN Number' : isin,
                        'Registration No' : registrationNumber, 
                        'Tell' : telephoneNumber,
                        'Fax' : faxNumber,
                        'Email' : emailAddress,
                        'Website' : website,
                        'Postal Address' : postalAddress,
                        'Physical Address' : physicalAddress,
                        'Status' : status                        
                    }
                    data.append(data_save)
                    print('Saving', data_save['Name'])
                    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                        writer = csv.DictWriter(csvfile, fieldnames=fields)
                        writer.writeheader()
                        writer.writerows(data)
                    
                    time.sleep(1)

                else:
                    print("Error Status Respons Detail Page", responseDetails.status_code)

            except requests.exceptions.RequestException as e:
                print("Requests Error ", e)

    else:
        print("Error Status ", response.status_code)

except requests.exceptions.RequestException as e:
    print("Requests Error ", e)



