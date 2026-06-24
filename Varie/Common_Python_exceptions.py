"""
# NameError

def myfunction():
    local_var = 10
print(local_var) # NameError: name 'local_var' is not defined

attenzione a:
-syntax
-scope
-external module import

"""

# -------------------------------------------------------------------

"""
# TypeError

-Operazioni non corrispondenti
-Argomenti di funzione non corretti
-Problemi di ereditarietà delle classi

"""


def calculate_area(length, width):
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        raise TypeError("Length and width must be numbers.")
    return length * width


print(calculate_area(5, "three"))  # TypeError: Length and width must be numbers.

# -------------------------------------------------------------------

"""
IndexError

-Accesso fuori dai limiti
-Sequenze vuote

"""
# verificare la lunghezza della sequenza prima dell acesso
my_list = [1, 2, 3]
for i in range(len(my_list)):
    print(my_list[i])

# lista vuota
my_list = []
try:
    print(my_list[0])
except IndexError:
    print("The list is empty.")

# -------------------------------------------------------------------

"""
# KeyError

-Chiave inesistente
-Creazione dinamica delle chiavi

prima di accedere alla chiave verificare l'esistenza, ad esempio
con 'in' o con il metodo get()

"""
my_dict = {"a": 1, "b": 2}
try:
    print(my_dict["c"])
except KeyError:
    print("Key not found in dictionary.")

# -------------------------------------------------------------------


# estione corretta delle eccezioni
import logging

my_dict = {"a": 1, "b": 2}
try:
    print(my_dict["c"])
except KeyError as e:
    logging.error(f"KeyError incontrato {e}")
