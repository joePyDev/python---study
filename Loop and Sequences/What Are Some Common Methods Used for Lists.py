
# metodo append() , aggiunge un elemento alla fine di una lista
num = [1,2,3,4,5]
num.append(6)
print(num)

altri_num = [6,7,8,9]
num.append(altri_num)
print(num)


# inserire singoli elementi della lista in un altra, extend():
num.extend(altri_num)
print(num)


# Il insert()metodo inserisce il valore specificato nella posizione specificata.
fruit = ["mele","pere","banane"]
fruit.insert(0,"lampone")
print(fruit)


# Il remove()metodo rimuove la prima occorrenza dell'elemento con il valore specificato.
valori = [30,50,60,80,90,False]
valori.remove(False)
print(valori)


# Il pop()metodo rimuove l'elemento nella posizione indice specificato.
alfabeto = ["a","b","c","d"]
alfabeto.pop(1)
print(alfabeto)


A = [1,2,3,4,5]
A.pop() # Se non si specifica , l'ultimo elemento viene rimosso.
print(A)


# Il metodo clear() rimuove tutti gli elementi da una lista.

my_list = [ 1,2,3,4,5,6]
my_list.clear()
print(my_list)


# Il metodo sort() ordina la lista in ordine crescente
numeri = [2,54,6,44,23,45,86,23,9,87,54]
numeri.sort()
print(numeri)


# sorted() restituisce un elenco ordinato dell'oggetto iterabile specificato.

numbers = [19,2,35,1,67,41]
sorted_numbers = sorted(numbers)
print(sorted_numbers)


# Il reverse() inverte l'ordine di ordinamento degli elementi.
numeri = [1,2,3,4,5,6]
numeri.reverse()
print(numeri)


# Il index() restituisce la posizione alla prima occorrenza del valore specificato.

frutta = ["mela","pera","limone","uva"]
indice = frutta.index("pera")
print(indice)












