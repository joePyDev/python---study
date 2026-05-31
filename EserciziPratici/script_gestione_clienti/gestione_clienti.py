import json 
import os

#----------------------------------------------------------------
"""
30/05/2026 

beta test strumento gestione clienti basic
G.P.
"""
#----------------------------------------------------------------
def verifica_file_txt():
    percorso = "clienti.txt"
    if os.path.exists(percorso):
        with open(percorso, "r", encoding="utf-8") as f:
            try:
                dati = json.load(f)
                if dati is None:
                    print("File corrotto (contiene null). Verrà ricreato.")
                    return {}
                return dati
            except json.JSONDecodeError:
                print("File vuoto o non valido. Verrà ricreato.")
                return {}
    else:
        with open(percorso, "w", encoding="utf-8") as f:
            json.dump({}, f)
        return {}
#----------------------------------------------------------------
          
#----------------------------------------------------------------        
def aggiungi_cliente(clienti):
    """ inserimento nuovi clienti """
    if not clienti:
        nuovo_codice = 1
    else:
        # Prendi tutte le chiavi, convertile in interi, poi prendi il massimo
        chiavi_interi = [int(k) for k in clienti.keys()]
        nuovo_codice = max(chiavi_interi) + 1
    nome_cliente = input("Inserisci nome e cognome del cliente: ")
    clienti[str(nuovo_codice)] = {"nome": nome_cliente.title(),"servizi": []} # crea una nova chiave
    print(f"Cliente {nome_cliente} aggiunto con codice {nuovo_codice}.")
    return clienti
#----------------------------------------------------------------
    
#----------------------------------------------------------------
def salva_clienti(clienti):
    if clienti is None:
        clienti = {}
    percorso = "clienti.txt"
    with open(percorso, "w", encoding="utf-8") as f:
        json.dump(clienti, f, indent=4)
#----------------------------------------------------------------

#----------------------------------------------------------------
def aggiungi_servizio(clienti):
    """si aggiunge i servizi del caso, ritorna l'elenco aggiornato """
    codice = input("Inserire il codice cliente: ")
    if not codice in clienti:
        return clienti
    data = input("Data (YYYY-MM-DD): ")
    tipo = input("Tipo di servizio: ")
    costo = float(input("Costo: "))
    servizio = {"data" : data, "tipo" : tipo , "costo" : costo}
    clienti[codice]["servizi"].append(servizio)
    print(f"Servizio aggiunto al cliente {clienti[codice]['nome']} (codice {codice})")
    return clienti
#----------------------------------------------------------------
    
#----------------------------------------------------------------    
def elenco_clienti(clienti):
    """ ritorna la lista dei clienti """
    if not clienti:
        print("Nessun cliente presente")
    else:
        for codice , dati in clienti.items():
            print(f"Codice: {codice} - Nome: {dati['nome']}")
#----------------------------------------------------------------
    
#----------------------------------------------------------------
def mostra_servizi(clienti):
    codice = input("Inserisci codice cliente: ")
    if not codice in clienti:
        print("Cliente non trovato")
        return clienti
    else: 
        servizi = clienti[codice]["servizi"]
        if not servizi:
            print("Nessun servizio registrato per questo cliente.")
        for i , servizio in enumerate(servizi,start=1):
            print(f"Servizio {i}: {servizio['data']} - {servizio['tipo']} - {servizio['costo']}€")
#----------------------------------------------------------------
             
#----------------------------------------------------------------
def modifica_nome_cliente(clienti):
    """ modifica il nome del cliente passato dal dizionario """
    codice = input("Codice cliente da modificare: ")
    if codice in clienti:
        nome_vecchio = clienti[codice]["nome"]
        nuovo_nome = input(f"Nome Attuale : {nome_vecchio}. Nuovo Nome: ")
        clienti[codice]["nome"] = nuovo_nome
        print("Nome aggiornato")
    else:
        print("codice cliente non trovato")
    return clienti
#----------------------------------------------------------------

#----------------------------------------------------------------
def gestisci_servizi_clienti(clienti):
    """ elimina modifica servizi in dizionario """
    codice = input("Inserisci il codice cliente: ")
    if codice not in clienti:
        print("Cliente non trovato")
        return clienti
    
    servizi = clienti[codice]["servizi"]
    if not servizi:
        print("Nessun servizio registrato per questo cliente.")
        return clienti
    
    # Mostra servizi
    for i, s in enumerate(servizi, start=1):
        print(f"{i}. {s['data']} - {s['tipo']} - {s['costo']}€")
    
    try:
        idx = int(input(f"Scegli il servizio (1-{len(servizi)}): ")) - 1
        if idx < 0 or idx >= len(servizi):
            print("Numero non valido.")
            return clienti
    except ValueError:
        print("Devi inserire un numero.")
        return clienti
    
    azione = input("Cosa fare? (M)odifica, (E)limina, (A)nnulla: ").upper()
    
    if azione == "M":
        # Modifica il servizio esistente
        servizio = servizi[idx]
        nuova_data = input(f"Nuova data ({servizio['data']}): ")
        if nuova_data:
            servizio["data"] = nuova_data
        nuovo_tipo = input(f"Nuovo tipo ({servizio['tipo']}): ")
        if nuovo_tipo:
            servizio["tipo"] = nuovo_tipo
        nuovo_costo = input(f"Nuovo costo ({servizio['costo']}): ")
        if nuovo_costo:
            servizio["costo"] = float(nuovo_costo)
        print("Servizio modificato.")
    elif azione == "E":
        del servizi[idx]
        print("Servizio eliminato.")
    elif azione == "A":
        print("Operazione annullata.")
    else:
        print("Azione non riconosciuta.")
    
    return clienti
#----------------------------------------------------------------


stringa_iniziale = """
1. Nuovo cliente
2. Aggiungi servizio a cliente esistente
3. Mostra servizi di un cliente
4. Elenco di tutti i clienti
5. Modifica nome cliente
6. Modifica/Elimina servizio
7. Salva ed esci

>>> """


clienti = verifica_file_txt()

while True:
    # stampa le opzioni (usa print() con righe separate)
    scelta = input(f"\nScegli un'opzione (1-7): \n{stringa_iniziale} ")
    if scelta == "1":
        print("\n\n------------- Nuovo cliente --------------------------\n\n")
        clienti = aggiungi_cliente(clienti)
        salva_clienti(clienti)   
        print("\n\n------------------------------------------------------\n\n")

    elif scelta == "2":
        print("\n\n------------- Aggiungi servizio a cliente esistente --\n\n")
        clienti = aggiungi_servizio(clienti)
        salva_clienti(clienti)
        print("\n\n------------------------------------------------------\n\n")

    elif scelta == "3":
        print("\n\n------------- Mostra servizi di un cliente -----------\n\n")
        mostra_servizi(clienti)
        print("\n\n------------------------------------------------------\n\n")

    elif scelta == "4":
        print("\n\n------------- Elenco di tutti i clienti --------------\n\n")

        elenco_clienti(clienti)
        print("\n\n------------------------------------------------------\n\n")
    elif scelta == "5":
        print("\n\n------------- Modifica nome cliente ------------------\n\n")

        clienti = modifica_nome_cliente(clienti)
        salva_clienti(clienti)
        print("\n\n------------------------------------------------------\n\n")

    elif scelta == "6":
        print("\n\n------------- Modifica/Elimina servizio --------------\n\n")
        clienti = gestisci_servizi_clienti(clienti)
        salva_clienti(clienti)
        print("\n\n------------------------------------------------------\n\n")

    elif scelta == "7":
        print("\n\n------------- Salva ed esci --------------------------\n\n")
        salva_clienti(clienti)   # salva un'ultima volta
        print("Uscita. Dati salvati.")
        break
    else:
        print("Opzione non valida")


#----------------------------------------------------------------









