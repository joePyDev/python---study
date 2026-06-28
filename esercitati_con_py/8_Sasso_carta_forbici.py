"""
Crea un gioco di sasso-carta-forbici per due giocatori.

Suggerimento:
    chiedi ai giocatori di fare le loro mosse (usando input)
    confrontale,
    stampa un messaggio di congratulazioni al vincitore
    chiedi se vogliono iniziare una nuova partita .

Ricorda le regole:

il sasso batte le forbici
Le forbici battono la carta
La carta batte sasso

"""

import random

lancio_utente = None
lancio_pc = None
# inizio gioco
while True:
    print("Iniziamo una nuova partita? y / n ")
    start_game = input("> ")
    if start_game == "y":
        # richiesta input
        print("Bene,Iniziamo!!")
        print("Scegli il lancio: sasso = 1 , carta = 2 , forbice = 3")
        lancio_utente = input("> ")
        lancio_pc = str(random.randint(1, 3))  # both included

        # confronto sasso batte forbici
        if lancio_utente == "1" and lancio_pc == "3":
            print("Hai vinto, sasso batte forbici")
            continue

        # confronto forbici battono la carta
        elif lancio_utente == "3" and lancio_pc == "2":
            print("Hai vinto, forbici batte carta")
            continue

        # confronto carta batte sasso
        elif lancio_utente == "2" and lancio_pc == "1":
            print("Hai vinto, carta batte sasso")
            continue
        # confronto sasso batte forbici
        elif lancio_pc == "1" and lancio_utente == "3":
            print("Hai perso, sasso batte forbici")
            continue

        # confronto forbici battono la carta
        elif lancio_pc == "3" and lancio_utente == "2":
            print("Hai perso, forbici batte carta")
            continue

        # confronto carta batte sasso
        elif lancio_pc == "2" and lancio_utente == "1":
            print("Hai perso, carta batte sasso")
            continue

        # confronto pareggio
        elif lancio_utente == lancio_pc:
            print("Pareggio!! , ritenta!!")
            continue
        else:
            print("inserimento numero non consentito,esco")
            break
    elif start_game == "n":

        print("Ciao,alla prossima!")

        break
    else:
        print(
            "Bonifico andato a buon fine,il programmatore ringrazia! spammm!!"
        )
        break

if lancio_pc or lancio_utente:
    print("Debug", lancio_utente, lancio_pc)
