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

