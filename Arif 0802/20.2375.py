import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.bci.ao/umbraco/Surface/BCIGoverningBodies/GetDepartmentPeopleList?parentId=1791&_=1691162503707"

payload = {}
headers = {
		'Cookie': 'SERVERID=s1'
}

response = requests.request("GET", url, headers=headers, data=payload)

fields = ['Names', 'Roles' , 'Titles', 'Biography']
filename = '20.2375.csv'

data = []

dataAPI = response.json()
data_api = dataAPI["list"]
for data_list in data_api:
    title = data_list['Name']
    people_ = data_list['People']
    for info in people_:
        name = info['Name']
        roles = info['Cargo']
        biography_html  = info['Biography']

        if biography_html is not None:
            soup = BeautifulSoup(biography_html, 'html.parser')
            biography_text = soup.get_text()
            biography = biography_text.strip()
        else:
            biography = ''
        
        data_20_2375 = {
            'Names' : name,
            'Roles' : roles,
            'Titles' : title,
            'Biography' : biography
        }

        data.append(data_20_2375)
        print('Saving', data_20_2375['Names'])
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            for item in data:
                writer.writerow(item) 


        
    
