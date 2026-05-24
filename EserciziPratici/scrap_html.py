# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re
import sys




# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


try:
    url = input('Enter - ')
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
except Exception as e :
    print(f"inserisci un url valido errore {e}")
    sys.exit()

parte_cercata = '\d+'
somma = 0
tag_cercato = "span"

tags = soup.find_all(tag_cercato)

if tags == []:
    print(f"nessuna corrispondenza di tag {tag_cercato}")
    sys.exit()
for tag in tags:
    tag = str(tag)
    lista = (re.search(parte_cercata,tag))
    if lista:
        numero = int(lista.group())
        somma += numero
if not somma:
    print("non ci sono valori da sommare")    
else:
    print("la somma è",somma) 


