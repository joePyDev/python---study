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










































