
# dir() 
# help()





dizionario = {}
contatore = 0

with open(r"C:\Users\gioel\OneDrive\Desktop\words.txt") as fhand:
    for riga in fhand:
        # 1. Puliamo la riga e dividiamola in una lista di parole
        parole_della_riga = riga.strip().split()
        
        # 2. Iteriamo su ogni singola parola estratta
        for parola in parole_della_riga:
            # Opzionale: puliamo la punteggiatura se necessario
            parola_pulita = parola.lower().strip(",.?!")
            
            if parola_pulita not in dizionario:
                dizionario[parola_pulita] = contatore
                contatore += 1



print(dizionario)
# Ora questa ricerca darà True
print("writing" in dizionario)