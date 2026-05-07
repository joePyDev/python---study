"""
 - i set non memorizzano valori duplicati.
 - mutabili e non ordinati
 - Possono contenere solo valori di tipi di dati 
   immutabili come numeri, stringhe e tuple.
 - supportano operazioni matematiche sugli insiemi,
   tra cui unione, intersezione, differenza e differenza simmetrica.
""" 


# dichiarazione set:
    
my_set = {1,2,3,4,5,6} #á graffe e valori separati da virgola


# per definire un set vuoto si usa set()

my_new_set = set()
print(type(my_new_set))

# se si scrive due parentesi graffe non si crea un set ma un dizionario
no_set = {} 
print(type(no_set)) # <class 'dict'>


# aggiungere un elemento a un set con .add()

my_set.add(6) 
print(my_set)

# Se si tenta di aggiungere un elemento già presente nell'insieme,
# ne verrà mantenuto solo uno.


# per rimuovere un elemento abbiamo 2 opzioni:

my_set.remove(1)
my_set.discard(2)

print(my_set)


# per rimuovere tutti gli elementi .clear()
my_set.clear()
print(my_set)

