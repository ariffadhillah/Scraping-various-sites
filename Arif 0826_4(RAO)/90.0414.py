import requests
import json

base_url = "https://12366.chinatax.gov.cn/sszyfw/bulletinBoard/getBulletinBoardPage"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62"
}

parameter = {
    'currentPage': 1,
}

response = requests.post(base_url, data=parameter, headers=headers)
if response.status_code == 200:
   print(response.json()) 
    # Ekstrak data JSON dari konten respons
    # json_start = response.content.index(b'(') + 1
    # json_end = response.content.rindex(b')')
    # json_data = response.content[json_start:json_end]

    # # Decode data JSON menjadi string dan kemudian parse sebagai objek JSON
    # json_obj = json_data.decode('utf-8')
    # data_api = json.loads(json_obj)
    # if data_api:
    #     content_ = data_api[0]['content']
    #     if content_:
    #         code = content_[0]['hqcjje']
    #         print(code)
    #         # code = 
    #     # if content:
    #     #     print(code)

    #     # first_name = data_api[0]['hqcjje']
    #     # print("First Name:", first_name)
    # else:
    #     print("No data or invalid JSON structure")
    
    # Akses konten dalam objek JSON
    # content = json_obj['content']
    # print(content)
    # for item in content:
    #     hqbjw1 = item['hqbjw1']
    #     hqbjw2 = item['hqbjw2']
    #     hqbjw3 = item['hqbjw3']
    #     print("hqbjw1:", hqbjw1)
    #     print("hqbjw2:", hqbjw2)
    #     print("hqbjw3:", hqbjw3)
else:
    print("Error:", response.status_code)

# from bs4 import BeautifulSoup
# import requests
# import json
# import csv

# baseurl = 'https://www.bse.cn/products/neeq_listed_companies/company_executives.html?companyCode=872953&typename=G'
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
# }

# r = requests.get(baseurl, headers=headers)
# soup = BeautifulSoup(r.content, 'lxml')

# find_setion = soup.find('div', id='companyExecutive')
# find_table = find_setion.find('table')
# print(find_table)

