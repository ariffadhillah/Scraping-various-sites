import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv

baseurl = 'https://ipsearch.saip.gov.sa/wopublish-search/public/'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67'
}

fields = ['Applicant (EN)', 'Applicant (AR)', 'Filing Date', 'Application Number', 'Designer (AR)' ,'Designer (EN)' , 'Details URL']
filename = '80.0008.csv'
data = []

def process_page(url):
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    searchTable = soup.find('table', id='dataTable')
    searchTableitems = searchTable.find_all('tr', class_='col-md-2')

    for item in searchTableitems:
        item_id = item['id']
        detail_url = urljoin(baseurl, f'detail/designs?id={item_id}')
        r_detail = requests.get(detail_url, headers=headers)
        soup_detail = BeautifulSoup(r_detail.content, 'lxml')
        productDetails = soup_detail.find('div', class_='product-details')
        
        # 
        applicationNumberFilingDate = productDetails.find('div', class_='col-md-2 product-form-label', string='(20) رقم الطلب وتاريخ الايداع')        
        filingDate = applicationNumberFilingDate.find_next_sibling('div', class_='col-md-4 product-form-details').find_all('span')[1].get_text(strip=True)
        applicationNumber = applicationNumberFilingDate.find_next_sibling('div', class_='col-md-4 product-form-details').find_all('span')[0].get_text(strip=True)
        # END

        rowApplicant = productDetails.find('div', id='apnaDiv')
        appliCant = rowApplicant.find_all('div', class_='row')

        theDesigners = productDetails.find_all('div', id='owDiv')
        designerAR_list = []
        designerEN_list = []

        for designer in theDesigners:
            designerAR = designer.find_all('div', class_='row')[0].text.strip()
            designerAR_list.append(designerAR)

            designerEN = designer.find_all('div', class_='row')[1].text.strip()
            designerEN_list.append(designerEN)

            designerAR_str = '   ,   '.join([designer.replace('(AR)', '  ').strip() for designer in designerAR_list])
            designerEN_str = '   ,   '.join([designer.replace('(EN)', '  ').strip() for designer in designerEN_list])

            data_80_0008 = {
                'Details URL': detail_url,
                'Filing Date': filingDate,
                'Application Number': applicationNumber, 
                'Applicant (AR)': appliCant[0].text.replace('(AR)', '').replace('\n', ''),
                'Applicant (EN)': appliCant[1].text.replace('(EN)', '').replace('\n', ''),
                'Designer (AR)': designerAR_str,
                'Designer (EN)': designerEN_str
            }

        data.append(data_80_0008)
        print('Saving', data_80_0008['Details URL'], data_80_0008['Designer (AR)'], data_80_0008['Designer (EN)'] )
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            writer.writerows(data)

    # Cari tautan ke halaman berikutnya
    current_page = 1
    next_link = soup.find('a', title='Go to page {}'.format(current_page + 1))
    while next_link:
        current_page += 1
        next_url = urljoin(baseurl, next_link['href'])
        r_next = requests.get(next_url, headers=headers)
        print(next_url)
        soup_next = BeautifulSoup(r_next.content, 'lxml')
        searchTable_next = soup_next.find('table', id='dataTable')
        searchTableitems_next = searchTable_next.find_all('tr', class_='col-md-2')

        for item_next in searchTableitems_next:
            item_id_next = item_next['id']
            detail_url_next = urljoin(baseurl, f'detail/designs?id={item_id_next}')
            r_detail_next = requests.get(detail_url_next, headers=headers)
            soup_detail_next = BeautifulSoup(r_detail_next.content, 'lxml')

            productDetails_next = soup_detail_next.find('div', class_='product-details')

            # 
            applicationNumberFilingDate_next = productDetails_next.find('div', class_='col-md-2 product-form-label', string='(20) رقم الطلب وتاريخ الايداع')
            filingDate_next = applicationNumberFilingDate_next.find_next_sibling('div', class_='col-md-4 product-form-details').find_all('span')[1].get_text(strip=True)
            applicationNumber_next = applicationNumberFilingDate_next.find_next_sibling('div', class_='col-md-4 product-form-details').find_all('span')[0].get_text(strip=True)
            # END

            rowApplicantNext = productDetails_next.find('div', id='apnaDiv')
            appliCant_next = rowApplicantNext.find_all('div', class_='row')

            theDesigners_next = productDetails_next.find_all('div', id='owDiv')
            designerAR_list_next = []
            designerEN_list_next = []

            for designer_next in theDesigners_next:
                designerAR_neext = designer_next.find_all('div', class_='row')[0].text.strip()
                designerAR_list_next.append(designerAR_neext)

                designerEN_next = designer.find_all('div', class_='row')[1].text.strip()
                designerEN_list_next.append(designerEN_next)

            # print(designerAR_list)
            # print(designerEN_list)

            # theDesigners_next = productDetails.find_all('div', id='owDiv')
            # designer_text_next = ', '.join([designer_next.text.replace('(AR)', '').replace('(EN)', '').replace('\n', '') for designer_next in theDesigners_next])
            
            designerAR_str_next = '   ,   '.join([designer_next.replace('(AR)', '  ').strip() for designer_next in designerAR_list_next])
            designerEN_str_next = '   ,   '.join([designer_next.replace('(EN)', '  ').strip() for designer_next in designerEN_list_next])

            data_80_0008_next = {
                'Details URL': detail_url_next,
                'Filing Date': filingDate_next,
                'Application Number': applicationNumber_next,
                'Applicant (AR)': appliCant_next[0].text.replace('(AR)','').replace('\n',''),
                'Applicant (EN)': appliCant_next[1].text.replace('(EN)','').replace('\n',''),
                'Designer (AR)': designerAR_str_next,
                'Designer (EN)': designerEN_str_next
            }

            data.append(data_80_0008_next)
            print('Saving', data_80_0008_next['Details URL'], data_80_0008_next['Designer (EN)'], data_80_0008_next['Designer (AR)'] )
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fields)
                writer.writeheader()
                writer.writerows(data)

        next_link = soup_next.find('a', title='Go to page {}'.format(current_page + 1))

# Mulai dengan halaman pertama
start_url = urljoin(baseurl, 'designs?17&query=*:*')
process_page(start_url)
