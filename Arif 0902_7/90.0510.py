# import requests

# url = "https://www.cnv.gov.ar/SitioWeb/RegistrosPublicos/DataTableIdoneos"

# # payload = "draw=1&columns%5B0%5D%5Bdata%5D=dni&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=cuit&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=true&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=nombreApellido&columns%5B2%5D%5Bname%5D=&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=estado&columns%5B3%5D%5Bname%5D=&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=true&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=&columns%5B4%5D%5Bname%5D=&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=true&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=0&order%5B0%5D%5Bdir%5D=asc&start=0&length=10&search%5Bvalue%5D=&search%5Bregex%5D=false"

# payload = "draw=2&columns%5B0%5D%5Bdata%5D=dni&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=cuit&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=true&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=nombreApellido&columns%5B2%5D%5Bname%5D=&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=estado&columns%5B3%5D%5Bname%5D=&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=true&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=&columns%5B4%5D%5Bname%5D=&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=true&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=0&order%5B0%5D%5Bdir%5D=asc&start=10&length=10&search%5Bvalue%5D=&search%5Bregex%5D=false"

# headers = {
# 		'Accept': 'application/json, text/javascript, */*; q=0.01',
# 		'Accept-Language': 'en-US,en;q=0.9',
# 		'Cache-Control': 'no-cache',
# 		'Connection': 'keep-alive',
# 		'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
# 		'Cookie': '_ga=GA1.3.2123605253.1693703946; ARRAffinity=1b5d62bae14a53032cbb52ac259d71d9917a62838c4440b95bbbf0e839d5ad81; _gid=GA1.3.1348668666.1693958674; _gat=1; ASP.NET_SessionId=5n1fh5tfmkrh1iutpu0tkikn',
# 		'DNT': '1',
# 		'Origin': 'https://www.cnv.gov.ar',
# 		'Pragma': 'no-cache',
# 		'Referer': 'https://www.cnv.gov.ar/SitioWeb/RegistrosPublicos/ResultadosIdoneos',
# 		'Sec-Fetch-Dest': 'empty',
# 		'Sec-Fetch-Mode': 'cors',
# 		'Sec-Fetch-Site': 'same-origin',
# 		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69',
# 		'X-Requested-With': 'XMLHttpRequest',
# 		'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Microsoft Edge";v="116"',
# 		'sec-ch-ua-mobile': '?0',
# 		'sec-ch-ua-platform': '"Windows"'
# }

# response = requests.request("POST", url, headers=headers, data=payload)

# print(response.text)






import requests
import html
from bs4 import BeautifulSoup

url = "https://www.sec.gov.rs/index.php/en/?__ajaxCall=1&__method=module:aridatatables:getData&moduleId=270&sEcho=1&iColumns=6&sColumns=&iDisplayStart=0&iDisplayLength=10&mDataProp_0=0&mDataProp_1=1&mDataProp_2=2&mDataProp_3=3&mDataProp_4=4&mDataProp_5=5&sSearch=&bRegex=false&sSearch_0=&bRegex_0=false&bSearchable_0=true&sSearch_1=&bRegex_1=false&bSearchable_1=true&sSearch_2=&bRegex_2=false&bSearchable_2=true&sSearch_3=&bRegex_3=false&bSearchable_3=true&sSearch_4=&bRegex_4=false&bSearchable_4=true&sSearch_5=&bRegex_5=false&bSearchable_5=true&iSortCol_0=0&sSortDir_0=asc&iSortingCols=1&bSortable_0=true&bSortable_1=true&bSortable_2=true&bSortable_3=true&bSortable_4=true&bSortable_5=true&_=1693960936118"

payload = {}
headers = {
		'Accept': 'application/json, text/javascript, */*; q=0.01',
		'Accept-Language': 'en-US,en;q=0.9',
		'Cache-Control': 'no-cache',
		'Connection': 'keep-alive',
		'Cookie': 'fcd145c34db92d75a12b04d69a3679eb=en-GB; gktab-gk-tab-1=3; 1abb45145d24b81ff687af5bd926d29d=kmnnt24a9m88k9t4gohvfh0ljdaei2md6dl6v2e4ds6j0pqst5l1; fcd145c34db92d75a12b04d69a3679eb=en-GB',
		'DNT': '2',
		'Pragma': 'no-cache',
		'Referer': 'https://www.sec.gov.rs/index.php/en/public-registers-of-information/register-of-portfolio-managers',
		'Sec-Fetch-Dest': 'empty',
		'Sec-Fetch-Mode': 'cors',
		'Sec-Fetch-Site': 'same-origin',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69',
		'X-Requested-With': 'XMLHttpRequest',
		'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Microsoft Edge";v="116"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"'
}

response = requests.request("GET", url, headers=headers, data=payload)
if response.status_code == 200:
    decoded_response = html.unescape(response.text)  # Mendekode karakter escape HTML
    soup = BeautifulSoup(decoded_response, 'html.parser')

    divs = soup.find_all('div')
    for div in divs:
        clean_text = div.text.replace(r'\/', '')
        print(clean_text)

else:
    print("Error Status ", response.status_code)
