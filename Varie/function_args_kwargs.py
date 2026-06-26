# -----------------------------------------------------------


# la funzione riceverà una tupla di argomenti e potrà accedere agli elementi
# *args
def my_funk(*args):
    print(f"il valore scelto è {args[2]}")


my_funk("1", "2", "3")

# -----------------------------------------------------------


# **Kwargs
def my_function(**kid):  # con i due asterischi **kid diventa un dizionario

    # cerca nel dizionario chid la chiave iname e ritorna il valore
    print("His last name is " + kid["lname"])


my_function(fname="Tobias", lname="Refsnes")
# kid = {"fname": "Tobias", "lname": "Refsnes"}
