import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.gov.ky/chiefofficers'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188'
}

data = []

fields = ['']
filename = '20.1155.csv'

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

find_section = soup.find('div', class_='scs-slot scs-responsive col-lg-9 col-md-8 col-sm-12')
print(find_section)