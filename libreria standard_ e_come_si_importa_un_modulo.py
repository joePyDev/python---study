"""
Alcuni moduli piu comuni:


math

random

re

datetime


con import "modulo" si aggiunge la libreria '


"""

# esempio:

import math

# la funzione si richiama con la notazione con il punto:
# nome modulo . nome funzione

# module_name.function_name()


# $ radice quadrata
radice_quadrata = math.sqrt(36)
print(radice_quadrata)


"""
se si vuole importare il modulo con un nome diverso(alias)

import module_name as module_alias

es: import math as m

    rq = m.sqrt(36)

"""


"""
E possibile importare solo parti di moduli:
    
from module_name import name1 , name2    
    
possiamo anche creare alias di parti di moduli:

from module_name import name1 as alias1 , name2 as alias2

    
"""

"""
# calcolare il seno e il coseno di un angolo

importando cosi le funzioni possiamo omettere 
il prefisso al momento della chiamata ma può causare conflitti
se ci sono nomi di variabili simili,ATTENZIONE!


from math import radians,sin,cos

angle_degrees = 40
angle_radians = radians(angle_degrees)

sine_value = sin(angle_radians)
cos_value = cos(angle_radians)

print(sine_value) # 0.6427876096865393
print(cos_value)  # 0.766044443118978


"""


import math

angle_degrees = 40
angle_radians = math.radians(angle_degrees)

sine_value = math.sin(angle_radians)
cos_value = math.cos(angle_radians)

print(sine_value)  # 0.6427876096865393
print(cos_value)  # 0.766044443118978


"""
utilizzando l'asterisco si importa tutto il contenuto del modulo
senza l'obbligo di specificare il nome del modulo come prefisso'

from module_name import *


from math import *
print(sqrt(36))  # 6.0
print(pow(5, 2)) # 25.0
print(exp(1))    # 2.718281828459045

Tuttavia, questa pratica è generalmente sconsigliata
perché può causare conflitti 

"""

"""


if __name__ == '__main__': 
    # Code
- se un file viene eseguito direttamente name viene impostata su main
- se il file viene importato come modulo name prende il nome del modulo

utile se vogliamo eseguire del codice solo se è in 
esecuzione come programma principale

"""
