# sappiamo che per definire una funzione dobbiamo usare la parola def:


def square(num):
    return num**2


print(square(4))


# rifattorizzata con lambda:

lambda num: num**2

numeri = [1, 2, 3, 4, 5, 6]

numeri_pari = list(filter(lambda x: x % 2 == 0, numeri))
print(numeri_pari)


# non è una buona pratica assegnare una funzione lambda a una variabile in questo modo:
numeri = [1, 2, 3, 4, 5, 6]
square = lambda x: x**2
numeri_square = list(map(square, numeri))


# evitare di creare funzioni lambda difficili da leggere o inutilmente complicate
result = (lambda x: (x**2 + 2 * x - 1) if x > 0 else (x**3 - x + 4))(3)
print("Result", result)  # 14
