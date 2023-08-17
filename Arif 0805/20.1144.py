# import requests
# from bs4 import BeautifulSoup
# import csv

# def find_key_recursive(data, target_key):
#     results = []
    
#     if isinstance(data, dict):
#         for key, value in data.items():
#             if key == target_key:
#                 results.append(value)
#             else:
#                 results.extend(find_key_recursive(value, target_key))
#     elif isinstance(data, list):
#         for item in data:
#             results.extend(find_key_recursive(item, target_key))
    
#     return results

# url = "https://www.gov.ky/_cache_a50b/pages/571.json"

# headers = {
#     'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.200'
# }

# response = requests.get(url, headers=headers)

# data_save = []

# fields = ['Names', 'Roles', 'Curriculum Vitae', 'Contact Us', 'Address', 'Office Hours:', 'PII']
# filename = '20.1144.csv'

# if response.status_code == 200:
#     dataAPI = response.json()

#     target_key = "userText"

#     user_text_data = find_key_recursive(dataAPI, target_key)
    
#     curriculum_vitae_values = []
    
#     for idx, user_text in enumerate(user_text_data, start=1):
#         soup = BeautifulSoup(user_text, 'html.parser')
#         info = soup

#         if idx == 4:
#             theGovernorOffice = info.text.strip()        
        
#         if idx in [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]:
#             curriculum_vitae_values.append(info.text)
            
#             # print(curriculum_vitae_values)

#         if idx == 5:
#             contact_data = [] 

#             for contact in soup.find_all('p'):
#                 info_contact = contact.get_text(separator='\n')
#                 contact_data.append(info_contact.strip())
                
#             if len(contact_data) >= 1:
#                 address = contact_data[0]
#             else:
#                 address = ""

#             if len(contact_data) >= 2:
#                 contact_us = contact_data[2]
#             else:
#                 contact_us = ""
 
#             if len(contact_data) >= 4:
#                 officeHours = contact_data[4]
#             else:
#                 officeHours = ""
            
#             # curriculum_vitae_combined = ' '.join(curriculum_vitae_values)
#             # curriculum_vitae_combined = curriculum_vitae_combined


#             data_20_1144 = {
#                 'Names': 'Mrs Jane Owen',
#                 'Roles': "The Governor's Office",
#                 'Curriculum Vitae': curriculum_vitae_values,
#                 'Contact Us': contact_us,
#                 'Address': address,
#                 'Office Hours:': officeHours,
#                 'PII': theGovernorOffice,
#             }

#             data_save.append(data_20_1144)

# # Save the data outside the loop
# print('Saving data...')
# with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=fields)
#     writer.writeheader()
#     for item in data_save:
#         writer.writerow(item)

# print('Data saved successfully.')



import requests
from bs4 import BeautifulSoup
import csv

def find_key_recursive(data, target_key):
    results = []
    
    if isinstance(data, dict):
        for key, value in data.items():
            if key == target_key:
                results.append(value)
            else:
                results.extend(find_key_recursive(value, target_key))
    elif isinstance(data, list):
        for item in data:
            results.extend(find_key_recursive(item, target_key))
    
    return results

url = "https://www.gov.ky/_cache_a50b/pages/571.json"

headers = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.200'
}

response = requests.get(url, headers=headers)

data_save = []

fields = ['Names', 'Roles', 'Curriculum Vitae', 'Contact Us', 'Address', 'Office Hours:', 'PII']
filename = '20.1144.csv'

if response.status_code == 200:
    dataAPI = response.json()

    target_key = "userText"

    user_text_data = find_key_recursive(dataAPI, target_key)
    
    
    for idx, user_text in enumerate(user_text_data, start=1):
        soup = BeautifulSoup(user_text, 'html.parser')
        info = soup

        if idx == 4:
            theGovernorOffice = info.text.strip()        
        
        # curriculum_vitae_values = ''
            # print(curriculum_vitae_values)

        if idx == 5:
            contact_data = [] 

            for contact in soup.find_all('p'):
                info_contact = contact.get_text(separator='\n')
                contact_data.append(info_contact.strip())
                
            if len(contact_data) >= 1:
                address = contact_data[0]
            else:
                address = ""

            if len(contact_data) >= 2:
                contact_us = contact_data[2]
            else:
                contact_us = ""
 
            if len(contact_data) >= 4:
                officeHours = contact_data[4]
            else:
                officeHours = ""

        if idx in [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]:
            curriculum_vitae_values = info.text.strip() 

            data_20_1144 = {
                'Names': 'Mrs Jane Owen',
                'Roles': "The Governor's Office",
                'Curriculum Vitae': curriculum_vitae_values,
                'Contact Us': contact_us,
                'Address': address,
                'Office Hours:': officeHours,
                'PII': theGovernorOffice,
            }

            data_save.append(data_20_1144)

# Save the data outside the loop
print('Saving data...')
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    for item in data_save:
        writer.writerow(item)

print('Data saved successfully.')
