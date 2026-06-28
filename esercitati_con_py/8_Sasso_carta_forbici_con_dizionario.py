import random

# Inizializzo le variabili a None (valore "sentinella")
lancio_utente = None
lancio_pc = None

# Dizionario delle regole: chiave = mossa che vince, valore = mossa che perde
vince_su = {
    "1": "3",  # sasso batte forbici
    "3": "2",  # forbici battono carta
    "2": "1",  # carta batte sasso
}

while True:
    print("\nIniziamo una nuova partita? y / n")
    start_game = input("> ")

    if start_game == "y":
        print("Bene, Iniziamo!!")
        print("Scegli il lancio: sasso = 1, carta = 2, forbice = 3")
        lancio_utente = input("> ")
        lancio_pc = str(random.randint(1, 3))

        # --- Controllo input valido ---
        if lancio_utente not in ("1", "2", "3"):
            print("Inserimento numero non consentito, esco.")
            break

        # --- Confronto con il dizionario ---
        if lancio_utente == lancio_pc:
            print("Pareggio!! Ritenta!!")
        elif vince_su[lancio_utente] == lancio_pc:
            print(f"Hai vinto! {lancio_utente} batte {lancio_pc}")
        else:
            print(f"Hai perso! {lancio_pc} batte {lancio_utente}")

    elif start_game == "n":
        print("Ciao, alla prossima!")
        break
    else:
        print("Input non valido. Uscita.")
        break

# --- Debug finale: stampa solo se almeno uno dei due ha un valore ---
if lancio_pc or lancio_utente:
    print("Debug - Ultimo lancio:", lancio_utente, lancio_pc)
