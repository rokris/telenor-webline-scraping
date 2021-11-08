import requests
import pandas as pd
from bs4 import BeautifulSoup


import_path = './webline.html'
export_path = './export_telenor_webline.csv'

with open(import_path, 'r', encoding = "ISO-8859-1") as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'html5lib') # Parse the HTML as a string

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
