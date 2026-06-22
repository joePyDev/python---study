# la funzione range() viene usata per generare una sequenza di numeri interi

# range(start,stop,step)

# l'argomento richiesto è stop e non inclusivo
for num in range(3):
    print(num)  # 0 1 2
print()
print(">>>>>>>>>>>>>\n")


# specificando start:


for numero in range(3, 5):
    print(numero)

print()
print(">>>>>>>>>>>>>\n")


# specificando step:

for numero in range(2, 11, 2):
    print(numero)

print()
print(">>>>>>>>>>>>>\n")


# sequenza in ordine decrescente:

for decnum in range(100, 0, -10):
    print(decnum)


print()
print(">>>>>>>>>>>>>\n")


# possiamo creare una lista usando il costruttore list()

numeripari = list(range(2, 11, 2))
print(numeripari)
