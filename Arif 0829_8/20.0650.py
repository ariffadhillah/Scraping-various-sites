import requests
from bs4 import BeautifulSoup
import csv

url = 'https://alp.org.au/about/organisation'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62'
}

data = []

fields = ['Names', 'Roles' , 'Titles' , 'PII' , 'Email' ,  'Facebook URL' , 'Instagram URL' , 'Twitter URL' ]
filename = '20.0650.csv'


r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

list_item_url = []

find_tag_a = soup.find_all('a', class_='ml-card__link', href=True)[:4]

# list_item_url = []

for link_elem in find_tag_a:
    urlBioDetail = 'https://alp.org.au' + link_elem['href']
    name = link_elem.find('div', class_='ml-card__title').text.strip()
    roles = link_elem.find('div', class_='ml-card__description').text.strip()
    list_item_url.append({'urlBioDetail': urlBioDetail, 'name': name, 'roles': roles})

for item_url in list_item_url:
    infoBio = item_url['urlBioDetail']
    name = item_url['name']
    roles = item_url['roles']
    
    r = requests.get(infoBio, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    # print(infoBio)
    # print(name)
    # print(roles)
    # print( )

    find_contact = soup.find('div', class_='page-grid-item__col-1-description')

    title = soup.find('h3', class_='ml-card__title-2').text.strip()

    desc = soup.find('div', class_='rich-text-wrapper')
    text_p_elements = desc.find_all('p')

    text_PII = "\n\n".join([p.get_text() for p in text_p_elements if not p.find('a')])

    # print(text_PII)

    
    facebook_link = find_contact.find('a', href=True, string='Facebook')
    instagram_link = find_contact.find('a', href=True, string='Instagram')
    twitter_link = find_contact.find('a', href=True, string='Twitter')
    email_link = find_contact.find('a', href=True, string='Send an email')

    if facebook_link:
        fb = facebook_link['href']
    else:
        fb = ''

    if instagram_link:
        ig = instagram_link['href']
    else:
        ig = ''

    if twitter_link:
        tw = twitter_link['href']
    else:
        tw = ''

    if email_link:
        email = email_link['href']
    else:
        email = ''

    # print("Name:", name)
    # print("Roles:", roles)
    # print("Title:", title)
    # print("Facebook URL:", fb)
    # print("Instagram URL: ", ig)
    # print(" Twitter URL:", tw)
    # print("Email URL:", email)
    # print( )

    data_save = {
        'Names' : name,
        'Roles' : roles,
        'Titles' : title,
        'PII': text_PII,
        'Email' : email,
        'Facebook URL' : fb,
        'Instagram URL' : ig,
        'Twitter URL' : tw
    }
    data.append(data_save)
    print('Saving', data_save['Names'])
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)
