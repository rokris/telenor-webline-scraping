# Telenor-Webline scraping

## How to get the Webline.html

### First get the cookies by loging in with your credentials and 2-factor.


wget --header "Cookie: authsession=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MzU4MjkyMDAsImV4cGlyYXRpb24iOjEwODAwLCJsYXN0X3JlbW90ZV9pcCI6IjgxLjE2Ni4yMDIuMjI3Iiwib3RwIjoiZmxhc2gtc21zIiwicmVtb3RlX2lwIjoiODEuMTY2LjIwMi4yMjciLCJzaWQiOiI0QkNBNkQyQy0zQUU2LTExRUMtODZGOS1CMDM5QjFERTQwQjAiLCJ1c2VybmFtZSI6InJvZ2Vrcmk1In0.5OSTmFSXkfhPvoHXSaTg2-RH5KsyNWaslIxX6cbib4I" https://webline.telenor.no/mod-perl/webline --post-data 'wlkid=3633215;id_customer=1825;Search=Please%20wait...;id_vpn=1115925;type=partner;cmd=html_customer_vpn'

## OR

curl -X POST https://webline.telenor.no/mod-perl/webline -d 'wlkid=3633215;id_customer=1825;Search=Please%20wait...;id_vpn=1115925;type=partner;cmd=html_customer_vpn' --header "Cookie: authsession=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MzU4MjkyMDAsImV4cGlyYXRpb24iOjEwODAwLCJsYXN0X3JlbW90ZV9pcCI6IjgxLjE2Ni4yMDIuMjI3Iiwib3RwIjoiZmxhc2gtc21zIiwicmVtb3RlX2lwIjoiODEuMTY2LjIwMi4yMjciLCJzaWQiOiI0QkNBNkQyQy0zQUU2LTExRUMtODZGOS1CMDM5QjFERTQwQjAiLCJ1c2VybmFtZSI6InJvZ2Vrcmk1In0.5OSTmFSXkfhPvoHXSaTg2-RH5KsyNWaslIxX6cbib4I"