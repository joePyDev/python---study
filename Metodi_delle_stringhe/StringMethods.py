"""

Gruppo 1: Trasformazione Case
string.capitalize()

string.casefold()

string.lower()

string.swapcase()

string.title()

string.upper()


Gruppo 2: Allineamento e Formattazione
string.center(length, character)

string.expandtabs(tabsize)

string.format(value1, value2, ...)

string.format_map(mapping)

string.ljust(length, character)

string.rjust(length, character)

string.zfill(length)


Gruppo 3: Ricerca e Conteggio
string.count(value, start, end)

string.endswith(value, start, end)

string.find(value, start, end)

string.index(value, start, end)

string.rfind(value, start, end)

string.rindex(value, start, end)

string.startswith(value, start, end)


Gruppo 4: Controlli (Boolean)
string.isalnum()

string.isalpha()

string.isdecimal()

string.isdigit()

string.isidentifier()

string.islower()

string.isnumeric()

string.isprintable()

string.isspace()

string.istitle()

string.isupper()


Gruppo 5: Modifica e Suddivisione
string.encode(encoding, errors)

string.join(iterable)

string.lstrip(characters)

string.partition(value)

string.replace(oldvalue, newvalue, count)

string.rpartition(value)

string.rsplit(separator, maxsplit)

string.rstrip(characters)

string.split(separator, maxsplit)

string.splitlines(keepends)

string.strip(characters)


Gruppo 6: Traduzione e Mappatura
string.maketrans(x, y, z)

string.translate(table)


"""



# help(str.metodo)


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



# isidentifier()#
#Una stringa è considerata un identificatore valido se contiene 
#solo lettere alfanumeriche (a, b, c) e (0-9) o trattini bassi (_). 
txt = "Demo"
X = txt.isidentifier()
print(X)



# islower()
# restituisce True se tutti i caratteri sono minuscoli
txt = "Ciao mondo"
X = txt.islower()
print(X)


# isnumeric()
# restituisce True se tutti i caratteri sono numerici (0-9), altrimenti False.
txt = "12345"
X = txt.isnumeric()
print(X)



# isprintable()
# restituisce True se tutti i caratteri sono stampabili, altrimenti False.
txt = "Hello , Are You #1"
X = txt.isprintable()
print(X)


# isspace()
#  restituisce True se tutti i caratteri di una stringa sono spazi bianchi, altrimenti False.
txt = "    "
X = txt.isspace()
print(X)


# istitle()
#  restituisce True se tutte le parole di un testo iniziano con
# una lettera maiuscola E il resto della parola è composto da lettere minuscole,
txt = "Hello,And Welcome To My World"
X = txt.istitle()
print(X)


# isupper()
# restituisce True se tutti i caratteri sono maiuscoli, altrimenti False.
txt = "HALLO WELCOME"
X = txt.isupper()
print(X)



# join()
# prende tutti gli elementi di un iterabile e li unisce in un'unica stringa.
my_tuple = ("jon", "mary","jane")
X = " . ".join(my_tuple)
print(X) # jon . mary . jane



# ljust()
# allineerà la stringa a sinistra, utilizzando un carattere specificato
# (lo spazio è il valore predefinito) come carattere di riempimento.
# string.ljust(length, character)
txt = "frutto"
X = txt.ljust(20)
print(X,"20 caratteri di distanza")



# lower()
# restituisce una stringa in cui tutti i caratteri sono minuscoli.
txt = "HELLO my Friends"
X = txt.lower()
print((X))


# lstrip()
# rimuove tutti i caratteri iniziali (lo spazio è il carattere iniziale predefinito da rimuovere).
txt = "    hello my Friends"
X = txt.lstrip()
print(X)   


# maketrans()
# metodo restituisce una tabella di mappatura che può essere
# utilizzata con il metodo per sostituire i caratteri specificati.
txt = "Hallo sam"
X = txt.maketrans("S","P","l")
print(X)

# translate()
# restituisce una stringa in cui alcuni caratteri specificati
# vengono sostituiti con il carattere descritto in un dizionario
# o in una tabella di corrispondenza.

print(txt.translate(X)) # gli abbiamo passato i valori creati da maketrans

#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))


# partition()
# cerca una stringa specificata e la suddivide in una tupla contenente tre elementi.
txt = "potrei mangiare una mela ogni giorno"
X = txt.partition("mela")
print(X)


# replace()
# sostituisce una frase specificata con un'altra frase specificata.

txt = "mi piace andare in bici"
X = txt.replace("bici","moto")
print(X)


# rfind()
# individua l'ultima occorrenza del valore specificato.
txt = "mi casa , su casa"
X = txt.rfind(("casa"))
print(X)

txt = "mi casa , su casa"
X = txt.rfind(("pippo"))
print(X)


#rindex()
#  individua l'ultima occorrenza del valore specificato.
txt = "mi casa , su casa"
X = txt.rindex(("casa"))
print(X)

txt = "mi casa , su casa"
X = txt.rfind(("pippo"))
print(X)


# rjust()
# il metodo allineerà a destra la stringa, utilizzando un carattere 
# specificato (lo spazio è il valore predefinito) come carattere di riempimento.
txt = "mela"
X = txt.rjust(15,"*")
print(X)



# rpartition()
# metodo cerca l'ultima occorrenza di una stringa specificata e
# la suddivide in una tupla contenente tre elementi.
txt = "potrei mangiare frutta ogni giorno, la frutta mi piace molto"
X = txt.rpartition("frutta")
print(X)




# rsplit()
# suddivide una stringa in una lista, partendo da destra.
txt = "apple, banana, cherry"
X = txt.rsplit(", ")# esegui il taglio in corrispondenza di ", "
print(X)



# rstrip()
# metodo rimuove tutti i caratteri finali (i caratteri alla fine di una stringa);
# lo spazio è il carattere finale predefinito da rimuovere.
txt = "banana        .       "
X = txt.rstrip()
print(X)


# split()
# suddivide una stringa in una lista.
txt = "welcome to the jungle"
X = txt.split()
print(X)


# splitlines()
# metodo suddivide una stringa in una lista. La suddivisione avviene
# in corrispondenza delle interruzioni di riga \n
txt = "grazie per la musica \nhello word"
X = txt.splitlines()
print(X)



# startswith()
# metodo restituisce True se la stringa inizia con il valore specificato, altrimenti False.
txt = "Hello word"
X = txt.startswith("Hello")
print(X)


# strip()
# rimuove tutti gli spazi bianchi iniziali e finali.
txt = "    banana    "
X = txt.strip()
print(X)




# swapcase()
# restituisce una stringa in cui tutte le lettere maiuscole sono minuscole e viceversa.
txt = "BuonGiorno mondo SOno MolTO ImPeGnAtO"
X = txt.swapcase()
print(X)



# title()
# restituisce una stringa in cui il primo carattere di ogni parola è maiuscolo.
txt = "sono andato al cinema"
X = txt.title()
print(X)



# upper()
# restituisce una stringa in cui tutti i caratteri sono maiuscoli.
txt = "sono una stringa minuscola"
X = txt.upper()
print(X)



# zfill()
# aggiunge degli zeri (0) all'inizio della stringa, fino a raggiungere la lunghezza specificata.
txt = "50"
X = txt.zfill(5)
print(X)





















