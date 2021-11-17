import requests
import pandas as pd
from bs4 import BeautifulSoup

# Access cookie from Webline
authsession = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MzcyMTE2MDAsImV4cGlyYXRpb24iOjEwODAwLCJsYXN0X3JlbW90ZV9pcCI6Ijc3LjE4LjUwLjcxIiwib3RwIjoiZmxhc2gtc21zIiwicmVtb3RlX2lwIjoiNzcuMTguNTAuNzEiLCJzaWQiOiI2Nzk2RUM4MC00N0FBLTExRUMtQTE1OS1GODY2QjFERTQwQjAiLCJ1c2VybmFtZSI6InJvZ2Vrcmk1In0.yd3l2W5IuaLuEij_U7VQZf-wm1iv7AwNaPiQKSqrF6o"
base_url = "https://webline.telenor.no/mod-perl/webline"
cookies = {'authsession': authsession}

## All VPN
payload = {
    'wlkid': '3633215',
    'id_customer': '1825',
    'View%20All': 'Please%20wait...',
    'type': 'partner',
    'table': 'customer',
    'id': '1825',
    'key': 'id_customer',
    'cmd': 'mvpnlist_region',
    'county': 'all',
    'sort': 'SiteId'
}

export_path = './export_telenor_webline_all.csv'

# Get the date from Webline webserver
r = requests.post(base_url, data=payload, cookies=cookies, stream=True)

# Create a nice Soup of the result
soup = BeautifulSoup(r.content, 'html5lib') # Parse the HTML as a string
table = soup.find_all('table')[3] # Grab a table

# Put data into a Pandas DataFrame
df = pd.read_html(str(table))
df = df[0]
df['Admin Status'] = df['Admin Status'].map('{:.0f}'.format)
df['VPN Access Count'] = df['VPN Access Count'].map('{:.0f}'.format)
df['Site ID'] = df['Site ID'].map('{:.0f}'.format)
df = df.astype(str)
#df['Bandwidth'] = df['Bandwidth'].str.replace('Kbits/s','')
#df['Bandwidth'] = df['Bandwidth'].str.replace(' ','')
df.to_csv(export_path, encoding='utf-8', index=False)
