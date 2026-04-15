
# dir() 
# help()


r"""


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

"""


# ------------------ 

# creazione dizionario vuoto con dict()
eng2sp = dict()

# le parentesi graffe {} rappresentano un dizionario vuoto
eng2sp = {}
 
# aggiunta elementi:
eng2sp["one"] = 1
#print(eng2sp["one"])    


# funzione len() restituisce il numero di coppie
eng2sp["two"] = 2
print(len(eng2sp))


# operatore in verifica la presenza della chiave
print("one" in eng2sp)


""" metodo value() restituisce i valori come una lista e poi è 
posibile verificare la presenza di un valore con  operatore in :
"""
valori_dict = list(eng2sp.values())
if 2 in valori_dict:
    print("i valori sono",valori_dict)
    


# dizionari come insieme di contatori

# come contare ad esempio quante volte appare ogni lettera
word = "fruttivendolofruttivendolo"
d = dict()
for c in word:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1
print(d)        



# il metodo get() riceve chiave e un valore predefinito.
# Se la chiave è presente nel dizionario, get restituisce il valore corrispondente,
# altrimenti restituisce il valore predefinito.

counts = {"pippo": 1, "anna": 2 , "luca":3}

print("Il valore trovato da get è:",counts.get("luca",0))


# con get() possiamo ottimizzare l'istogramma:
word = "fruttivendolo"
d = dict()
for c in word:
    d[c] = d.get(c,0) + 1
print(d)    



# --- 

ccc = dict()
ccc["csev"] = 1
ccc["cwen"] = 1

print(ccc)




names = ["Anna", "Bob", "Anna", "Cara", "Bob", "Anna"]

counts = {}

for person in names:
    if person not in counts:
        counts[person] = 1
    else:
        counts[person] = counts[person] + 1

print(counts)



scores = {"alice": 5, "bob": 12, "carol": 7}

for person, points in scores.items():
    print(person, points)




fname = r"C:\Users\gioel\OneDrive\Documenti\Programmazione\Python_course2\esercizi\romeo.txt"
#fname = input("Inserisci il nome del file")
try:
    fhand = open(fname)
except:
    print("il file non può essere aperto")
    exit()

conteggio = dict()

for line in fhand:
    words = line.split()
    for word in words:
        if word not in conteggio:
            conteggio[word] = 1
        else:
            conteggio[word] += 1
            
print("Istogramma:" , conteggio)            
            
            
# --------------------

    
dic = {"pippo": 15 , "salvo": 36 , "luca": 32}
for chiave in dic:
    print(chiave,dic[chiave])



dizionario = {"aa":1 ,"bb":2 ,"cc":3 ,"dd":4 ,"ee":5 ,"ff":6 ,"gg":7 ,"hh":8 ,"ii":9 }

for parole_ciave in dizionario:
    print(parole_ciave , dizionario[parole_ciave],"\n")




counts = { "chuck" : 1 , "annie" : 42, "jan": 100}

for key in counts:
    if counts[key] >= 10:
        print(key,counts[key])




counts = { "chuck" : 1 , "annie" : 42, "jan": 100}

lst = list(counts.keys())
print(lst)
lst.sort()
print(lst)
for key in lst:
    print(key,counts[key])







