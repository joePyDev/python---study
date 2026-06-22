# https://books.toscrape.com/catalogue/category/books/fantasy_19/index.html

# ispeziona su pulsante next :


"""
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
"""

"""






1. Imposta url_partenza = "https://.../index.html"
2. Crea una lista vuota per tutti i libri
3. Finché esiste una url:
    3.1 Scarica la pagina con requests
    3.2 Crea la soup
    3.3 Estrai i libri dalla pagina (con find_all...)
    3.4 Aggiungi i libri alla lista totale
    3.5 Cerca il tag li class="next"
    3.6 Se esiste, prendi href e costruisci il nuovo url (sostituendo index.html con href)
    3.7 Altrimenti, esci dal ciclo
4. Dopo il ciclo, salva la lista in CSV
"""


import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv


def apertura_url(url):
    """si passa l'url , richiesta ,ritorna la zuppa senno none"""
    r = requests.get(url)
    if r.status_code != 200:
        print("errore richiesta url")
        return
    soup = BeautifulSoup(r.text, "html.parser")
    return soup


def collezione_libri(soup, url_corrente):
    lista_libri = []
    # Trova tutti i contenitori dei libri (article con classe product_pod)
    articoli = soup.find_all("article", class_="product_pod")

    for articolo in articoli:
        # Estrai titolo (dall'attributo title del tag a dentro h3)
        titolo_tag = articolo.find("h3").find("a")
        titolo = titolo_tag.get("title")

        # Estrai link relativo e trasformalo in assoluto
        link_relativo = titolo_tag.get("href")
        link = urljoin(url_corrente, link_relativo)

        # Estrai prezzo (p con classe price_color), togli il simbolo £
        prezzo_tag = articolo.find("p", class_="price_color")
        prezzo = prezzo_tag.text.replace("£", "")  # oppure prezzo[1:]

        # Estrai disponibilità (p con classe instock availability)
        disponibilita_tag = articolo.find("p", class_="instock availability")
        disponibilita = disponibilita_tag.text.strip()

        # Crea un dizionario con i dati del libro
        libro_info = {
            "titolo": titolo,
            "prezzo": prezzo,
            "disponibilita": disponibilita,
            "link": link,
        }
        lista_libri.append(libro_info)

    return lista_libri


def cerca_url_pulsante(soup, url_corrente):
    pulsante_next = soup.find("li", class_="next")
    if not pulsante_next:
        return
    href_relativo = pulsante_next.find("a")
    nuovo_url = urljoin(url_corrente, href_relativo.get("href"))
    return nuovo_url


url = "https://books.toscrape.com/catalogue/category/books/fantasy_19/index.html"
contatore = 0
tutti_libri = []


while True:
    # ----------------------------------------------------------------------
    soup = apertura_url(url)
    if not soup:
        break
    tutti_libri.extend(collezione_libri(soup, url))
    prossimo_url = cerca_url_pulsante(soup, url)
    prossimo_url = cerca_url_pulsante(soup, url)
    if not prossimo_url:
        break
    url = prossimo_url
    # ----------------------------------------------------------------------


with open("fantasy_book_csv", "w", newline="", encoding="utf-8") as f:
    write = csv.DictWriter(f, fieldnames=["titolo", "prezzo", "disponibilita", "link"])
    write.writeheader()
    write.writerows(tutti_libri)

print(f"Salvati {len(tutti_libri)} libri in fantasy_books.csv")
