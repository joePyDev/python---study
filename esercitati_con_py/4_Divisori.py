"""
Crea un programma che chieda all'utente di inserire un numero e
poi stampi un elenco di tutti i divisori di quel numero.
"""

import sys

try:
    divisore = int(input("inserisci un numero: "))
except ValueError as e:
    print(f"inserisci un numero valido, errore: {e}")
    sys.exit()
else:
    lista_divisori = []
    if divisore <= 0:
        print(f"inserisci un numero positivo, hai digitato {divisore}")
        sys.exit()
    for i in range(1, divisore + 1):
        if divisore % i == 0:
            lista_divisori.append(i)
    print(f"Lista divisori di {divisore} è {lista_divisori}")
