"""
Il programma richiederà all'utente di
inserire una posizione, contatterà un servizio web,
recupererà i dati in formato JSON dal servizio web, li analizzerà e
estrarrà il primo plus_code dal JSON.

Endpoint API
http://py4e-data.dr-chuck.net/opengeo?

Per chiamare l'API, è necessario fornire l'indirizzo richiesto
come parametro q= , opportunamente codificato in URL
utilizzando la funzione urllib.parse.urlencode()

"""

import urllib.request, urllib.parse
import json, ssl

# Heavily rate limited proxy of https://www.geoapify.com/ api
serviceurl = "http://py4e-data.dr-chuck.net/opengeo?"

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input("Enter location: ")
    if len(address) < 1:
        break

    address = address.strip()
    parms = dict()
    parms["q"] = address
    url = serviceurl + urllib.parse.urlencode(parms)
    print("Retrieving", url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read().decode()
    print("Retrieved", len(data), "characters")

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or "features" not in js:
        print("==== Download error ===")
        print(data)
        break

    if len(js["features"]) == 0:
        print("==== Object not found ====")
        print(data)
        break

    lista_pcode = list()
    lista_features = js["features"]
    for i in lista_features:
        lista_properties = i["properties"]
    for chiave, valore in lista_properties.items():
        if "plus_code" in chiave:
            lista_pcode.append(valore)
    print("Plus code", lista_pcode[0])
