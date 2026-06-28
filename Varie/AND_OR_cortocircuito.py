# operatore OR:

risultato_or = 10 or 0  # ritorna 10 truthy

# operatore AND:

risultato_and = 10 and 0 and 5  # ritorna 0 falsy

# -----------------------------------------------------------


# esempi pratici:

# Se l'utente non scrive niente, input restituisce "" (stringa vuota, falsy)
nome = input("Inserisci nome: ") or "Anonimo"


# protezione da errori:
utenti = [{"nome": "Luca"}, {"nome": "Mario"}, {"nome": "Anna"}]
# se la lista è vuota non ritorna errore
if utenti and utenti[0]["nome"] == "Mario":
    print("Trovato!")
else:
    print("lista vuota o nome npon trovato")
