# le tuple sono immutabili
"""
I valori della tupla possono essere di qualsiasi tipo e indicizzati 
tramite numeri interi.
"""

T = ("a","b","c")

# tupla con singolo elemento:
t = ("a",)
type((t)) # tuple


# in assenza della virgola python considera ("a")  un espressione con una stringa tra parentesi
t1 = ("a")
type((t1)) # str


# Utilizzando come argomento di tuple una sequenza (stringa, elenco o tupla)
# ritorna una tupla
mylist = [1,2,3,4,5,6]
mytuple = (1,2,3,4,5,(1,2,3))

t2 = tuple("sonounatupla")
t3 = tuple(mylist)
t4 = tuple(mytuple)
print(t2) # ('s', 'o', 'n', 'o', 'u', 'n', 'a', 't', 'u', 'p', 'l', 'a')



# L amaggior parte degli operatori delle liste funziona sulle tuple

t6 = ("a","s","f","4")
print(t6[3]) # posizione di un elemento

print(t6[:2]) # intervallo elementi


# non è posibile modificare elementi di una tupla
"""
t[0] = "A"  TypeError: object doesnt support item assignment

"""


# Pur non essendo possibile modificare gli elementi di una tupla, puoi sostituirla con un’altra:

my_tuple = ("bbbb","ccccc","dddd")

my_tuple = ("A",) + my_tuple[1:] 

print(my_tuple)




# Confronto tra tuple

(1,2,3,4) > (1,2,3,0,1,5) # true
(1,2,20000000) < (1,3,4) # true





# Modello DSU (decorate - sort - undecorate)

# elenco di parole da ordinare in base alla glunghezza

# decorate
txt = "sono una sequenza da ordinare in base alla lunghezza"
parole = txt.split()
t = list()
for parola in parole:
    t.append((len(parola),parola))
# sort
t.sort(reverse = True)
# undecorate
res = list()
for lunghezza , parola in t:
    res.append(parola)

print(res)





# assegnazione tupla unpacking:
m = ["have","fun"]

x,y = m # Assegnazione di tupla (senza parentesi)
(x,y) = m # Assegnazione con parentesi esplicite
print(x,y)


# assegnazione esplicita 
x = m[0]
y = m[1]



# scambio di valori_
print(x,y)

x , y = y , x

print(x,y)


#Il numero di variabili a sinistra e il numero di valori a destra devono essere uguali:
# a, b = 1, 2, 3  ValueError: too many values to unpack



#  il lato destro può contenere un qualsiasi tipo di sequenza (stringa,
# elenco o tupla).

indirizzo = "monty@python.org"
uname,domain = indirizzo.split("@") 



# dizionari e tuple
d = {"a":10,"b":1,"c":22}
t = list(d.items())
print(t)


# ordinare l'elenco di tuple.
d = {"ff":33,"a":10,"b":1,"c":22 }
t = list(d.items())
print(t)
t.sort()
print(t)



# Assegnazione multipla con dizionari

for key , val in list(d.items()):
    print(val,key)
#  l’ordine è basato sul valore dell’hash (cioè, nessun ordine particolare).



# ordinare in base al valore:
d = {"ff":33,"a":10,"b":1,"c":22 }
l = list()
for key , val in d.items():
    l.append((val,key))
l.sort(reverse = True)
print(l)






# Le parole più comuni
import string

fhand = open (r"C:\Users\gioel\OneDrive\Documenti\Programmazione\Python_course2\esercizi\romeo.txt")
counts = dict()
for line in fhand:
    line = line.translate(str.maketrans("","",string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

lst = list()
for key , val in list(counts.items()):
    lst.append((val , key))
lst.sort(reverse = True) 
for key , val in lst[:10]:
    print(key , val)   




# tuple come chiavi nei dizionari
# Chiave semplice: Stringa, numero.
# Chiave composta: Tupla.
# Mai come chiave: Liste, Dizionari, Set (perché sono mutabili).


last = 10
first = 0
number = "1234562254"
directory = dict()
directory[last , first] = number # L’espressione tra parentesi quadre è una tupla.
print(directory) # {(10, 0): '1234562254'}

for last , first in directory:
    print(first , last,directory[last,first])






















