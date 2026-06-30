"""
Scrivi un programma che restituisca una lista
contenente solo gli elementi comuni alle due liste (senza duplicati).
 Assicurati che il programma funzioni con due liste di dimensioni diverse.
Scrivi il programma in una sola riga di codice Python
 utilizzando almeno una list comprehension

"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = list(set([x for x in a if x in b]))
