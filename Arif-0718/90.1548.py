import csv
import requests
from bs4 import BeautifulSoup
import re

baseurl = 'https://sia.org.ws/index.php/cb-profile/userslist/4-list-of-members?'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82'
}

fields = ['Name', 'Organisation']
filename = '90.1548.csv'
data = []

# Create a set to keep track of unique entries
unique_entries = set()

for x in range(1, 5):
    limitstart = (x - 1) * 30
    url = f'limitstart={limitstart}'
    r = requests.get(baseurl + url, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    content_container = soup.find('div', id='cbUserTable')
    firstname_tags = content_container.find_all('div', class_='cbUserListFieldLine cbUserListFL_firstname')
    lastname_tags = content_container.find_all('div', class_='cbUserListFieldLine cbUserListFL_lastname')
    organisation_tags = content_container.find_all('div', class_='cbUserListFieldLine cbUserListFL_cb_organisation')

    name_list = list(zip([f.text for f in firstname_tags], [l.text for l in lastname_tags], [o.text for o in organisation_tags]))

    for firstname, lastname, organization in name_list:
        entry = f"{firstname} {lastname} {organization}"
        if entry not in unique_entries:  # Check if the entry is not a duplicate
            unique_entries.add(entry)  # Add the entry to the set
            
            data_90_1548 = {
                'Name': f"{firstname} {lastname}",
                'Organisation': organization
            }

            data.append(data_90_1548)
            print('Saving', data_90_1548['Name'])

# Save the data to CSV file
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(data)
