import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl  # defaults to certificate verification and most secure protocol (now TLS)
import sys


def selezione_link(tags, posizione):
    """cicla i link e trova quello corrispondente alla posizione"""
    count = 0
    for tag in tags:
        link_aperto = tag.get("href", None)
        count += 1
        if count == int(posizione):
            print(link_aperto)
            return link_aperto


def apertura_link(url, posizione):
    """si passa url e posizione link da trovare di ritorno"""
    try:
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, "html.parser")
        tags = soup("a")
    except Exception as errore:
        print(f"Errore inserimento url {errore}")
        sys.exit()
    if not isinstance(posizione, int):
        print(
            f"Inserire una posizione corretta,solo numeri, inserito {type(posizione)}"
        )
        sys.exit()
    link_selezionato = selezione_link(tags, posizione)
    return link_selezionato


# Ignore SSL/TLS certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input("Enter URL: ")
position = 18
count = 7
flag = None

print(f"Enter count: {count}")
print(f"Enter Position: {position}")
print(url)
for ciclo in range(count):
    if flag == None:
        link = apertura_link(url, position)
        flag = "triggherata"
    else:
        link = apertura_link(link, position)
