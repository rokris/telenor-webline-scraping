# Telenor-Webline scraping
## Webline authsession cookie
>First get the cookie by loging in with your credentials and 2-factor and copy the cookie authsession:\<value> from the browser. https://webline.telenor.no

> Change the value of authsession variable in the file *.py
---
## Reference
### 1. wget

>``wget --header "Cookie: authsession=<value>" https://webline.telenor.no/mod-perl/webline --post-data 'wlkid=3633215;id_customer=1825;Search=Please%20wait...;id_vpn=1115925;type=partner;cmd=html_customer_vpn' -O webline.html``

### 2 cURL

>``curl -X POST https://webline.telenor.no/mod-perl/webline -d 'wlkid=3633215;id_customer=1825;Search=Please%20wait...;id_vpn=1115925;type=partner;cmd=html_customer_vpn' --header "Cookie: authsession=<value>" -o webline.html``