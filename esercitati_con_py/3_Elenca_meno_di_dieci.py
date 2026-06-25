# 1 prints out all the elements of the list that are less than 5.

lista = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for elemento in lista:
    if elemento < 5:
        print(elemento)


"""
#2
Invece di stampare gli elementi uno per uno, crea un nuovo elenco che contenga tutti gli elementi inferiori a 5 di questo elenco e stampa questo nuovo elenco.
"""
new_lista = []

for elemento in lista:
    if elemento < 5:
        new_lista.append(elemento)
print(new_lista)


"""
#3
Scrivi questo in una sola riga di codice Python.
"""
new_new_lista = [elemento for elemento in lista if elemento < 5]


"""
Chiedi all'utente di inserire un numero e restituisci un elenco contenente solo gli elementi dell'elenco originale ache sono inferiori al numero fornito dall'utente.
"""
digit = int(input("Inserisci un numero"))
new_new_new_lista = [elemento for elemento in lista if elemento < digit]
