
def calcolo_area_rettangolo(base=1 , altezza=1):
    """ valori di default per calcolare area del quadrato """
    area = base * altezza 
    return area

area = calcolo_area_rettangolo()
print(area)



# Esempio 1 – Saluto personalizzato o generico
def saluto(nome="amico"):
    """ se si passa il nome ,senno print amico """
    print(f"ciao {nome}")
    
saluto()   
saluto("franco")




# Esempio 2 – Calcolo prezzo con IVA opzionale

def prezzo_totale(importo,iva=22):
    return importo + (importo * iva / 100)

print(prezzo_totale(100))      # 122.0  (IVA 22% di default)
print(prezzo_totale(100, 10))  # 110.0  (IVA al 10%)




# * raccoglie in una tupla  i posizionali, e ** in un dizionario kwargument
def flexible_function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

flexible_function(1, 2, 3, name="Alice", age=30)

# Argomenti posizionali: (1, 2, 3)
# Argomenti con parole chiave: {'nome': 'Alice', 'età': 30}




def create_user_profile(name, age, occupation="Student", interests=None): # Use None as default
    """
    Creates a user profile with optional interests.

    Args:
        name (str): The user's name (required).
        age (int): The user's age (required).
        occupation (str, optional): The user's occupation (defaults to "Student").
        interests (list, optional): A list of the user's interests (defaults to None).
    """
    if interests is None:  # Initialize if None
        interests = [] 

    profile = {
        "name": name,
        "age": age,
        "occupation": occupation,
        "interests": interests
    }

    return profile

# Usage
user1 = create_user_profile("Alice", 25, "Software Engineer", ["Coding", "Hiking"])
user2 = create_user_profile("Bob", 18)  # Uses default occupation and no interests
user3 = create_user_profile("Carol", 30, interests=["Gardening", "Reading"])

print(user1)
print(user2)
print(user3)












