"""
Come funziona: scorri l'array, un valore alla volta.
Per ogni valore, confrontalo con il valore successivo. 
Se il valore è maggiore del successivo, scambia i valori 
in modo che il valore più alto venga per ultimo. 
Ripeti il ​​processo per tante volte quanti sono i valori presenti nell'array.
"""



lista = [5,15,23,26,34,12,2,4,9,7]
print("lista originale",lista)            

lunghezza_lista = len(lista)
for i in range(lunghezza_lista ):
    for j in range(lunghezza_lista - i - 1):
        if lista[j] > lista[j+1]:
            lista[j],lista[j+1] = lista[j+1] , lista[j]
print("lista ordinata",lista)            
            





lista_2 = [5,15,23,26,34,12,2,4,9,7,45,32,65,18]
lunghezza_lista_2 = len(lista_2)

for i in range(lunghezza_lista_2 - 1):
    scambiato = False
    for j in range(lunghezza_lista_2 - i - 1):
        if lista_2[j] > lista_2[j+1]:
           lista_2[j] , lista_2[j+1] = lista_2[j+1] , lista_2[j]
           scambiato = True
    if not scambiato:
        break
print("lista 2 ordinata:", lista_2)



