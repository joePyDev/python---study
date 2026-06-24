"""
[espressione for elemento in iterabile]

Prendi ogni elemento dall'iterabile,
esegui su di esso l'espressione e metti
il risultato in una nuova lista.

"""

numeri = [1, 2, 3, 4, 5, 6]

# ciclo classico

quadrati_classici = []
for n in numeri:
    quadrati_classici.append(n**2)

print(quadrati_classici)


# Con list comprehension (molto più diretta)

quadrati = [n**2 for n in numeri]
print(quadrati)


# Filtrare elementi con IF in coda
X = [num for num in numeri if num > 2]
print(X)


# Logica condizionale (con if-else nell'espressione)
# Se vogliamo trasformare l'elemento in base a una condizione,
# l'if-else va messo prima del for.


# etichette pari o dispari
etichette = ["Pari" if n % 2 == 0 else "Dispari" for n in numeri]

condizione = [True if n % 2 == 0 else False for n in numeri]


"""
Regola mnemoniche fondamentali:

... if ... dopo il for = Filtro (escludo elementi).

... if ... else ... prima del for = Operatore ternario (modifico il valore).

"""


# 4 cicli annidiati
matrice = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
piatta = [numero for riga in matrice for numero in riga]


# ATTENZIONE: modo SBAGLIATO (crea riferimenti allo stesso oggetto)
# sbagliata = [[0] * 3] * 3  # NON USARE MAI


# Modo CORRETTO con list comprehension annidata
tabella = [[0 for _ in range(3)] for _ in range(3)]
print(tabella)  # Output: [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# Ogni riga è un oggetto indipendente in memoria.


coordinate = [(x, y) for x in range(3) for y in range(3)]
print(coordinate)

# che corrisponde a:
coordinate = []
for x in range(3):  # <-- Primo for (ESTERNO)
    for y in range(3):  # <-- Secondo for (INTERNO)
        coordinate.append((x, y))
