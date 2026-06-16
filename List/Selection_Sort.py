"""
Scorri l'array per trovare il valore più basso. 
Sposta il valore più basso all'inizio della parte non ordinata dell'array. 
Scorri nuovamente l'array tante volte quanti sono i valori presenti nell'array.
"""


lista = [1,5,3,4,6,58,4,5,21,23,54,78,56]
lunghezza_lista = len(lista)

for i in range(lunghezza_lista - 1):
    print(">>>>> ciclo esterno = ",i)
    min_indice = i
    for j in range(i + 1 , lunghezza_lista):
        print("ciclo interno = ",j)
        if lista[j] < lista[min_indice]:
            print(">debug<",lista[j],lista[min_indice])
            min_indice = j
            print(">>>>debug min indice",min_indice)
    min_value = lista.pop(min_indice)
    print("debug  min value",min_value)
    lista.insert(i,min_value)
    print("debug  lista", lista)

print(lista)    




lista2 =  [1,3,4,6,58,5,21,23]

lunghezza2 = len(lista2)
for i in range(lunghezza2):
    min_indice = i
    for j in range(i +1 , lunghezza2):
        if lista2[j] < lista2[min_indice]:
            min_indice = j
    lista2[i],lista2[min_indice] = lista2[min_indice] , lista2[i]
    
print(lista2)    
    
    
    
    
    
    
    
    
    
    
