# Analizziamo nel dettaglio i componenti chiave di una classe:
    
    
    
    
# Definizione della classe:    
    
"""
Per definire una classe si usa  la parola "class" seguita dal nome della classe

class Automobili:

Pensate alla definizione della classe come 
allo stampo per la creazione degli oggetti. 
Essa delinea la struttura e le funzionalità 
che ogni oggetto Automobile avrà.

"""


# Attributi(dati):
"""
Gli attributi sono le variabili che memorizzano 
lo stato o le caratteristiche di un oggetto. 
"""

class Automobile_esempio_attributi:
    def __init__(self , marca,modello,anno,colore):
        self._marca = marca
        self._modello = modello
        self._anno = anno
        self._colore = colore
        self._livello_carburante = 100  # livello iniziale
        
        
        
        
# Metodi (comportamenti) / funzioni:
"""
I metodi sono funzioni definite all'interno 
della classe che operano sui dati dell'oggetto. 

"""
class Automobilie_esempio_metodi:
    def __init__(self , marca,modello,anno,colore):
        self._marca = marca
        self._modello = modello
        self._anno = anno
        self._colore = colore
        self._livello_carburante = 100  # livello iniziale
        
    def accendi_motore(self):
        print(f"il {self._modello} si mette in moto")
        
    def accellera(self):
        print(f"il {self._modello} sta accellerando nonostante sia del{self._anno}")

    def frena(self):
        print(f"il {self._modello} sta frenanto ma ha ancora {self._livello_carburante}litri di carburante")
            
        
        
        
        
# Il metodo __init__ : un costruttore speciale
"""
Il suo ruolo principale è quello di inizializzare
gli attributi dell'oggetto con i valori appropriati.

class Car:
    def __init__(self, make, model, year, color):
        # ... (initializes attributes)

"""
        


        
        
        
        
        
        
        
        
        
        
        