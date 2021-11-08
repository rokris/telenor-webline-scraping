import requests
import pandas as pd
from bs4 import BeautifulSoup

# Access cookie from Webline
authsession = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MzY0MzQwMDAsImV4cGlyYXRpb24iOjEwODAwLCJsYXN0X3JlbW90ZV9pcCI6IjgxLjE2Ni4yMDIuMjI3Iiwib3RwIjoiZmxhc2gtc21zIiwicmVtb3RlX2lwIjoiODEuMTY2LjIwMi4yMjciLCJzaWQiOiIyRkRDNTk4QS00MDkxLTExRUMtOEVFMy1DMzUxQjFERTQwQjAiLCJ1c2VybmFtZSI6InJvZ2Vrcmk1In0.RfgX23FRw4rNkhmQNSkAEi-WJkqkTExO92gRmjK2wqM"
base_url = "https://webline.telenor.no/mod-perl/webline"
cookies = {'authsession': authsession}
payload = {'wlkid':'3633215',
           'id_customer':'1825',
           'Search':'Please%20wait...',
           'id_vpn':'1115925',
           'type':'partner',
           'cmd':'html_customer_vpn'}

export_path = './export_telenor_webline.csv'

# Get the date from Webline webserver
r = requests.post(base_url, data=payload, cookies=cookies)

# Create a nice Soup of the result
soup = BeautifulSoup(r.content, 'html5lib') # Parse the HTML as a string
table = soup.find_all('table')[4] # Grab a table
rows = table.find_all('td') # Find the data

# Put data into a Pandas DataFrame
df = pd.read_html(str(table))
df = df[0]
df['Admin Status'] = df['Admin Status'].map('{:.0f}'.format)
df['VPN Access ID'] = df['VPN Access ID'].map('{:.0f}'.format)
df['Site Id'] = df['Site Id'].map('{:.0f}'.format)
df = df.astype(str)
df['Bandwidth'] = df['Bandwidth'].str.replace('Kbits/s','')
df['Bandwidth'] = df['Bandwidth'].str.replace(' ','')
df.to_csv(export_path, encoding='utf-8', index=False)
