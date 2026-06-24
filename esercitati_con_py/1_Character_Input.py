import datetime
import sys

anno_corrente = datetime.datetime.now()
anno = anno_corrente.strftime("%Y")
anno = int(anno)

try:
    nome = input(">>> Enter your name:")
    eta = int(input(">>> Enter your age: "))

except ValueError as e:

    print(f"Errore di tipo: {e}")
    sys.exit()

if eta > 0:
    differenza = 100 - eta
    print(f"{nome} Avrai 100 anni nel { anno + differenza} ")
else:
    print("non sei ancora nato")


altro_numero = int(input("Inserisci un altro numero: "))

for i in range(altro_numero):
    print(f"{nome} Avrai 100 anni nel { anno + differenza} ")

for i in range(altro_numero):
    print(f"{nome} Avrai 100 anni nel { anno + differenza}\n")
