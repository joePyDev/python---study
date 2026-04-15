# come contare ad esempio quante volte appare ogni lettera, creare un istogramma
word = "fruttivendolofruttivendolo"
d = dict()
for c in word:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1
print(d)        




# con get() possiamo ottimizzare l'istogramma:
word = "fruttivendolo"
d = dict()
for c in word:
    d[c] = d.get(c,0) + 1
print(d)   



