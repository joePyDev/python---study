"""
Scrivi una riga di codice Python che prenda questa lista ae crei
una nuova lista che contenga solo gli elementi pari di questa lista.
"""

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

lista = [x for x in a if x % 2 == 0]
