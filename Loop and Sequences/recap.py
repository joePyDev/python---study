# liste : indicizzate e mutabili
lista = [1,2,3,"aaa","bbb",False,True,[1,2,3,4]]

# accesso alle liste :
    
X = lista[0]
print(X)

# accesso tramite indice negativo:
X = lista[-1]
print(X)

# creazione lista :
 
var_L = "non sono ancora una lista"
print(list(var_L),"adesso si")

# trovare la lunghezza della lista:
print(len(lista))

# le liste sono mutabili:
lista[0] = "AAAAAA"
print(lista)

# rimozioni elementi:
del lista[0]
print(lista)


# verificare la presenza di un elemento:
x = "aaaa" in lista
print(x)


# liste annidiate:
lista2 = ["aaa",[1,2,3,4],"bbb"]
print(lista2[1])


# estarzione valori lista:
lista = [1,2,3]
A,B,C = lista
print(A,B,C)


# raccogliere gli elementi rimanenti di una lista
# operatore asterisco *

name , *resto = lista # crea un ulteriore lista dentro resto
print(type(resto))

# slicing delle lista:
print(lista[:2])    

# metodi delle stringhe

lista.append(5) # [1, 2, 3, 5]

nuoviNum = [6,4,5]
lista.extend(nuoviNum) #♠ [1, 2, 3, 5, 6, 4, 5]

lista.insert(1, "object") # [1, 'object', 2, 3, 5, 6, 4, 5]

lista.remove(5)

lista.pop()

lista.clear()

print(lista)

lista = [1,5,3,4,6,8,2,1,4,5,6]
lista.sort()
print(lista)

new_lista = sorted(lista)
print(new_lista)

new_lista.reverse()
print(new_lista)

print(new_lista.index(5))




# tuple
unaTupla = ("aaa",1,False)

print(unaTupla[0])
print(unaTupla[-1])

mystring = "sonounastringa"
print(tuple(mystring))

print("aaa" in mystring)


A,B,C = unaTupla
print(A,B,C)


A , *F = unaTupla
print(F)

print(unaTupla[1:])



# Metodi comuni per le tuple
print(unaTupla.count("aaa"))

print(unaTupla.index("aaa"))

unatupladiinteri = (1,4,3,6,4,9,6,1,6,3,9)
print(sorted(unatupladiinteri))

print(sorted(unatupladiinteri,reverse=True))





# enumerate()  e zip()

lang = ["AAA","BBB","CCC","DDD"]
for indice , l  , in enumerate(lang):
    print(indice,l)


print(list(enumerate(lang)))




developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
ids = [1, 2, 3, 4]

for name, id in zip(developers, ids):
    print(f'Name: {name}')
    print(f'ID: {id}')




even_numbers = [num for num in range(21) if num % 2 == 0]
print(even_numbers)





numeri = [1,2,3,4,5,6]








