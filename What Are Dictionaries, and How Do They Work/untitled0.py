
"""
possibile iterare su un dizionario se è necessario accedere
ed elaborare le sue coppie chiave-valore.
"""

prodotti = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}


# values() , keys() , items()

for valore in prodotti.values():
    print(valore)

for chiave in prodotti.keys():
    print(chiave)    
    
for chiave , valore in prodotti.items():
    print(chiave,valore)