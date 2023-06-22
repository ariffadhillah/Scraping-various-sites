# fileName 40.0204 

import requests
import json
import csv

url = "http://emo.krx.co.kr/contents/EMO/99/EMO99000001.jspx"

payload = "market_gubun=ALL&fromDate=20220618&toDate=20230618&pagePath=%2Fcontents%2FSVL%2FE%2F05010200%2FEMO05010200.jsp&code=MuaN3ngkgwbAZukGaa2yo1HBTpuzOaQwujONxF1eEOY%2FnMtWM3der87JdbYLcDhK%2BHQq9%2FeVuOzUfeQoiC7ygSi04zlZZ30KlSS1O8PrUbxHc5fH22L4bv1x4UAuJjVyEIr3YPHuX7ZgF2FkF23puw4IYE8SU7XJKeBaaQiN1j5LHxgh%2Fr8AVozdBA1GP%2F5e&pageFirstCall=Y"
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'SCOUTER=x55k5ffn2l1rf0; __utmz=203361797.1686887744.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _ga=GA1.1.160033924.1686887745; JSESSIONID=341E2F09A5BA0B2D2838B3F08BAE8E64.102tomcat2; __utma=203361797.163848093.1686887744.1686887744.1687016926.2; __utmc=203361797; __utmt=1; _ga_3S72WFFYZB=GS1.1.1687016926.2.1.1687017078.0.0.0; __utmb=203361797.2.10.1687016926; SCOUTER=x2jli5m8jsst5; JSESSIONID=51A14D5AF728AE99FB961AEA6415341A.57tomcat2',
    'DNT': '1',
    'Origin': 'http://emo.krx.co.kr',
    'Pragma': 'no-cache',
    'Referer': 'http://emo.krx.co.kr/contents/SVL/E/05010200/EMO05010200.jsp',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.51',
    'X-Requested-With': 'XMLHttpRequest'
}

response = requests.post(url, headers=headers, data=payload)

if response.status_code == 200:
    try:
        data = json.loads(response.text)  # Parsing data JSON

        ds1_data = data['DS1']

        with open('40.0204.csv', mode='w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Current Price', 'Change', 'Disclosure Date', 'Designation', 'Code'])

            for item in ds1_data:
                name = item.get('isu_nm')
                current_price = item.get('isu_cur_pr')
                change = item.get('prv_dd_cmpr')
                disclosure_date = item.get('act_dd')
                designation = item.get('design_dd')
                code = item.get('isu_srt_cd')

                writer.writerow([name, current_price, change, disclosure_date, designation, code])

        print("Data has been saved to 40.0204.csv")

    except json.JSONDecodeError as e:
        print("Error parsing JSON:", e)

else:
    print("Error:", response.status_code)
