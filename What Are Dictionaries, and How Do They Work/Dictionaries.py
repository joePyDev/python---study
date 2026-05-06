# strutture dati integrate che memorizzano collezioni di coppie chiave-valore.
# Con i dizionari Python, si utilizza una chiave per trovare il valore corrispondente.


"""

dizionario = {chiave2 : valore2 , chiave2 : valore2 }


"""

#  Le chiavi devono essere univoche nel dizionario e devono essere di un tipo di dati immutabile.
#  I valori, invece, possono essere ripetuti e possono essere di qualsiasi tipo di dati.

attributi = {"forza": 5 , "salute": 10 , "resistenza" : 10}



# costruttore dict()
nuovi_attributi = dict()


# accesso alla chiave:
print(attributi["forza"]) # ritorna il valore


# aggiornare un valore:
attributi["forza"] = 10

# se la chiave non presente viene aggiunta:
attributi["altezza"] = 30



# .get()metodo recupera il valore associato a una chiave.
# dictionary.get(key, default)

attributi.get("altezza",0) # se la chiave non esiste restituisce una lista vuota


# keys() ritorna tutte le chiavi
print(attributi.keys())# dict_keys(['forza', 'salute', 'resistenza', 'altezza'])


# values() ritorna tutti i vaori
print(attributi.values()) # dict_values([10, 10, 10, 30])


# item() ritorna tutte le coppie chiave valore
print(attributi.items())
"""
dict_keys(['forza', 'salute', 'resistenza', 'altezza'])
dict_values([10, 10, 10, 30])
dict_items([('forza', 10), ('salute', 10), ('resistenza', 10), ('altezza', 30)])
"""


# il metodo clear() rimuove tutte le coppie
"""
attributi.clear()
print(attributi) # {}
 
"""



A = attributi.pop("forza") # rimuove forza e ritorna il valore

print(A)
print(attributi)



# popitem() rimuove l'ultimo elemento inserito

attributi.popitem()
print(attributi)



# update() il dizionario con il contenuto di un altro
# chiavi uguali vengono sovrascritte

A = {"a":1,"b":1,}

B = {"c":1,"d":1,}

A.update(B) # {'a': 1, 'b': 1, 'c': 1, 'd': 1}


















