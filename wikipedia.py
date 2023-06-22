
# # # import pandas as pd
# # # from bs4 import BeautifulSoup

# # # html = '''
# # # <table>
# # #     <tr>
# # #         <td>Kozosushi Co.,LTD. </td>
# # #         <td>9973</td>
# # #         <td rowspan="1">Apr. 21, 2023</td>
# # #         <td rowspan="1">17:00</td>
# # #         <td rowspan="1">17:15</td>
# # #         <td rowspan="1">17:16</td>
# # #         <td rowspan="1">An announcement was made related to merger</td>
# # #     </tr>
# # #     <tr>
# # #         <td>BROCCOLI Co.,Ltd. </td>
# # #         <td>2706</td>
# # #         <td rowspan="1">Apr. 14, 2023</td>
# # #         <td rowspan="1">16:00</td>
# # #         <td rowspan="1">16:25</td>
# # #         <td rowspan="1">16:26</td>
# # #         <td rowspan="1">An announcement was made related to tender offer, Designated to a issue under supervision</td>
# # #     </tr>
# # #     <tr>
# # #         <td>ARCLAND SERVICE HOLDINGS CO.,LTD. </td>
# # #         <td>3085</td>
# # #         <td rowspan="2">Apr. 14, 2023</td>
# # #         <td rowspan="2">15:00</td>
# # #         <td rowspan="2">15:15</td>
# # #         <td rowspan="2">15:16</td>
# # #         <td rowspan="2">An announcement was made related to merger</td>
# # #     </tr>
# # #     <tr>
# # #         <td>JPX-Nikkei 400 Bear -1x Inverse ETF </td>
# # #         <td>1468</td>
# # #     </tr>
# # #     <tr>
# # #         <td>inveteris ETF </td>
# # #         <td>2450</td>
# # #     </tr>
# # #     <tr>
# # #         <td>HOLDINGS MUI CO.,LTD. </td>
# # #         <td>1026</td>
# # #         <td rowspan="2">Juni. 14, 2020</td>
# # #         <td rowspan="2">16:00</td>
# # #         <td rowspan="2">13:15</td>
# # #         <td rowspan="2">14:16</td>
# # #         <td rowspan="2">An announcement was</td>
# # #     </tr>
# # #     <tr>
# # #         <td>Food inveteris</td>
# # #         <td>5620</td>
# # #     </tr>
    
# # # </table>
# # # '''

# # # soup = BeautifulSoup(html, 'html.parser')
# # # table = soup.find('table')

# # # # Membaca tabel HTML dengan pandas
# # # df = pd.read_html(str(table))[0]

# # # # Mengganti nama kolom
# # # df.columns = ['IssueName', 'Code', 'Date', 'SuspensionTime_Start', 'SuspensionTime_End', 'TradingRestartTime', 'Reason']

# # # # Menggabungkan baris yang memiliki rowspan
# # # df['IssueName'] = df['IssueName'].fillna(method='ffill')

# # # # Menghapus baris yang memiliki nilai null pada kolom 'Code'
# # # df = df.dropna(subset=['Code'])

# # # # Mengubah format data pada kolom 'Date'
# # # df['Date'] = df['Date'].fillna('')
# # # df['Date'] = df['Date'].mask(df['Date'] == '', df['Date'].shift())

# # # # Menampilkan data
# # # for _, row in df.iterrows():
# # #     print('IssueName:', row['IssueName'])
# # #     print('Code:', row['Code'])
# # #     print('Date:', row['Date'])
# # #     print('SuspensionTime_Start:', row['SuspensionTime_Start'])
# # #     print('SuspensionTime_End:', row['SuspensionTime_End'])
# # #     print('TradingRestartTime:', row['TradingRestartTime'])
# # #     print('Reason:', row['Reason'])
# # #     print()




# # # step 2

# # # import pandas as pd
# # # from bs4 import BeautifulSoup

# # # html = '''
# # # <table>
# # #     <tr>
# # #         <td>Kozosushi Co.,LTD. </td>
# # #         <td>9973</td>
# # #         <td rowspan="1">Apr. 21, 2023</td>
# # #         <td rowspan="1">17:00</td>
# # #         <td rowspan="1">17:15</td>
# # #         <td rowspan="1">17:16</td>
# # #         <td rowspan="1">An announcement was made related to merger</td>
# # #     </tr>
# # #     <tr>
# # #         <td>BROCCOLI Co.,Ltd. </td>
# # #         <td>2706</td>
# # #         <td rowspan="1">Apr. 14, 2023</td>
# # #         <td rowspan="1">16:00</td>
# # #         <td rowspan="1">16:25</td>
# # #         <td rowspan="1">16:26</td>
# # #         <td rowspan="1">An announcement was made related to tender offer, Designated to a issue under supervision</td>
# # #     </tr>
# # #     <tr>
# # #         <td>ARCLAND SERVICE HOLDINGS CO.,LTD. </td>
# # #         <td>3085</td>
# # #         <td rowspan="2">Apr. 14, 2023</td>
# # #         <td rowspan="2">15:00</td>
# # #         <td rowspan="2">15:15</td>
# # #         <td rowspan="2">15:16</td>
# # #         <td rowspan="2">An announcement was made related to merger</td>
# # #     </tr>
# # #     <tr>
# # #         <td>JPX-Nikkei 400 Bear -1x Inverse ETF </td>
# # #         <td>1468</td>
# # #     </tr>
# # #     <tr>
# # #         <td>Kenedix Residential Next Investment Corporation</td>
# # #         <td>8068</td>
# # #     </tr>
# # #     <tr>
# # #         <td>RYOYO ELECTRO CORPORATION</td>
# # #         <td>6032</td>
# # #     </tr>
# # #     <tr>
# # #         <td>Kenedix Residential Next Investment Corporation</td>
# # #         <td>3222</td>
# # #     </tr>
# # # </table>
# # # '''

# # # soup = BeautifulSoup(html, 'html.parser')
# # # table = soup.find('table')

# # # # Membaca tabel HTML dengan pandas
# # # df = pd.read_html(str(table))[0]

# # # # Mengganti nama kolom
# # # df.columns = ['IssueName', 'Code', 'Date', 'SuspensionTime_Start', 'SuspensionTime_End', 'TradingRestartTime', 'Reason']

# # # # Mengisi nilai-nilai rowspan
# # # rowspan_cols = ['Date', 'SuspensionTime_Start', 'SuspensionTime_End', 'TradingRestartTime', 'Reason']
# # # prev_values = ['', '', '', '', '']
# # # rowspan_index = 0
# # # for i, row in df.iterrows():
# # #     for j, col in enumerate(rowspan_cols):
# # #         if row[col] != '':
# # #             prev_values[j] = row[col]
# # #         else:
# # #             df.at[i, col] = prev_values[j]

# # # # Menghapus baris yang tidak memiliki nilai pada kolom 'Code'
# # # df = df.dropna(subset=['Code'])

# # # # Menampilkan data
# # # for index, row in df.iterrows():
# # #     print('IssueName:', row['IssueName'])
# # #     print('Code:', row['Code'])
# # #     print('Date:', row['Date'])
# # #     print('SuspensionTime_Start:', row['SuspensionTime_Start'])
# # #     print('SuspensionTime_End:', row['SuspensionTime_End'])
# # #     print('TradingRestartTime:', row['TradingRestartTime'])
# # #     print('Reason:', row['Reason'])
# # #     print()


# # # # data table  benar

# # # import pandas as pd
# # # from bs4 import BeautifulSoup

# # # html = '''
# # # <table>
# # #     <tr>
# # #         <td>Kozosushi Co.,LTD. </td>
# # #         <td>9973</td>
# # #         <td rowspan="1">Apr. 21, 2023</td>
# # #         <td rowspan="1">17:00</td>
# # #         <td rowspan="1">17:15</td>
# # #         <td rowspan="1">17:16</td>
# # #         <td rowspan="1">An announcement was made related to merger</td>
# # #     </tr>
# # #     <tr>
# # #         <td>BROCCOLI Co.,Ltd. </td>
# # #         <td>2706</td>
# # #         <td rowspan="1">Apr. 14, 2023</td>
# # #         <td rowspan="1">16:00</td>
# # #         <td rowspan="1">16:25</td>
# # #         <td rowspan="1">16:26</td>
# # #         <td rowspan="1">An announcement was made related to tender offer, Designated to a issue under supervision</td>
# # #     </tr>
# # #     <tr>
# # #         <td>ARCLAND SERVICE HOLDINGS CO.,LTD. </td>
# # #         <td>3085</td>
# # #         <td rowspan="2">Apr. 14, 2023</td>
# # #         <td rowspan="2">15:00</td>
# # #         <td rowspan="2">15:15</td>
# # #         <td rowspan="2">15:16</td>
# # #         <td rowspan="2">An announcement was made related to merger</td>
# # #     </tr>
# # #     <tr>
# # #         <td>JPX-Nikkei 400 Bear -1x Inverse ETF </td>
# # #         <td>1468</td>
# # #     </tr>
# # #     <tr>
# # #         <td>inveteris ETF </td>
# # #         <td>2450</td>
# # #     </tr>
# # #     <tr>
# # #         <td>HOLDINGS MUI CO.,LTD. </td>
# # #         <td>1026</td>
# # #         <td rowspan="2">Juni. 14, 2020</td>
# # #         <td rowspan="2">16:00</td>
# # #         <td rowspan="2">13:15</td>
# # #         <td rowspan="2">14:16</td>
# # #         <td rowspan="2">An announcement was</td>
# # #     </tr>
# # #     <tr>
# # #         <td>Food inveteris</td>
# # #         <td>5620</td>
# # #     </tr>
# # #     <tr>
# # #         <td>coba</td>
# # #         <td>3479</td>
# # #     </tr>
# # #     <tr>
# # #         <td>coba Food inveteris</td>
# # #         <td>12345</td>
# # #     </tr>
# # #     <tr>
# # #         <td>test</td>
# # #         <td>1345</td>
# # #     </tr>
    
# # # </table>
# # # '''

# # # soup = BeautifulSoup(html, 'html.parser')
# # # table = soup.find('table')

# # # # Membaca tabel HTML dengan pandas
# # # df = pd.read_html(str(table))[0]

# # # # Mengganti nama kolom
# # # df.columns = ['IssueName', 'Code', 'Date', 'SuspensionTime_Start', 'SuspensionTime_End', 'TradingRestartTime', 'Reason']

# # # # Menggabungkan baris yang memiliki rowspan
# # # df['IssueName'] = df['IssueName'].fillna(method='ffill')

# # # # Menghapus baris yang memiliki nilai null pada kolom 'Code'
# # # df = df.dropna(subset=['Code'])

# # # # Mengisi data kosong pada kolom 'Date'
# # # df['Date'] = df['Date'].fillna(method='ffill')

# # # # Mengisi data kosong pada kolom 'SuspensionTime_Start', 'SuspensionTime_End', 'TradingRestartTime', dan 'Reason'
# # # df['SuspensionTime_Start'] = df['SuspensionTime_Start'].fillna(method='ffill')
# # # df['SuspensionTime_End'] = df['SuspensionTime_End'].fillna(method='ffill')
# # # df['TradingRestartTime'] = df['TradingRestartTime'].fillna(method='ffill')
# # # df['Reason'] = df['Reason'].fillna(method='ffill')

# # # # Menampilkan data
# # # for _, row in df.iterrows():
# # #     print('IssueName:', row['IssueName'])
# # #     print('Code:', row['Code'])
# # #     print('Date:', row['Date'])
# # #     print('SuspensionTime_Start:', row['SuspensionTime_Start'])
# # #     print('SuspensionTime_End:', row['SuspensionTime_End'])
# # #     print('TradingRestartTime:', row['TradingRestartTime'])
# # #     print('Reason:', row['Reason'])
# # #     print()




# # # data table  benar
# # import pandas as pd
# # import requests
# # from bs4 import BeautifulSoup
# # import json
# # import re

# # baseurl = 'https://www.jpx.co.jp/english/markets/equities/suspended/index.html'
# # headers = {
# #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43'
# # }

# # r = requests.get(baseurl, headers=headers)
# # soup = BeautifulSoup(r.content, 'lxml')

# # table = soup.find('table', class_='widetable')



# # # # Membaca tabel HTML dengan pandas
# # df = pd.read_html(str(table))[0]

# # # Mengganti nama kolom
# # df.columns = ['IssueName', 'Code', 'Date', 'SuspensionTime_Start', 'SuspensionTime_End', 'TradingRestartTime', 'Reason']

# # # Menggabungkan baris yang memiliki rowspan
# # df['IssueName'] = df['IssueName'].fillna(method='ffill')

# # # Menghapus baris yang memiliki nilai null pada kolom 'Code'
# # df = df.dropna(subset=['Code'])

# # # Mengisi data kosong pada kolom 'Date'
# # df['Date'] = df['Date'].fillna(method='ffill')

# # # Mengisi data kosong pada kolom 'SuspensionTime_Start', 'SuspensionTime_End', 'TradingRestartTime', dan 'Reason'
# # df['SuspensionTime_Start'] = df['SuspensionTime_Start'].fillna(method='ffill')
# # df['SuspensionTime_End'] = df['SuspensionTime_End'].fillna(method='ffill')
# # df['TradingRestartTime'] = df['TradingRestartTime'].fillna(method='ffill')
# # df['Reason'] = df['Reason'].fillna(method='ffill')

# # # Menampilkan data
# # for _, row in df.iterrows():
# #     print('IssueName:', row['IssueName'])
# #     print('Code:', row['Code'])
# #     print('Date:', row['Date'])
# #     print('SuspensionTime_Start:', row['SuspensionTime_Start'])
# #     print('SuspensionTime_End:', row['SuspensionTime_End'])
# #     print('TradingRestartTime:', row['TradingRestartTime'])
# #     print('Reason:', row['Reason'])
# #     print()




# import pandas as pd
# import requests
# from bs4 import BeautifulSoup
# import json
# import re
# # Parsing HTML menggunakan BeautifulSoup
# # link = 'https://www.sc.com.my/regulation/enforcement/actions/administrative-actions/administrative-actions-in-2016'
# link = 'https://www.sc.com.my/regulation/enforcement/actions/administrative-actions/administrative-actions-in-2002'
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43'
# }
# r = requests.get(link, headers=headers)
# soup = BeautifulSoup(r.content, 'lxml')
# table = soup.find('table', class_='tab_format')

# # Membaca tabel HTML dengan pandas
# df = pd.read_html(str(table))[0]

# # Menghapus baris yang memiliki semua kolom kosong
# df = df.dropna(how='all')

# # Menyesuaikan jumlah kolom yang diharapkan
# expected_columns = ['IssueName', 'Code', 'Company', 'Description', 'Action taken', kolom6]

# try:
#     kolom6 = ['Status']
# except:
#     kolom6 = ''

# # Menyesuaikan jumlah kolom
# if len(df.columns) > len(expected_columns):
#     expected_columns += [''] * (len(df.columns) - len(expected_columns))
# elif len(df.columns) < len(expected_columns):
#     df.columns = expected_columns[:len(df.columns)]

# # Mengganti nama kolom
# df.columns = expected_columns

# try:

#     # Menampilkan data
#     for _, row in df.iterrows():
#         if any(row[expected_columns]):
#             print('IssueName:', row['IssueName'])
#             print('Code:', row['Code'])
#             print('Company:', row['Company'])
#             print('Description:', row['Description'])
#             print('Action taken:', row['Action taken'])
#             if row['Status']:
#                 print('Status:', row['Status'])
#             else:
#                 print('Status: (kosong)')
#             print()
# except:
#     None


# import pandas as pd
# import requests
# from bs4 import BeautifulSoup

# # Parsing HTML menggunakan BeautifulSoup
# link = 'https://www.sc.com.my/permalink.aspx?id=DC56FFE2-73F0-4813-A460-9BD4506F2959'
# # link = 'https://www.sc.com.my/regulation/enforcement/actions/administrative-actions/administrative-actions-in-2002'
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43'
# }
# r = requests.get(link, headers=headers)
# soup = BeautifulSoup(r.content, 'lxml')
# table = soup.find('table', class_='tab_format')

# # Membaca tabel HTML dengan pandas
# df = pd.read_html(str(table))[0]

# # Menghapus baris yang memiliki semua kolom kosong
# df = df.dropna(how='all')

# # Menyesuaikan jumlah kolom yang diharapkan
# expected_columns = ['No', 'Nature of Misconduct', 'Parties Involved', 'Brief description of misconduct', 'Action Taken', 'Date of Action']

# # Menambahkan kolom kosong jika jumlah kolom aktual kurang dari yang diharapkan
# if len(df.columns) < len(expected_columns):
#     diff = len(expected_columns) - len(df.columns)
#     df = pd.concat([df, pd.DataFrame(columns=expected_columns[-diff:])], axis=1)

# # Mengganti nama kolom
# df.columns = expected_columns

# # Menampilkan data
# for _, row in df.iterrows():
#     if any(row[expected_columns]):
#         no = row['No']
#         natureofMisconduct = row['Nature of Misconduct']
#         partiesInvolved = row['Parties Involved']
#         briefdescriptionofmisconduct = row['Brief description of misconduct']
#         actionTaken = row['Action Taken']
#         if pd.notna(row['Date of Action']):
#             dateofAction = row['Date of Action']
#         else:
#             print('Date of Action: (kosong)')
#         print()

#         print(no, natureofMisconduct, partiesInvolved, briefdescriptionofmisconduct, actionTaken, dateofAction)



import pandas as pd
import requests
from bs4 import BeautifulSoup

# Parsing HTML menggunakan BeautifulSoup
# link = 'https://www.sc.com.my/permalink.aspx?id=DC56FFE2-73F0-4813-A460-9BD4506F2959'
# link = 'https://www.sc.com.my/regulation/enforcement/actions/administrative-actions/administrative-actions-in-2002'
link = 'https://www.sc.com.my/regulation/enforcement/actions/administrative-actions/administrative-actions-in-2022'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43'
}
r = requests.get(link, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')
table = soup.find('table', class_='tab_format')

# Membaca tabel HTML dengan pandas
df = pd.read_html(str(table))[0]

# Menghapus baris yang memiliki semua kolom kosong
df = df.dropna(how='all')

# Menyesuaikan jumlah kolom yang diharapkan
expected_columns = ['No', 'Nature of Misconduct', 'Parties Involved', 'Brief description of misconduct', 'Action Taken', 'Date of Action']

# Menambahkan kolom kosong jika jumlah kolom aktual kurang dari yang diharapkan
if len(df.columns) < len(expected_columns):
    diff = len(expected_columns) - len(df.columns)
    df = pd.concat([df, pd.DataFrame(columns=expected_columns[-diff:])], axis=1)

# Mengganti nama kolom
df.columns = expected_columns

# Menampilkan data
for _, row in df.iterrows():
    if any(row[expected_columns]):
        no = row['No']
        natureofMisconduct = row['Nature of Misconduct']
        partiesInvolved = row['Parties Involved']
        briefdescriptionofmisconduct = row['Brief description of misconduct']
        actionTaken = row['Action Taken']
        dateofAction = row['Date of Action'] if pd.notna(row['Date of Action']) else '(kosong)'

        print()
        print(no, natureofMisconduct, partiesInvolved, briefdescriptionofmisconduct, actionTaken, dateofAction)

    # print(no, natureofMisconduct,  briefdescriptionofmisconduct, actionTaken, dateofAction)
