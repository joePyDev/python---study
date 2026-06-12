
# strutture chiave - valore
valore1 = 1
valore2 = 2
my_dict = {"chiave1":valore1 , "chiave2":valore2}

# costruttore dizionario:
new_dict = dict()

# oppure:
pizza = dict([('name', 'Margherita Pizza'), ('price', 8.9),
              ('calories_per_slice', 250), ('toppings', ['mozzarella', 'basil'])])


# Acesso a valore tramite chiave:
pizza["name"] # 'Margherita Pizza'


#Metodo get() , recupera valore chiave senno ritorna valore predefinito:
valore_get = pizza.get("ciao","no key in dict!")


# metodi keys() e values() , restituiscono un oggetto vista con chiavi e valori:
chiavi =  pizza.keys()
valori =  pizza.values()


# items() restituisce entrambi chiave/valore
oggeto_items = pizza.items()


# clear() rimuove tutte le coppi chiave valore
clone_pizza = dict([('name', 'Margherita Pizza'), ('price', 8.9),
              ('calories_per_slice', 250), ('toppings', ['mozzarella', 'basil'])])
clone_pizza.clear()


# pop() elimina la coppia chiave valore e ritorna il valore
clone_pizza = dict([('name', 'Margherita Pizza'), ('price', 8.9),
              ('calories_per_slice', 250), ('toppings', ['mozzarella', 'basil'])])
pizza_popped = clone_pizza.pop("name")


# popitem() rimuove l'ultimo elemento inserito
clone_pizza.popitem()


#  aggiorna le coppie chiave-valore con le coppie
#  chiave-valore di un altro dizionario
#  Se hanno chiavi in ​​comune, i loro valori vengono sovrascritti

clone_pizza.update({ 'price': 15, 'total_time': 25 })



# scorrere un dizionario 

dizionario_frutta = {"mele" : 50 ,
                     "pere": 20 ,
                     "carote": 10 ,
                     "mele" : 50 }

for quantita_frutta in  dizionario_frutta.values():
    None

for nome_frutta in dizionario_frutta.keys():
    None
    
for nome_frutta , quantita_frutta in dizionario_frutta.items():
   None
    #print(nome_frutta , quantita_frutta)



# enumerare con un ciclo
# possiamo specificare l'indice di partenza
for nome_frutta , quantita_frutta in enumerate(dizionario_frutta.items(),1): 
    None
   # print(nome_frutta , quantita_frutta)
"""
1 ('mele', 50)
2 ('pere', 20)
3 ('carote', 10)
"""



# SET
# No duplicati , mutabili , non ordinati
 
my_set = {1,2,3,4,5,6}


# Metodi dei SET:
    
# add() aggiunge elemento
my_set.add(30)


# remove() o discard() per rimuovere un elemento
my_set.remove(1)
my_set.discard(2)

# clear() rimuove tutti gli elementi
 


# Operazioni Matematiche
# issubset() , issuperset() verificano se un set è un sottoinsieme o soprainsieme di un set

my_set2 = {1,2,3,4,5,6}
my_set3 = {2,3,4,5,6}

verifica_sottoinsieme = my_set2.issubset(my_set3)
verifica_sottoinsieme = my_set2.issuperset(my_set3)


# isdisjoint() verifica se ci sono elementi in comune
verifica_disgiunti = my_set2.isdisjoint(my_set3)


# operatore di unione | ritorna un un nuovo insieme con tutti gli elementi
unione_set =  my_set2 | my_set3  

# operatore di intersezione & , nupvo insieme di elementi in comune
intersezione_set = my_set2 & my_set3

# operatore differenza - nuovo insieme con elementi che non sono presenti nel set
differenza_set = my_set2 - my_set3


# differenza simmetrica ^ restituisce un nuovo insieme con gli elementi che
# sono presenti nel primo o nel secondo insieme, ma non in entrambi.
differenza_simmetrica_set = my_set2 ^ my_set3


# L'operatore "in" verifica se un elemento appartiene ad un insieme
verifica_presenza_elemento = 5 in my_set2

