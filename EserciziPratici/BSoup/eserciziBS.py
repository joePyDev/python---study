import requests
from bs4 import BeautifulSoup
import sys

url = "http://books.toscrape.com/"
response = requests.get(url)

if response.status_code == 200:
    print("Pagina scaricata con successo")
else:
    print(f"Errore {response.status_code}")
    sys.exit()
    
soup = BeautifulSoup(response.text,"html.parser")    


title_tag = soup.find('title')
print("Titolo della pagina:", title_tag.text)

paragrafi = soup.find_all('p')
print(f"\nNumero di paragrafi trovati: {len(paragrafi)}")
# Stampa solo il primo paragrafo come esempio
if paragrafi:
    print("Primo paragrafo:", paragrafi[0].text[:100])
    
