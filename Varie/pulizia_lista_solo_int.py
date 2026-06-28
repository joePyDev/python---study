# pulizia lista da valori non interi:


lista = [1, 2, 3, 4, 5, "6", 7, 8, 9]
lista = [x for x in lista if type(x) == int]
"""
Prestare attenzione al uguaglianza di tipo, non di valore che 
non produrrebbe alcun risultato.
- type(x) == int confronto corretto di tipo
- x == int confronto non corretto, valuta il contenuto del oggetto

"""
