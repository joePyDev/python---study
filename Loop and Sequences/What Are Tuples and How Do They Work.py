# Una tupla è un tipo di dato Python utilizzato per creare una sequenza ordinata di valori.
developer = ("alice",34,"rust dev")

# le tuple sono immutabili, e non possono essere modificate

# accesso ad un elemento:
print(developer[1])

# indicizzazione negativa:
print(developer[-1])


#☺ Se si tenta di inserire un indice che supera o
# è uguale alla lunghezza della tupla, si riceverà un errore IndexError

numbers = (1,2,3,4,5,6)
# print(numbers[6]) # tuple index out of range


# per creare una tupla possiamo usare il costruttore tuple():
lettere = "abcdefghi"
print(tuple(lettere))


# verifica elemento nella tupla con in:
numeri = (1,2,3,4,5,6,7,8,9)
print(1 in numeri)



# È possibile estrarre gli elementi da una tupla proprio come si fa con le liste:

soggetto = ("pippo","muratore",35)

nome , professione , eta = soggetto

print(nome)
print(professione)
print(eta)

