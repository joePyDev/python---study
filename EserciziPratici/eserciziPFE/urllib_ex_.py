"""
Esercizio 1 – Scarica e stampa una pagina semplice
Obiettivo: Scaricare il contenuto di una pagina web
 (es. http://data.pr4e.org/romeo.txt)
e stamparlo a schermo riga per riga
(senza modifiche, mantenendo spazi e newline).

Suggerimenti:

Usa urllib.request.urlopen().

Leggi riga per riga con un ciclo for.

Decodifica ogni riga da bytes a str con .decode().

Output atteso: Il testo esatto del file, incluso il carattere di newline
 alla fine di ogni riga.


import urllib.request , urllib.parse , urllib.error
fhand = urllib.request.urlopen("https://www.w3schools.com/htmL//html_basic.asp")
for line in fhand:
    print(line.decode().strip())

"""

"""
Esercizio 2 – Conta le parole in una pagina web
Obiettivo: Scaricare il testo da un URL, contare il numero totale di parole 
(separate da spazi, newline, punteggiatura) e stamparlo.

Suggerimenti:

Dopo aver ottenuto l’intero contenuto come stringa, usa .split().

Attenzione: potresti trovare tag HTML se l’URL punta a una pagina web 
(es. http://example.com). Per questo esercizio, usa un URL che punta 
a un file di solo testo (es. http://data.pr4e.org/romeo.txt).

Variante: Conta quante volte compare una certa parola (es. "the").
"""


import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")

counts = dict()
for line in fhand:
    print("Debug >>>>", line)
    parole = line.decode().split()
    for parola in parole:
        counts[parola] = counts.get(parola, 0) + 1

print(counts)
print(parole)
