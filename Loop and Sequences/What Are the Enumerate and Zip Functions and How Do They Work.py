

# Enumerate and Zip Functions

lang = ["ita","sp","fr","td","ing"]

for lan in lang:
    print(lan)



# se volessi anche un indice:
index = 0
for lan in lang:
    print(f" index{index} amd language {lan}")
    index += 1    
    
    
    
#  La enumerate()funzione tiene traccia dell'indice
#  di un iterabile e restituisce un oggetto enumerato.

myList =  list(enumerate((lang)))

for index , lan in enumerate(lang):
    print(f"index {index} language {lan}")
    
    
# la funzione enumerate accetta anche start,ovvero il valore di pertenza del indice:

for index , lan in enumerate(lang,1):
    print(f"index {index} language {lan}")
        
    
# iterare su più iterabili in parallelo
    
parole = ["aaa","bbb","ccc","ddd","eee"]

ids = [1,2,3,4,5]

mylist2list = list(zip(parole,ids))

print(mylist2list)



developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
ids = [1, 2, 3, 4]

for name, id in zip(developers, ids):
    print(f'Name: {name}')
    print(f'ID: {id}')