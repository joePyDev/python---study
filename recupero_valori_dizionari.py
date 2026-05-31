# Dizionario annidato di esempio
studente = {"Pippo": {"eta": 20, "voto": 7}}

print("Dizionario originale:", studente)
print("-" * 50)

# Metodo 1: doppia parentesi quadra []
print("Metodo 1 - Doppia parentesi quadra []")
print("studente['Pippo']['eta']  ->", studente["Pippo"]["eta"])
print("studente['Pippo']['voto'] ->", studente["Pippo"]["voto"])
print()

# Metodo 2: .get() in cascata (più sicuro, evita KeyError)
print("Metodo 2 - .get() in cascata")
print("studente.get('Pippo', {}).get('eta')  ->", studente.get("Pippo", {}).get("eta"))
print("studente.get('Pippo', {}).get('voto') ->", studente.get("Pippo", {}).get("voto"))
print("(Se la chiave esterna non esiste, restituisce None senza errori)")
print()

# Metodo 3: Assegnare il dizionario interno a una variabile
print("Metodo 3 - Assegnazione a variabile intermedia")
dati_pippo = studente["Pippo"]
print("dati_pippo = studente['Pippo']")
print("dati_pippo['eta']  ->", dati_pippo["eta"])
print("dati_pippo['voto'] ->", dati_pippo["voto"])