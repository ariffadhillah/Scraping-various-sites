import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.parliament.nz/en/mps-and-electorates/members-of-parliament/'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62'
}

data = []

fields = ['']
filename = '20.0658.csv'

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

find_table = soup.find('table', class_='table--list')
print(find_table)
