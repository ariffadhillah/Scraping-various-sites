import requests
import csv
import time

data = []

url = "https://gbpa.com/scripts/inc/licensees/ssp.php"
params = {
    "draw": 0,
    "columns[0][data]": 0,
    "columns[0][name]": "",
    "columns[0][searchable]": True,
    "columns[0][orderable]": True,
    "columns[0][search][value]": "",
    "columns[0][search][regex]": False,
    "columns[1][data]": 1,
    "columns[1][name]": "",
    "columns[1][searchable]": True,
    "columns[1][orderable]": True,
    "columns[1][search][value]": "",
    "columns[1][search][regex]": False,
    "order[0][column]": 0,
    "order[0][dir]": "asc",
    "start": 0,  # Start from the first record
    "length": 100,
    "search[value]": "",
    "search[regex]": False,
}

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183',
    'Cookie': '_ga=GA1.1.1317144421.1690161008; _ga_JYDDYPD2MB=GS1.1.1690347093.6.1.1690347093.0.0.0'
}

fields = ['Category', 'Client Name', 'Trade Name 1', 'Trade Name 2', 'Trade Name 3', 'Trade Name 4']
filename = '90.2443.csv'

def scrape_data(start):
    params["start"] = start
    while True:
        try:
            response = requests.get(url, params=params, headers=header)
            if response.status_code == 200:
                dataAPI = response.json()
                data_api = dataAPI["data"]

                if len(data_api) == 0:
                    break

                for data_list in data_api:
                    category = data_list['0']
                    client_Name = data_list['1']
                    trade_Name_1 = data_list['2']
                    trade_Name_2 = data_list['3']
                    trade_Name_3 = data_list['4']
                    value_4 = data_list['5']

                    data_90_2443 = {
                        'Category': category,
                        'Client Name': client_Name,
                        'Trade Name 1': trade_Name_1,
                        'Trade Name 2': trade_Name_2,
                        'Trade Name 3': trade_Name_3,
                        'Trade Name 4': value_4
                    }
                    data.append(data_90_2443)
                    print('Saving', data_90_2443['Category'])

                time.sleep(1)  # Increased sleep time to 1 second
                params["start"] += len(data_api)
            else:
                print("Permintaan tidak berhasil. Kode status:", response.status_code)
                continue
        except requests.exceptions.RequestException as e:
            
            print("Terjadi kesalahan saat mengirim permintaan:", e)
            continue

if __name__ == "__main__":
    scrape_data(0)
    # scrape_data(2437)

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)
