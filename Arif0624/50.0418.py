import requests
from bs4 import BeautifulSoup
import json
import re

baseurl = 'https://www.sfc.hk/en/Regulatory-functions/Enforcement/Upcoming-hearings-calendar'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43'
}

r = requests.get(baseurl, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

