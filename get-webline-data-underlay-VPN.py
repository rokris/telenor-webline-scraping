import jwt
import pandas as pd
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://webline.telenor.no/mod-perl/webline"
EXPORT_PATH_CSV = "./export_telenor_webline_underlay_vpn.csv"
EXPORT_PATH_JSON = "./export_telenor_webline_underlay_vpn.json"

def getJwt():
    while True:
        jwt_string = input("Access cookie: ")
        try:
            jwt.decode(
                jwt_string, 
                algorithms="HS256", 
                key="", 
                options={"verify_exp": True, "verify_signature": False}
            )
        except:
            print("Invalid JWT")
        else:
            return jwt_string


def scrapeWebline():
    # Get all VPN links
    cookies = {"authsession": getJwt()}
    payload = {
        "wlkid": "3633215",
        "id_customer": "1825",
        "Search": "Please%20wait...",
        "id_vpn": "1115925",
        "type": "partner",
        "cmd": "html_customer_vpn",
        "sort": "SiteId",
    }

    result = requests.post(
        BASE_URL, 
        data=payload, 
        cookies=cookies, 
        stream=True
    )
    return result


def createDataset(result):
    # Create a nice Soup of the result
    soup = BeautifulSoup(result.content, "html5lib")
    table = soup.find_all("table")[4]
    
    # Put data into a Pandas DataFrame
    df = pd.read_html(str(table))
    df = df[0]
    df["Admin Status"] = df["Admin Status"].map("{:.0f}".format)
    df["VPN Access ID"] = df["VPN Access ID"].map("{:.0f}".format)
    df["Site Id"] = df["Site Id"].map("{:.0f}".format)
    df = df.astype(str)
    
    return df


def main():

    # Get the date from Webline webserver
    result = scrapeWebline()

    # Create Pandas dataset
    dataset = createDataset(result)

    # Export data to files
    dataset.to_csv(EXPORT_PATH_CSV, encoding="utf-8", index=False)
    dataset.to_json(EXPORT_PATH_JSON, index=False, orient="table")


if __name__ == "__main__":
    main()