numero = int(input("Inserisci un numero: "))
multiplo_quattro = numero % 4
risultato = numero % 2
if risultato == 0 and not multiplo_quattro == 0:
    print("numero pari")
elif risultato == 1 and not multiplo_quattro == 0:
    print("Numero dispari")
else:
    print(f"{numero} è un Multiplo di 4")


num = int(input("Inserisci un numero: "))
ceck = int(input("Inserisci numero ceck: "))
modulo = num % ceck
if modulo == 0:
    print("Divisione esatta")
else:
    print("Non è una divisione esatta")


"""
num = int(input("give me a number to check: "))
check = int(input("give me a number to divide by: "))

if num % 4 == 0:
    print(num, "is a multiple of 4")
elif num % 2 == 0:
    print(num, "is an even number")
else:
    print(num, "is an odd number")

if num % check == 0:
    print(num, "divides evenly by", check)
else:
    print(num, "does not divide evenly by", check)
"""
