import sys

nome = ""
print("Il nome dello script è:", sys.argv[0])

# Leggo gli argomenti passati
if len(sys.argv) > 1:
    nome = sys.argv[1]
    print("Ciao,", nome)
else:
    print("Non hai passato alcun nome!")


if nome != "":
    print(nome)
else:
    print("no name")
