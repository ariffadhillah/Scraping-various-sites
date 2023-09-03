import requests

url = "https://www.cnv.gov.ar/SitioWeb/RegistrosPublicos/DataTableIdoneos"

payload = "draw=1&columns%5B0%5D%5Bdata%5D=dni&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=cuit&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=true&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=nombreApellido&columns%5B2%5D%5Bname%5D=&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=estado&columns%5B3%5D%5Bname%5D=&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=true&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=&columns%5B4%5D%5Bname%5D=&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=true&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=0&order%5B0%5D%5Bdir%5D=asc&start=0&length=10&search%5Bvalue%5D=&search%5Bregex%5D=false"
headers = {
		'Accept': 'application/json, text/javascript, */*; q=0.01',
		'Accept-Language': 'en-US,en;q=0.9',
		'Cache-Control': 'no-cache',
		'Connection': 'keep-alive',
		'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
		'Cookie': '_ga=GA1.3.2123605253.1693703946; _gid=GA1.3.387052383.1693703946; ARRAffinity=844e0554d448b0317c9ed9a9b79272332e8752f83276ee79c5cc6b58c1b4602f; _gat=1; ASP.NET_SessionId=x3sj5qj2f3lswo0uszxrj0jw',
		'DNT': '1',
		'Origin': 'https://www.cnv.gov.ar',
		'Pragma': 'no-cache',
		'Referer': 'https://www.cnv.gov.ar/SitioWeb/RegistrosPublicos/ResultadosIdoneos',
		'Sec-Fetch-Dest': 'empty',
		'Sec-Fetch-Mode': 'cors',
		'Sec-Fetch-Site': 'same-origin',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69',
		'X-Requested-With': 'XMLHttpRequest',
		'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Microsoft Edge";v="116"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)





curl "https://www.cnv.gov.ar/SitioWeb/RegistrosPublicos/DataTableIdoneos" ^
  -H "Accept: application/json, text/javascript, */*; q=0.01" ^
  -H "Accept-Language: en-US,en;q=0.9" ^
  -H "Cache-Control: no-cache" ^
  -H "Connection: keep-alive" ^
  -H "Content-Type: application/x-www-form-urlencoded; charset=UTF-8" ^
  -H "Cookie: _ga=GA1.3.2123605253.1693703946; _gid=GA1.3.387052383.1693703946; ARRAffinity=844e0554d448b0317c9ed9a9b79272332e8752f83276ee79c5cc6b58c1b4602f; _gat=1; ASP.NET_SessionId=x3sj5qj2f3lswo0uszxrj0jw" ^
  -H "DNT: 1" ^
  -H "Origin: https://www.cnv.gov.ar" ^
  -H "Pragma: no-cache" ^
  -H "Referer: https://www.cnv.gov.ar/SitioWeb/RegistrosPublicos/ResultadosIdoneos" ^
  -H "Sec-Fetch-Dest: empty" ^
  -H "Sec-Fetch-Mode: cors" ^
  -H "Sec-Fetch-Site: same-origin" ^
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69" ^
  -H "X-Requested-With: XMLHttpRequest" ^
  -H "sec-ch-ua: ^\^"Chromium^\^";v=^\^"116^\^", ^\^"Not)A;Brand^\^";v=^\^"24^\^", ^\^"Microsoft Edge^\^";v=^\^"116^\^"" ^
  -H "sec-ch-ua-mobile: ?0" ^
  -H "sec-ch-ua-platform: ^\^"Windows^\^"" ^
  --data-raw "draw=1&columns^%^5B0^%^5D^%^5Bdata^%^5D=dni&columns^%^5B0^%^5D^%^5Bname^%^5D=&columns^%^5B0^%^5D^%^5Bsearchable^%^5D=true&columns^%^5B0^%^5D^%^5Borderable^%^5D=true&columns^%^5B0^%^5D^%^5Bsearch^%^5D^%^5Bvalue^%^5D=&columns^%^5B0^%^5D^%^5Bsearch^%^5D^%^5Bregex^%^5D=false&columns^%^5B1^%^5D^%^5Bdata^%^5D=cuit&columns^%^5B1^%^5D^%^5Bname^%^5D=&columns^%^5B1^%^5D^%^5Bsearchable^%^5D=true&columns^%^5B1^%^5D^%^5Borderable^%^5D=true&columns^%^5B1^%^5D^%^5Bsearch^%^5D^%^5Bvalue^%^5D=&columns^%^5B1^%^5D^%^5Bsearch^%^5D^%^5Bregex^%^5D=false&columns^%^5B2^%^5D^%^5Bdata^%^5D=nombreApellido&columns^%^5B2^%^5D^%^5Bname^%^5D=&columns^%^5B2^%^5D^%^5Bsearchable^%^5D=true&columns^%^5B2^%^5D^%^5Borderable^%^5D=true&columns^%^5B2^%^5D^%^5Bsearch^%^5D^%^5Bvalue^%^5D=&columns^%^5B2^%^5D^%^5Bsearch^%^5D^%^5Bregex^%^5D=false&columns^%^5B3^%^5D^%^5Bdata^%^5D=estado&columns^%^5B3^%^5D^%^5Bname^%^5D=&columns^%^5B3^%^5D^%^5Bsearchable^%^5D=true&columns^%^5B3^%^5D^%^5Borderable^%^5D=true&columns^%^5B3^%^5D^%^5Bsearch^%^5D^%^5Bvalue^%^5D=&columns^%^5B3^%^5D^%^5Bsearch^%^5D^%^5Bregex^%^5D=false&columns^%^5B4^%^5D^%^5Bdata^%^5D=&columns^%^5B4^%^5D^%^5Bname^%^5D=&columns^%^5B4^%^5D^%^5Bsearchable^%^5D=true&columns^%^5B4^%^5D^%^5Borderable^%^5D=true&columns^%^5B4^%^5D^%^5Bsearch^%^5D^%^5Bvalue^%^5D=&columns^%^5B4^%^5D^%^5Bsearch^%^5D^%^5Bregex^%^5D=false&order^%^5B0^%^5D^%^5Bcolumn^%^5D=0&order^%^5B0^%^5D^%^5Bdir^%^5D=asc&start=0&length=10&search^%^5Bvalue^%^5D=&search^%^5Bregex^%^5D=false" ^
  --compressed