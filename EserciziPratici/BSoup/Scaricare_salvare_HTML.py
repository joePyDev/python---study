# Scaricare la pagina http://books.toscrape.com/ e salvarla in un file books.html.

from bs4 import BeautifulSoup

# Quale libreria Python si usa per fare richieste HTTP?
import requests

# Scrivi la riga per importare la libreria requests e la riga per fare la richiesta GET all'URL.
r = requests.get("http://books.toscrape.com/")

if r.status_code != 200:
    print("Errore nel download")
    exit()

# si crea il file con il contenuto html della pagina
with open("nuovo_book_html", "w", encoding="utf-8") as file:
    file.write(r.text)  # .write() è un metodo dei file python


# apriamo il file in lettura
with open("nuovo_book_html", "r", encoding="utf-8") as file:
    contenuto_html = file.read()  # .read() è un metodo dei file python


# crea l'albero html con la zuppa!
soup = BeautifulSoup(contenuto_html, "html.parser")

# trova il contenuto del tag title
print(soup.find("title").text)


# cerca tutti i tag h3
h3 = soup.find_all("h3")


# quanti h3 trova nella pagina
print(len(h3), "\n")


# accesso al primo libro della lista
primo_libro = h3[0]


# Trova il div che contiene le info sul prezzo
contenitore_prezzo = soup.find("div", class_="product_price")
# All'interno di quel div, trova il prezzo
prezzo = contenitore_prezzo.find("p", class_="price_color").text
prezzo_pulito = prezzo[1:]
print("Prezzo estratto (combinato):", prezzo_pulito)
