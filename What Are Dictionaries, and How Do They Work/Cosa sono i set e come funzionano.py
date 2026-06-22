"""
- i set non memorizzano valori duplicati.
- mutabili e non ordinati
- Possono contenere solo valori di tipi di dati
  immutabili come numeri, stringhe e tuple.
- supportano operazioni matematiche sugli insiemi,
  tra cui unione, intersezione, differenza e differenza simmetrica.
"""

# dichiarazione set:

my_set = {1, 2, 3, 4, 5, 6}  # á graffe e valori separati da virgola


# per definire un set vuoto si usa set()

my_new_set = set()
print(type(my_new_set))

# se si scrive due parentesi graffe non si crea un set ma un dizionario
no_set = {}
print(type(no_set))  # <class 'dict'>


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


"""
I metodi .issubset()e .issuperset()verificano rispettivamente
se un insieme è un sottoinsieme o un sovrainsieme di un altro insieme.
"""

set1 = {1, 2, 3, 4, 5}
set2 = {2, 3, 4, 6}

print(set2.issubset(set1))  # False
print(set1.issuperset(set2))  # False


# .isdisjoint() verifica se NON ci sono elementi in comune
print(set1.isdisjoint(set2))


# operatore unione |    ritorna un insieme di tutti gli elementi di entrambi gli insiemi
set3 = set1 | set2
print(set3)


# operatore & ritorna un nuovo insieme con solo gli elementi in comune
set3 = set1 & set2
print(set3)


# operatore - sottrazione ritorna elementi del primo nsieme non presenti negli altri

set3 = set1 - set2
print(set3)


# operatore differenza simmetrica  ^ ritorna
# elementi che appartengono al primo o al secondo insieme, ma non a entrambi.

set3 = set1 ^ set2
print(set3)


"""
 operatore di assegnazione composta 
|= &= -= ^=
"""


# operatore -= calcola la differenza tra 2 set e aggiorna il primo con il risultato
set1 -= set2
print(set1)


# con in possiamo verificare la presenza di un valore

print(5 in set1)  # True
