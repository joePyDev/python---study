
# dir() 
# help()


"""

counts = {}

counts['apple'] = counts.get('apple', 0) + 1
counts['apple'] = counts.get('apple', 0) + 1
counts['apple'] = counts.get('apple', 0) + 1

print(counts)



words = ['apple', 'banana', 'apple']

counts = dict()

for w in words:
    counts[w] = 10

print(counts)



lines = ["red blue", "green yellow"]

for line in lines:
    words = line.split()
    for w in words:
        print(w)


line = "clown ran away"
words = line.split()
print(words)



counts = {'apple': 3, 'banana': 5, 'cherry': 2}

largest = None
for word, count in counts.items():
    if largest is None or count > largest:
        largest = count

print(largest)

"""



# Sfida di programmazione funzionale: Calcolatrice di prezzi

sconto = 15
prezzo_articolo = 75 

valore_sconto = sconto / 100 * prezzo_articolo
prezzo_scontato = prezzo_articolo - valore_sconto

print(f"il prezzo scontato è: {prezzo_scontato}")  



















