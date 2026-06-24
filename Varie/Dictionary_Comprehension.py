"""
Dictionary comprehension is used to create a dictionary in a short and clear way.

{ chiave: valore for elemento in iterabile }


key: The item to use as the dictionary key.
value: The item to use as the dictionary value.
iterable: Any sequence or collection to loop through.
condition (optional): Lets you include only certain items

"""

sq = {x: x**2 for x in range(1, 6)}

keys = ["a", "b", "c", "d", "e"]
values = [1, 2, 3, 4, 5]
d = {k: v for (k, v) in zip(keys, values)}


quadrati = {}
for x in range(5):
    quadrati[x] = x**2
print(quadrati)
quadrati = {x: x**2 for x in range(5)}
print(quadrati)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}


parole = ["gatto", "cane", "topo"]
# la chiave è la variabile del ciclo
dict_parole = {x: len(x) for x in parole}


parole = ["gatto", "cane", "topo"]
# La chiave può essere il risultato di un'espressione qualsiasi applicata a x
diz = {x.upper(): len(x) for x in parole}
# Output: {'GATTO': 5, 'CANE': 4, 'TOPO': 4}
