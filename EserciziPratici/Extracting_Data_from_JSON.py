# Extracting Data from JSON

"""
l programma richiederà un URL,
leggerà i dati JSON da quell'URL utilizzando urllib,
quindi analizzerà ed estrarrà il numero di commenti dai dati JSON,
calcolerà la somma dei numeri nel file e inserirà la somma qui sotto.

"""

url1 = "http://py4e-data.dr-chuck.net/comments_42.json"
url2 = "http://py4e-data.dr-chuck.net/comments_2383209.json"


import urllib.request
import json

url = input("inserisci url: ")
if len(url) < 1:
    url = url2

apertura_url = urllib.request.urlopen(url)
data = apertura_url.read()
contenuto_json = json.loads(data)

lista_valori = []
for chiave in contenuto_json["comments"]:
    lista_valori.append(chiave["count"])


lista_valori = sum(lista_valori)
print(lista_valori)
