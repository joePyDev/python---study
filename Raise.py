# sintassi : raise [Eccezione] [("messaggio")]
"""
Se nessuno lo cattura con try/except, allora Python lo manda automaticamente a console e il programma si interrompe (crasha).

Se lo catturi con try/except, puoi gestirlo come vuoi (stamparlo, ignorarlo, correggerlo) e il programma continua senza crashare.
"""


# Sollevare un'eccezione built‑in
def dividi(a, b):
    if b == 0:
        raise ValueError("Il divisore non può essere zero!")
    return a / b

# Uso
try:
    risultato = dividi(10, 0)
except ValueError as e:
    print("Errore:", e, "debug")   # Errore: Il divisore non può essere zero!



# Validare un tipo di dato
def stampa_nome(nome):
    if not isinstance(nome, str):
        raise TypeError(f"Ci si aspetta una stringa, ricevuto {type(nome)}")
    print(f"Ciao {nome}")    
    
stampa_nome(123)    


# Rilanciare un'eccezione dopo aver fatto qualcosa
try:
    data = int(input("Inserisci un numero"))
except ValueError:
    print("Input non valido. Rilancio l'errore.")    
    raise
    
   
# raise SENZA try/except (va a console e crasha)
def calcola_età(anno_nascita):
    if anno_nascita > 2024:
        raise ValueError("L'anno non può essere futuro!")
    return 2024 - anno_nascita

# Nessun try/except qui
eta = calcola_età(2030)  # L'errore viene sollevato, va in console e il programma si ferma

print("Questo non viene mai stampato")
    
    