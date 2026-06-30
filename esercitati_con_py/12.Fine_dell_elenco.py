"""
Scrivi un programma che prenda in input un elenco di numeri
(ad esempio, a = [5, 10, 15, 20, 25]) e crei un nuovo elenco
contenente solo il primo e l'ultimo elemento dell'elenco dato.
Per esercitarti, scrivi questo codice all'interno di una funzione.

"""


def seziona_lista(lista):
    new_lista = [x for x in lista if x == lista[0] or x == lista[-1]]
    return new_lista


lista_utente = []

while True:
    inserimento_utente = int(input("Inserisci una seri di numeri: "))
    lista_utente.append(inserimento_utente)
    if len(lista_utente) == 5:
        break

A = seziona_lista(lista_utente)
