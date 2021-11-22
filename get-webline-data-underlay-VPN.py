def main():
    import pandas as pd
    import requests
    from bs4 import BeautifulSoup

    # Access cookie from Webline
    authsession = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MzcyMTE2MDAsImV4cGlyYXRpb24iOjEwODAwLCJsYXN0X3JlbW90ZV9pcCI6IjgxLjE2Ni4yMDIuMjI3Iiwib3RwIjoiZmxhc2gtc21zIiwicmVtb3RlX2lwIjoiNzcuMTguNTAuNzE7ODEuMTY2LjIwMi4yMjciLCJzaWQiOiIwQkE5NEE5Ni00N0RGLTExRUMtQkY5My01RTUxQjFERTQwQjAiLCJ1c2VybmFtZSI6InJvZ2Vrcmk1In0.dtccyAzFfdYubYPCM9X_0eCPlOeDCz6-aiSJbVifZbI"  # noqa: E501
    base_url = "https://webline.telenor.no/mod-perl/webline"
    cookies = {"authsession": authsession}

    # Underlay VPN
    payload = {
        "wlkid": "3633215",
        "id_customer": "1825",
        "Search": "Please%20wait...",
        "id_vpn": "1115925",
        "type": "partner",
        "cmd": "html_customer_vpn",
        "sort": "SiteId",
    }

    export_path = "./export_telenor_webline_underlay_vpn.csv"

    # Get the date from Webline webserver
    r = requests.post(base_url, data=payload, cookies=cookies, stream=True)

    # Create a nice Soup of the result
    soup = BeautifulSoup(r.content, "html5lib")
    table = soup.find_all("table")[4]

    # Put data into a Pandas DataFrame
    df = pd.read_html(str(table))
    df = df[0]
    df["Admin Status"] = df["Admin Status"].map("{:.0f}".format)
    df["VPN Access ID"] = df["VPN Access ID"].map("{:.0f}".format)
    df["Site Id"] = df["Site Id"].map("{:.0f}".format)
    df = df.astype(str)
    df.to_csv(export_path, encoding="utf-8", index=False)


if __name__ == "__main__":
    main()
