from bs4 import BeautifulSoup
import requests
import json
import csv

baseurl = 'http://swt.gansu.gov.cn/swt/c108415/202203/1994210.shtml'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62'
}

r = requests.get(baseurl, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

find_setion = soup.find('div', id='zoom')
# find_table = find_setion.find('table')
print(find_setion)
