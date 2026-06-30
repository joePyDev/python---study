#  Chiedi all'utente un numero e determina se è primo o meno.


def è_primo(n):
    if n < 2:
        return
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        print("debugg", i)
        if n % i == 0:
            return False


# main

try:
    numero_utente = int(input("Scegli un numero: "))
    if è_primo(numero_utente):
        print(f"Il numero {numero_utente} è primo!")
    else:
        print(f"Il numero {numero_utente} è composto (o minore di 2).")
except ValueError:
    print("Errore: devi inserire un numero intero!")
