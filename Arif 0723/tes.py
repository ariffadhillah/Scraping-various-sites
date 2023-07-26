# import http.client

# conn = http.client.HTTPSConnection("gbpa.com")
# payload = ''
# headers = {}
# conn.request("GET", "/scripts/inc/licensees/ssp.php?draw=3&columns%255B0%255D%255Bdata%255D=0&columns%255B0%255D%255Bname%255D=&columns%255B0%255D%255Bsearchable%255D=true&columns%255B0%255D%255Borderable%255D=true&columns%255B0%255D%255Bsearch%255D%255Bvalue%255D=&columns%255B0%255D%255Bsearch%255D%255Bregex%255D=false&columns%255B1%255D%255Bdata%255D=1&columns%255B1%255D%255Bname%255D=&columns%255B1%255D%255Bsearchable%255D=true&columns%255B1%255D%255Borderable%255D=true&columns%255B1%255D%255Bsearch%255D%255Bvalue%255D=&columns%255B1%255D%255Bsearch%255D%255Bregex%255D=false&columns%255B2%255D%255Bdata%255D=2&columns%255B2%255D%255Bname%255D=&columns%255B2%255D%255Bsearchable%255D=true&columns%255B2%255D%255Borderable%255D=true&columns%255B2%255D%255Bsearch%255D%255Bvalue%255D=&columns%255B2%255D%255Bsearch%255D%255Bregex%255D=false&columns%255B3%255D%255Bdata%255D=3&columns%255B3%255D%255Bname%255D=&columns%255B3%255D%255Bsearchable%255D=true&columns%255B3%255D%255Borderable%255D=true&columns%255B3%255D%255Bsearch%255D%255Bvalue%255D=&columns%255B3%255D%255Bsearch%255D%255Bregex%255D=false&columns%255B4%255D%255Bdata%255D=4&columns%255B4%255D%255Bname%255D=&columns%255B4%255D%255Bsearchable%255D=true&columns%255B4%255D%255Borderable%255D=true&columns%255B4%255D%255Bsearch%255D%255Bvalue%255D=&columns%255B4%255D%255Bsearch%255D%255Bregex%255D=false&columns%255B5%255D%255Bdata%255D=5&columns%255B5%255D%255Bname%255D=&columns%255B5%255D%255Bsearchable%255D=true&columns%255B5%255D%255Borderable%255D=true&columns%255B5%255D%255Bsearch%255D%255Bvalue%255D=&columns%255B5%255D%255Bsearch%255D%255Bregex%255D=false&order%255B0%255D%255Bcolumn%255D=0&order%255B0%255D%255Bdir%255D=asc&start=6100&length=100&search%255Bvalue%255D=&search%255Bregex%255D=false&_=1690347095589%0A", payload, headers)
# res = conn.getresponse()
# data = res.read()
# print(data.decode("utf-8"))


import http.client
import json

conn = http.client.HTTPSConnection("gbpa.com")
payload = ''
headers = {}
conn.request("GET", "/scripts/inc/licensees/ssp.php?draw=3&columns%255B0%255D%255Bdata%255D=0&columns%255B0%255D%255Bname%255D=&columns%255B0%255D%255Bsearchable%255D=true&columns%255B0%255D%255Borderable%255D=true&columns%255B0%255D%255Bsearch%255D%255Bvalue%255D=&columns%255B0%255D%255Bsearch%255D%255Bregex%255D=false&columns%255B1%255D%255Bdata%255D=1&columns%255B1%255D%255Bname%255D=&columns%255B1%255D%255Bsearchable%255D=true&columns%255B1%255D%255Borderable%255D=true&columns%255B1%255D%255Bsearch%255D%255Bvalue%255D=&columns%255B1%255D%255Bsearch%255D%255Bregex%255D=false&columns%255B2%255D%255Bdata%255D=2&columns%255B2%255D%255Bname%255D=&columns%255B2%255D%255Bsearchable%255D=true&columns%255B2%255D%255Borderable%255D=true&columns%255B2%255D%255Bsearch%255D%255Bvalue%255D=&columns%255B2%255D%255Bsearch%255D%255Bregex%255D=false&columns%255B3%255D%255Bdata%255D=3&columns%255B3%255D%255Bname%255D=&columns%255B3%255D%255Bsearchable%255D=true&columns%255B3%255D%255Borderable%255D=true&columns%255B3%255D%255Bsearch%255D%255Bvalue%255D=&columns%255B3%255D%255Bsearch%255D%255Bregex%255D=false&columns%255B4%255D%255Bdata%255D=4&columns%255B4%255D%255Bname%255D=&columns%255B4%255D%255Bsearchable%255D=true&columns%255B4%255D%255Borderable%255D=true&columns%255B4%255D%255Bsearch%255D%255Bvalue%255D=&columns%255B4%255D%255Bsearch%255D%255Bregex%255D=false&columns%255B5%255D%255Bdata%255D=5&columns%255B5%255D%255Bname%255D=&columns%255B5%255D%255Bsearchable%255D=true&columns%255B5%255D%255Borderable%255D=true&columns%255B5%255D%255Bsearch%255D%255Bvalue%255D=&columns%255B5%255D%255Bsearch%255D%255Bregex%255D=false&order%255B0%255D%255Bcolumn%255D=0&order%255B0%255D%255Bdir%255D=asc&start=6100&length=100&search%255Bvalue%255D=&search%255Bregex%255D=false&_=1690347095589%0A", payload, headers)
res = conn.getresponse()
data = res.read()

# Assuming the response is in JSON format, parse it
json_data = json.loads(data.decode("utf-8"))

# Extract the desired data from the JSON response
dapa_api_data = json_data["data"]

print(dapa_api_data)
