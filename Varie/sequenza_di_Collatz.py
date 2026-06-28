import sys


def collatz(number):
    if number % 2 == 0:
        risultato = number // 2
    else:
        risultato = 3 * number + 1
    print(risultato)
    return risultato


try:
    numero = int(input("inserisci un numero:"))
    while numero != 1:
        numero = collatz(numero)
except ValueError:
    print("eggs!! devi inserire un numero!")
    sys.exit()
