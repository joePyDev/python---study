import re

somma = 0
fhand = open(r"Sample data.txt")
for line in fhand:
    line = line.rstrip()
    numeri = re.findall("[0-9]+", line)
    if len(numeri) > 0:
        for valore in numeri:
            numeriInteri = int(valore)
            somma += numeriInteri
print(somma)


import re

somma = 0
fhand = open(r"Actual data.txt")
for line in fhand:
    line = line.rstrip()
    numeri = re.findall("[0-9]+", line)
    if len(numeri) > 0:
        for valore in numeri:
            numeriInteri = int(valore)
            somma += numeriInteri
print(somma)
