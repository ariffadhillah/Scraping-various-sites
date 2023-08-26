import requests
import csv

url = "https://lsoservice.wyoleg.gov/api/legislator/2023/S"

fields = ['Names' , 'Party' , 'Phone' , 'Email' , 'District' , 'County' ,  'Address']

filename = '20.0432.csv'

payload = {}
headers = {
    'Cookie': 'ARRAffinity=b94576c2d163020e8817f221b76de4b33a22a5901de8abf953ffba7f6962ecc3; ARRAffinitySameSite=b94576c2d163020e8817f221b76de4b33a22a5901de8abf953ffba7f6962ecc3'
}

response = requests.request("GET", url, headers=headers, data=payload)

data_api = response.json()

data_item = []  # Inisialisasi data sebagai daftar kosong

if isinstance(data_api, list) and len(data_api) > 0:
    for data in data_api:
        name = data['name']
        party = data['party']
        district_ = data['district']
        county = data['county']
        address_ = data['address']
        city = data['city']
        state = data['state']
        zip = data['zip']
        address = address_ + ' ' + city + ', ' + state + ' ' + zip
        phone = data['phone']
        eMail = data['eMail']

        data_save = {
            'Names': name,
            'Party': party,
            'Phone' : phone,
            'Email' : eMail,
            'District' : district_,
            'County' : county,
            'Address' : address
        }
        
        data_item.append(data_save)  # Menambahkan data_save ke dalam daftar data

else:
    print("No data or invalid JSON structure")


print('Saving', len(data_item), 'Names')
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(data_item)
