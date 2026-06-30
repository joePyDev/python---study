def box_print(simbolo, larghezza, altezza):
    if len(simbolo) != 1:
        raise Exception("il simbolo deve essere un singolo carattere")
    if larghezza <= 2:
        raise Exception("larghezza deve essere maggiore di 2")
    if altezza <= 2:
        raise Exception("Altezza deve essere maggiore di 2")

    print(simbolo * larghezza)
    for i in range(altezza - 2):
        print(simbolo + (" " * (larghezza - 2)) + simbolo)
    print(simbolo * larghezza)


try:
    box_print("*", 4, 4)
    box_print("O", 20, 5)
    box_print("x", 1, 3)
    box_print("ZZ", 3, 3)
except Exception as err:
    print("An exception happened: " + str(err))
try:
    box_print("ZZ", 3, 3)
except Exception as err:
    print("An exception happened: " + str(err))
