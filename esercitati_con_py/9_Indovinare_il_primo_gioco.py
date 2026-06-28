"""
Genera un numero casuale tra 1 e 9 (inclusi 1 e 9).
Chiedi all'utente di indovinare il numero,
poi comunicagli se ha indovinato troppo poco,
troppo tanto o esattamente il numero corretto.

"""

import random


def genera_numero():
    return random.randint(1, 9)


def confronto_numeri(numero_casuale, numero_utente):
    numero_utente = int(numero_utente)
    if numero_casuale > numero_utente:
        return "Il numero casuale era più alto del tuo!"
    elif numero_casuale < numero_utente:
        return "Il numero casuale era più basso del tuo!"
    else:
        return "Hai indovinato il numero casuale!"


contatore = 0
while True:
    numero_casuale = genera_numero()
    numero_utente = input(
        """Indovina il numero casuale da 1 a 9 ,exit per terminare """
    )
    if numero_utente == "exit":
        print(f"tentativo numero {contatore}")
        break
    else:
        try:
            confronto = confronto_numeri(numero_casuale, numero_utente)
        except ValueError as e:
            print(f"errore , inserisci un numero , {e}")
            break
        contatore += 1
        print(confronto)
