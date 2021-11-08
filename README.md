# Telenor-Webline scraping

## How to get the Webline.html

### First get the cookies by loging in with your credentials and 2-factor.


wget --header "Cookie: authsession=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MzY0MzQwMDAsImV4cGlyYXRpb24iOjEwODAwLCJsYXN0X3JlbW90ZV9pcCI6IjgxLjE2Ni4yMDIuMjI3Iiwib3RwIjoiZmxhc2gtc21zIiwicmVtb3RlX2lwIjoiODEuMTY2LjIwMi4yMjciLCJzaWQiOiIyRkRDNTk4QS00MDkxLTExRUMtOEVFMy1DMzUxQjFERTQwQjAiLCJ1c2VybmFtZSI6InJvZ2Vrcmk1In0.RfgX23FRw4rNkhmQNSkAEi-WJkqkTExO92gRmjK2wqM" https://webline.telenor.no/mod-perl/webline --post-data 'wlkid=3633215;id_customer=1825;Search=Please%20wait...;id_vpn=1115925;type=partner;cmd=html_customer_vpn' -O webline.html

## OR

curl -X POST https://webline.telenor.no/mod-perl/webline -d 'wlkid=3633215;id_customer=1825;Search=Please%20wait...;id_vpn=1115925;type=partner;cmd=html_customer_vpn' --header "Cookie: authsession=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MzY0MzQwMDAsImV4cGlyYXRpb24iOjEwODAwLCJsYXN0X3JlbW90ZV9pcCI6IjgxLjE2Ni4yMDIuMjI3Iiwib3RwIjoiZmxhc2gtc21zIiwicmVtb3RlX2lwIjoiODEuMTY2LjIwMi4yMjciLCJzaWQiOiIyRkRDNTk4QS00MDkxLTExRUMtOEVFMy1DMzUxQjFERTQwQjAiLCJ1c2VybmFtZSI6InJvZ2Vrcmk1In0.RfgX23FRw4rNkhmQNSkAEi-WJkqkTExO92gRmjK2wqM" -o webline.html