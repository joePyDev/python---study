
"""
Scenario del cliente:
“Ho bisogno di una lista di tutti i libri presenti in questa pagina, con titolo e prezzo, da salvarmi in un file CSV.”

https://books.toscrape.com/




Fare una richiesta HTTP con requests

Analizzare l’HTML con BeautifulSoup

Estrarre dati mirati e pulirli

Salvarli in un CSV con csv (o pandas)

Gestire eventuali errori di connessione



Logica del procedimento
Scarica il codice HTML della pagina

Individua il blocco che contiene ogni prodotto (ispezionando la pagina)

Per ogni blocco, estrai titolo e prezzo

Pulisci i dati (togli caratteri inutili)

Scrivi i dati in un file CSV




"""

import requests
from bs4 import BeautifulSoup
import csv

url = 'http://books.toscrape.com/'

try:
    risposta = requests.get(url)
    risposta.raise_for_status()   # controlla errori HTTP
    html = risposta.text
except requests.exceptions.RequestException as e:
    print(f"Errore nel caricamento della pagina: {e}")
    exit()


soup = BeautifulSoup(html, 'html.parser')

prodotti = soup.find_all('article', class_='product_pod')
print(f'Trovati {len(prodotti)} prodotti.')

dati_libri = []

for prodotto in prodotti:
    # Titolo: prendiamo l'attributo 'title' del link dentro h3
    titolo = prodotto.h3.a['title'].strip()
    
    # Prezzo: prendiamo il testo dentro <p class="price_color">
    prezzo_elemento = prodotto.find('p', class_='price_color')
    prezzo = prezzo_elemento.text.strip()   # es. 'Â£51.77'
    
    # Puliamo il simbolo della sterlina (opzionale, ma il cliente vuole solo numero)
    prezzo_pulito = prezzo.replace('Â£', '').replace('£', '')
    
    dati_libri.append([titolo, prezzo_pulito])

print(dati_libri[:3])  # vediamo i primi 3














