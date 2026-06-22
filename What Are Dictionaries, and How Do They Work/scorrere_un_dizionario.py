"""
possibile iterare su un dizionario se è necessario accedere
ed elaborare le sue coppie chiave-valore.
"""

prodotti = {
    "Laptop": 990,
    "Smartphone": 600,
    "Tablet": 250,
    "Headphones": 70,
}


# values() , keys() , items()

for valore in prodotti.values():
    print(valore)

for chiave in prodotti.keys():
    print(chiave)

for chiave, valore in prodotti.items():
    print(chiave, valore)


prodotti = {
    "Laptop": 990,
    "Smartphone": 600,
    "Tablet": 250,
    "Headphones": 70,
}

for prodotto, prezzo in prodotti.items():
    prodotti[prodotto] = round(prezzo * 0.8)

print(prodotti)


# enumerate() assegna un intero ad ogni coppia
for prodotto in enumerate(prodotti):
    print(prodotto)
"""
(0, 'Laptop')
(1, 'Smartphone')
(2, 'Tablet')
(3, 'Headphones')

"""

for indice, prodotto in enumerate(prodotti):
    print(indice, prodotto)
"""
0 Laptop
1 Smartphone
2 Tablet
3 Headphones
"""

# itterando sui valori:
for prodotto in enumerate(prodotti.values()):
    print(prodotto)
"""
(0, 792)
(1, 480)
(2, 200)
(3, 56)
"""

for indice, prodotto in enumerate(prodotti.values()):
    print(indice, prodotto)
"""
0 792
1 480
2 200
3 56
"""

for prodotto in enumerate(
    prodotti.items(),
):
    print(prodotto)
"""
(0, ('Laptop', 792))
(1, ('Smartphone', 480))
(2, ('Tablet', 200))
(3, ('Headphones', 56))
"""


for indice, prodotto in enumerate(prodotti.items(), 1):  # indice 1
    print(indice, prodotto)

"""
1 ('Laptop', 792)
2 ('Smartphone', 480)
3 ('Tablet', 200)
4 ('Headphones', 56)
"""
