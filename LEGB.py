"""
La regola LEGB: la strategia di ricerca delle variabili di Python
Quando si utilizza una variabile nel codice, Python avvia una ricerca sistematica per trovarne il valore. L'ordine di ricerca è descritto dalla regola LEGB:

Locale (L): Python verifica innanzitutto se la variabile esiste all'interno della funzione o del blocco di codice corrente.

Funzione contenitore (E): Se non trovata localmente, cerca nelle funzioni Enclosing (se si utilizzano funzioni annidate, come le matrioske).

Globale (G): Successivamente, cerca nell'ambito globale, ovvero nelle variabili definite al livello superiore del modulo.

Integrato (B): Infine, controlla lo spazio dei nomi integrato di Python per funzioni e oggetti predefiniti come print, list, ecc.
"""




# ambito locale:
    
def saluta_locale():
    # 'messaggio' è una variabile LOCALE: esiste solo dentro questa funzione
    messaggio = "Ciao dal ambito locale"
    print("Dentro la funzione:")
    print(messaggio)
    
saluta_locale()    
    

# Proviamo ad usare 'messaggio' fuori dalla funzione
try:
    print("\nFuori dalla funzione saluta:")
    print(messaggio)   # -> ERRORE: NameError: name 'messaggio' is not defined
except NameError as e:
    print(f"ERRORE previsto: {e}")
    
    






# ESEMPIO 2 - Ambito Globale (G)

# Questa è una variabile GLOBALE: definita fuori da qualsiasi funzione
nome = "Alice"


def saluta_globale():
    print("dentro saluta_globale")
    print("ciao",nome)     # Python non trova 'nome' nel locale,
                           # passa al Enclosing (assente),
                           # poi al globale: lo trova qui.

def cambia_nome():
    # Se proviamo a MODIFICARE la variabile globale,
    # Python, per default, crea una nuova variabile LOCALE
    # che "oscura" quella globale.
    nome = "Bob"           # Questa è LOCALE, non tocca la globale!
    print("Dentro cambia_nome:")
    print("nome locale:", nome)

def cambia_nome_globale():
    # Per modificare DAVVERO la globale, dobbiamo dichiararla 'global'
    global nome
    nome = "Charlie"
    print("Dentro cambia_nome_globale:")
    print("nome (globale):", nome)

# --- Esecuzione dei test ---

print("--- Inizio programma ---")
print("Inizialmente globale:", nome)

print("\n1. Chiamo saluta():")
saluta_globale()

print("\n2. Chiamo cambia_nome() (senza global):")
cambia_nome()
print("Dopo cambia_nome(), globale nome =", nome)   # Resta 'Alice'

print("\n3. Chiamo cambia_nome_globale() (con global):")
cambia_nome_globale()
print("Dopo cambia_nome_globale(), globale nome =", nome)   # Ora 'Charlie'

print("fine globale il nome è modificato in",nome,"\n")





# ESEMPIO 3 - Funzione contenitore (E), funzioni annidate

def esterna():
    # 'saluto' è definita nella funzione esterna.
    # Per la funzione interna, è una variabile di "Funzione contenitore" (E).
    saluto = "Ciao dall'esterna!"

    def interna():
        # Leggiamo 'saluto': Python cerca in L (non c'è), poi in E (la trova!)
        print("Dentro interna, leggo saluto:", saluto)

    def interna_modifica_sbagliata():
        # Tentativo di MODIFICARE 'saluto' SENZA 'nonlocal'.
        # Python crea una NUOVA variabile LOCALE che oscura quella esterna.
        saluto = "Ciao modificato!"  # Questa è LOCALE, non tocca l'esterna!
        print("Dentro interna_modifica_sbagliata:", saluto)

    def interna_modifica_corretta():
        # Per modificare DAVVERO la variabile della funzione esterna,
        # dobbiamo dichiararla 'nonlocal'.
        nonlocal saluto
        saluto = "Ciao modificato con nonlocal!"
        print("Dentro interna_modifica_corretta:", saluto)

    print("\n--- Dentro esterna, prima delle chiamate ---")
    print("saluto iniziale:", saluto)

    print("\n1. Chiamo interna():")
    interna()
    print("saluto dopo interna():", saluto)  # Resta invariato

    print("\n2. Chiamo interna_modifica_sbagliata():")
    interna_modifica_sbagliata()
    print("saluto dopo interna_modifica_sbagliata():", saluto)  # Invariato

    print("\n3. Chiamo interna_modifica_corretta():")
    interna_modifica_corretta()
    print("saluto dopo interna_modifica_corretta():", saluto)  # Modificato!

# Esecuzione
print("=== INIZIO PROGRAMMA ===")
esterna()
print("=== FINE ===")




# ESEMPIO 4 - Livello Integrato (B)

# 'print' è un nome integrato: Python lo trova nel livello B.
print("Ciao dal livello Integrato!")

# Anche 'len' è integrato.
numeri = [1, 2, 3]
print("La lista ha", len(numeri), "elementi.")

# Possiamo OSCURARE un nome integrato definendone uno nostro
# nei livelli precedenti. QUI È UN ERRORE DA EVITARE!
# Esempio: definiamo una variabile locale 'print' che nasconde la funzione built-in.
def funzione_che_oscura_print():
    # 'print' ora è una stringa LOCALE, non più la funzione integrata.
    print = "Ciao"   #  OSCURA il built-in 'print' a livello Locale
    # print("Questo darebbe errore!")   # perché 'print' ora è una stringa, non chiamabile.
    print("Qui non stampo, perché print è una stringa.")  # Questo riga darebbe errore

# Per evitare l'errore, NON eseguiamo la funzione. Ti spiego solo il concetto.

# È possibile anche oscurare un integrato a livello Globale (DA NON FARE):
# len = 42   #  Ora 'len' non è più la funzione, ma un intero. Meglio evitare.

# Per vedere TUTTI i nomi integrati:
print("\nNomi integrati disponibili (primi 20):")
import builtins
nomi_integrati = dir(builtins)
print(nomi_integrati[:20])  # Mostriamo i primi 20 nomi per dare un'idea










