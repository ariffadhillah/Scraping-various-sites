# fileName 40.0206

import requests
import json
import csv

url = "http://emo.krx.co.kr/contents/EMO/99/EMO99000001.jspx"

payload = "market_gubun=ALL&fromDate=20220618&toDate=20230618&pagePath=%2Fcontents%2FSVL%2FE%2F05030200%2FEMO05030200.jsp&code=MuaN3ngkgwbAZukGaa2yo%2BqIP1fMgyFOCFKgP5610Sm1kPqie8ehcxcfgYs1CkBjXbUizWhatLGaKJjmymMf7m9BVeyQ%2Fr5Mga1964TZ6Sz95kEdkiXRgIPUTNCWE8pFL1v5xN2WVB%2FhADAChoM00Vv%2FdvoRcQcJrdXg0NBCcroWstju0fvLQ1pWCmC8VZIs&pageFirstCall=Y"
headers = {
  'Accept': 'application/json, text/javascript, */*; q=0.01',
  'Accept-Language': 'en-US,en;q=0.9',
  'Cache-Control': 'no-cache',
  'Connection': 'keep-alive',
  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'Cookie': 'SCOUTER=x55k5ffn2l1rf0; __utmz=203361797.1686887744.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _ga=GA1.1.160033924.1686887745; SCOUTER=x79t8k6dvndh3s; JSESSIONID=F48A6903106C6F2129885E4B4257E407.57tomcat2; __utma=203361797.163848093.1686887744.1687069935.1687081205.7; __utmc=203361797; __utmt=1; __utmb=203361797.10.10.1687081205; _ga_3S72WFFYZB=GS1.1.1687081205.8.1.1687082864.0.0.0; SCOUTER=x2jli5m8jsst5',
  'DNT': '1',
  'Origin': 'http://emo.krx.co.kr',
  'Pragma': 'no-cache',
  'Referer': 'http://emo.krx.co.kr/contents/SVL/E/05030200/EMO05030200.jsp',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.51',
  'X-Requested-With': 'XMLHttpRequest'
}

response = requests.request("POST", url, headers=headers, data=payload)

if response.status_code == 200:
    try:
        data = json.loads(response.text)  # Parsing data JSON

        ds1_data = data['DS1']

        with open('40.0206.csv', mode='w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Current Price', 'Change', 'Disclosure Date', 'Designation', 'Release', 'Code'])

            for item in ds1_data:
                name = item.get('kor_isu_nm')
                current_price = item.get('isu_std_pr')
                change = item.get('prv_dd_cmpr')
                disclosure_date = item.get('act_dd')
                designation = item.get('design_dd')
                release = item.get('free_dt')
                code = item.get('isu_cd')

                writer.writerow([name, current_price, change, disclosure_date, designation, release, code])

        print("Data has been saved to 40.0206.csv")

    except json.JSONDecodeError as e:
        print("Error parsing JSON:", e)

else:
    print("Error:", response.status_code)

