"""
Scrivi un programma che restituisca una lista contenente
solo gli elementi comuni alle due liste (senza duplicati).
Assicurati che il programma funzioni correttamente con
liste di dimensioni diverse.

"""

lista1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

set1 = set(lista1)
set2 = set(lista2)

# !!! lista_finale = list(set1 & set2)

lista_finale = []

if set1 and set2:
    for i in set1:
        if i in set2:
            lista_finale.append(i)
    if len(lista_finale) > 0:
        print(f"I numeri comuni alle liste sono: {lista_finale}")
    else:
        print("non ci sono numeri in comune")
else:
    print("non sono ammesse liste vuote")
