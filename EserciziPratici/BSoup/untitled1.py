

# https://books.toscrape.com/catalogue/category/books/fantasy_19/index.html

# ispeziona su pulsante next : 


import sys
import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/catalogue/category/books/fantasy_19/index.html"
# Scrivi la riga per importare la libreria requests e la riga per fare la richiesta GET all'URL.
r = requests.get('https://books.toscrape.com/catalogue/category/books/fantasy_19/index.html')

if r.status_code != 200:
    print("Errore nel download")
    exit()    
    
soup = BeautifulSoup(r.text,"html.parser")

tag = soup.find("li",class_="next")
tag = tag.find("a")
tag = tag.get("href")
page2_tag = url.replace("index.html","page-2.html")






url = "https://books.toscrape.com/catalogue/category/books/fantasy_19/index.html"
lista_libri = []
contatore = 0

while True:
    r = requests.get(url)
    if r.status_code != 200:
        print("errore richiesta url")
        break
    soup = BeautifulSoup(r.text,"html.parser")
    
    libri = soup.find_all("h3")
    for libro in libri:
        lista_libri.append(libro.text)
    
    pulsante_next = soup.find("li" , class_="next")
    if not pulsante_next: break
   # nuovo_url = url.replace()
    

    # contatore provvisorio per evitare ciclo infinito in fase di test
    contatore = contatore +1
    if contatore == 1: break




   
    
    
    
    
    
    
    