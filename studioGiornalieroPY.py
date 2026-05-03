nome = "pippo"
frase = "Ciao come stai"
eta = 30

X = len(frase.split())

if frase.lower().startswith("ciao"):
    print("si")

print(nome+" "+ frase +" ", str(eta))


print(frase[-2:].upper())

print(frase[2:5])


X = int(len(frase)/2)
print(frase[X:])




X = 5
Y = 10
Z = 50

risultato = (X + Y) ** 2 - Z

eta = "25"

print(risultato - int(eta) * 3)

X +=  2 * (Y % Z) 

print(X)


print(abs(Y - (Z ** 4)))