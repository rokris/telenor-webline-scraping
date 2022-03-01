# Telenor-Webline-Scraping
##
### Webline authsession cookie
>First get the cookie by loging in with your credentials and 2-factor and copy the cookie authsession:\<value> from the browser. <https://webline.telenor.no>
### Create a Python environment using Anaconda
>`conda create --name py310 python=3.10'`\
`conda activate py310`
### Install Python requirements
>`pip install -r requirements.txt`
### To start application
>`python get-webline-data-underlay-VPN.py`\
or\
`python get-webline-data-all.py`
---
## Environment
> This application is tested with Python 3.10
---
## Reference
### 1. wget
#### All VPN wget
>``wget --header "Cookie: authsession=<value>" https://webline.telenor.no/mod-perl/webline --post-data 'wlkid=3633215;id_customer=1825;View%20All=Please%20wait...;type=partner;table=customer;id=1825;key=id_customer;cmd=mvpnlist_region;county=all;sort=SiteId' -O webline.html``
#### Underlay VPN wget
>``wget --header "Cookie: authsession=<value>" https://webline.telenor.no/mod-perl/webline --post-data 'wlkid=3633215;id_customer=1825;Search=Please%20wait...;id_vpn=1115925;type=partner;cmd=html_customer_vpn' -O webline.html``
---
### 2. cURL
#### All VPN curl
>``curl -X POST https://webline.telenor.no/mod-perl/webline -d 'wlkid=3633215;id_customer=1825;View%20All=Please%20wait...;type=partner;table=customer;id=1825;key=id_customer;cmd=mvpnlist_region;county=all;sort=SiteId' --header "Cookie: authsession=<value>" -o webline.html``
#### Underlay VPN curl
>``curl -X POST https://webline.telenor.no/mod-perl/webline -d 'wlkid=3633215;id_customer=1825;Search=Please%20wait...;id_vpn=1115925;type=partner;cmd=html_customer_vpn' --header "Cookie: authsession=<value>" -o webline.html``
