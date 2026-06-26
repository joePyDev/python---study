"""
Chiedi all'utente di inserire una stringa e stampa se questa è palindroma o meno.
"""

import string

frase = input("Inserisci una frase: ")

frase_pulita = ""
for carattere in frase.lower():
    if carattere != " " and carattere not in string.punctuation:
        frase_pulita += carattere

if not frase_pulita:
    print("Non hai inserito caratteri validi!")
else:

    inversa = frase_pulita[::-1]

    print(f"Frase pulita: {frase_pulita}")
    print(f"Frase inversa: {inversa}")

    if frase_pulita == inversa:
        print("Palindroma!!")
    else:
        print("Non è palindroma")
