"""
[capitalize, casefold, center, count, encode,
endswith, expandtabs, find, format, format_map,
index, isalnum, isalpha, isdecimal, isdigit,
isidentifier, islower, isnumeric, isprintable,
isspace, istitle, isupper, join, ljust, lower,
lstrip, maketrans, partition, replace, rfind,
rindex, rjust, rpartition, rsplit, rstrip,
split, splitlines, startswith, strip, swapcase,
title, translate, upper, zfill]
"""

# help(metodo)


# capitalize() Scrive in ​​maiuscolo la prima lettera di questa frase
txt = "hello word"
X = txt.capitalize()
print(X)


# casefold() converte la stringa in minuscolo
txt = "HELLO word"
X = txt.casefold()
print(X)


# center() scrive la parola indicata al centro con lo spazio indicato
txt = "banana"
X = txt.center(20)
print(X)


# count()
# Restituisce il numero di volte in cui il valore  compare nella stringa:
txt = "amo la frutta , in particolare le mele"
X = txt.count("frutta")
print(X)    


# encode89
# Codifica la stringa in UTF-8
txt = "il mio nome è Gio"
X = txt.encode()
print(X)


# endswith89
# Verifica se la stringa termina con il simbolo/carattere indicato: 
# string.endswith(value, start, end)
txt = "hello, welcome to my word"
X = txt.endswith("word")
print(X)


# expandtabs()
# Il metodo expandtabs() in Python serve a sostituire i 
#caratteri di tabulazione (\t) all'interno di una stringa con 
#degli spazi bianchi.
txt = "H\te\tl\to"
X = txt.expandtabs(2)
print(X)


# find()
# Restituisce l'indice (la posizione) della prima occorrenza trovata.
txt = "benvenuti nel mio mondo"
X = txt.find("benvenuti")
print(X)


# format()
#Permette di inserire valori (variabili, numeri, testi) all'interno di
# una stringa "modello" usando le parentesi graffe {} come segnaposto.
testo = "Ciao, mi chiamo {} e ho {} anni."
print(testo.format("Alice", 25))
# segnaposto indicizzato al positional argument
txt = "il mio nome è {0} ho anni {1} e lavoro in {1}"
X = txt.format("pippo", 25)
print(X)


# format_map()
# accetta valori da un dizionario
dati = {"nome":"pippo","anni":25,"lavoro":"Developer"}
txt = "Il mio nome è {nome}, ho {anni} e faccio il {lavoro}"
txt = txt.format_map(dati)
print(txt)


# index()
# Restituisce la posizione (indice) della prima occorrenza trovata.
# string.index(value, start, end)
frase = "il codice è poesia"
pos = frase.index("codice")
print(pos)


# isalnum()
# verificare se una stringa è composta esclusivamente da caratteri alfanumerici.ù

print("pippo53".isalnum())
print("pippo".isalnum())
print("pippo 25".isalnum()) # false
print("pippoç°ç°°".isalnum()) # false


# isalpha()
# restituisce True solo se la stringa è composta esclusivamente da lettere.
# Solo lettere
print("Pippo".isalpha())      # True
print("nì".isalpha())         # True (le accentate sono lettere)

# Con numeri
print("Pippo25".isalpha())    # False (il '25' lo fa fallire)


# esempio
nome =("Inserisci il tuo nome: ") # input utente

if nome.isalpha():
    print("Nome accettato.")
else:
    print("Errore: il nome non può contenere numeri o spazi.")



# isdecimal()
# controlla se la stringa è composta interamente da caratteri decimali(0-9)
print("123".isdecimal())
print("10.5".isdecimal())   # False (il punto non è un decimale)


# isdigit()
# Verifica se tutti i caratteri del testo sono cifre:
txt = "50800"

x = txt.isdigit()

print(x)























