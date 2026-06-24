import random
import statistics
import sys

# scelta casuale
moneta = random.choice(["testa", "croce"])

# random da interi
numero = random.randint(1, 10)

# mescola carte
carte = ["regina", "re", "bastoni"]
random.shuffle(carte)
for carta in carte:
    print(carta)


# calcolo avg
media = statistics.mean([100, 90])


print("ciao mi chiamo", sys.argv[1])
