import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv
import unicodedata

baseurl = 'https://ipsearch.saip.gov.sa/wopublish-search/public/'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67'
}

fields = ['Mark (EN)', 'Mark (AR)',  'Filing Date', 'Application Number', 'Details URL']
filename = '80.0007.csv'
data = []

def process_page(url):
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    searchTable = soup.find('table', id='dataTable')
    searchTableitems = searchTable.find_all('tr', class_='col-md-2')
    # print(searchTableitems)

    for item in searchTableitems:
        item_id = item['id']
        detail_url = urljoin(baseurl, f'detail/trademarks?id={item_id}')
        # print(detail_url)

        r_detail = requests.get(detail_url, headers=headers)
        soup_detail = BeautifulSoup(r_detail.content, 'lxml')
        productDetails = soup_detail.find('div', class_='detail-container col-md-12')  
    #     # 
        applicationNumberFilingDate = productDetails.find('div', class_='col-md-2 product-form-label', string='(200) رقم الطلب وتاريخ الايداع')        
        filingDate = applicationNumberFilingDate.find_next_sibling('div', class_='col-md-4 product-form-details').find_all('span')[1].get_text(strip=True)
        applicationNumber = applicationNumberFilingDate.find_next_sibling('div', class_='col-md-4 product-form-details').find_all('span')[0].get_text(strip=True)

        mark_name = productDetails.find('div', class_='col-md-2 product-form-label', string='(541)العلامة التجارية')
        mark_nameap = mark_name.find_next_sibling('div', class_='col-md-4 product-form-details')
        
        nameMark =  mark_nameap.find_all('b')[0]
        try:
            nametextAR = unicodedata.normalize("NFKD", nameMark.next_sibling.strip())
        except:
            nametextAR = ''
        
        nameMarkEN =  mark_nameap.find_all('b')[1]
        try:
            nametextEN = unicodedata.normalize("NFKD", nameMarkEN.next_sibling.strip())
        except:
            nametextEN = ''


        data_80_0008 = {
            'Details URL': detail_url,
            'Filing Date': filingDate,
            'Application Number': applicationNumber, 
            'Mark (AR)': nametextAR.replace('-',''),
            'Mark (EN)': nametextEN.replace('-',''),

        }

        data.append(data_80_0008)
        print('Saving', data_80_0008['Details URL'])
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            writer.writerows(data)

    # 
    current_page = 1
    next_link = soup.find('a', title='Go to page {}'.format(current_page + 1))
    while next_link:
        current_page += 1
        next_url = urljoin(baseurl, next_link['href'])
        r_next = requests.get(next_url, headers=headers)
        soup_next = BeautifulSoup(r_next.content, 'lxml')
        searchTable_next = soup_next.find('table', id='dataTable')
        # print(searchTable_next)
        searchTableitems_next = searchTable_next.find_all('tr', class_='col-md-2')

        for item_next in searchTableitems_next:
            item_id_next = item_next['id']
            detail_url_next = urljoin(baseurl, f'detail/trademarks?id={item_id_next}')
            
            r_detail_next = requests.get(detail_url_next, headers=headers)
            soup_detail_next = BeautifulSoup(r_detail_next.content, 'lxml')

            productDetails_next = soup_detail_next.find('div', class_='product-details')

            # 
            applicationNumberFilingDate_next = productDetails_next.find('div', class_='col-md-2 product-form-label', string='(200) رقم الطلب وتاريخ الايداع')
            filingDate_next = applicationNumberFilingDate_next.find_next_sibling('div', class_='col-md-4 product-form-details').find_all('span')[1].get_text(strip=True)
            applicationNumber_next = applicationNumberFilingDate_next.find_next_sibling('div', class_='col-md-4 product-form-details').find_all('span')[0].get_text(strip=True)

            print(detail_url_next)
            detailmark = soup_detail_next.find('div', class_='detail-container col-md-12')
            mark_name_next = detailmark.find('div', class_='col-md-2 product-form-label', string='(541)العلامة التجارية')
            mark_nameap_next = mark_name_next.find_next_sibling('div', class_='col-md-4 product-form-details')
            markAR_next = mark_nameap_next.find_all('b')[0]

            try:
                nametextAR_next = unicodedata.normalize("NFKD", markAR_next.next_sibling.strip())
            except:
                nametextAR_next = ''
            

            markEN_next = mark_nameap_next.find_all('b')[1]
            try:
                nametextEN_next = unicodedata.normalize("NFKD", markEN_next.next_sibling.strip())
            except:
                nametextEN_next = ''

            data_80_0008_next = {
                'Details URL': detail_url_next,
                'Filing Date': filingDate_next,
                'Application Number': applicationNumber_next,
                'Mark (AR)': nametextAR_next.replace('-',''),
                'Mark (EN)': nametextEN_next.replace('-',''),
            }

            data.append(data_80_0008_next)
            print('Saving', data_80_0008_next['Details URL'])
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fields)
                writer.writeheader()
                writer.writerows(data)

        next_link = soup_next.find('a', title='Go to page {}'.format(current_page + 1))

# Start with the first page
start_url = urljoin(baseurl, 'trademarks?3&lang=en&query=*:*')
process_page(start_url)
