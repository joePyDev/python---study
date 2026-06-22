import requests
from bs4 import BeautifulSoup

r = requests.get("http://books.toscrape.com/")

"""print(r.status_code)
print(type(r.text))
print(len(r.text))
print(r.text[:400])"""


with open("mio_sito.html", "w") as file:
    file.write(r.text)

with open("mio_sito.html") as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, "html.parser")

print(soup.find("title").text)

libri = soup.find_all(class_="product_pod")
print(f"numero libri trovati {len(libri)}")

primo_libro = soup.find("h3").get_text()

print("\n>>>>>>\n")
print(primo_libro)


indice = 0
lista_libri = soup.find_all("h3")
for libro in lista_libri:
    indice = indice + 1
    print(f"indice libro n:{indice}", libro.get_text())
