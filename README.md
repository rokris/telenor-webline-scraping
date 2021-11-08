# Telenor-Webline scraping

## How to download the webline.html file
---
## 1. Loging in to Webline with your credentials
>First get the cookie by loging in with your credentials and 2-factor and copy the cookie authsession:\<value>

## 2. Replace the value in the command

>``wget --header "Cookie: authsession=<value>" https://webline.telenor.no/mod-perl/webline --post-data 'wlkid=3633215;id_customer=1825;Search=Please%20wait...;id_vpn=1115925;type=partner;cmd=html_customer_vpn' -O webline.html``

## **OR**

>``curl -X POST https://webline.telenor.no/mod-perl/webline -d 'wlkid=3633215;id_customer=1825;Search=Please%20wait...;id_vpn=1115925;type=partner;cmd=html_customer_vpn' --header "Cookie: authsession=<value>" -o webline.html``