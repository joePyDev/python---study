import random

for i in range(100):  # cento lanci
    if random.randint(0, 1) == 0:
        print("T", end=" ")
    else:
        print("C", end=" ")
print()  # stampa nuova riga alla fine
