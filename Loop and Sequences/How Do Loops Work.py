

# ciclo for:
    
nomi = ["Luca","Pippo","Giovanna"]

for nome in nomi:
    print(nome)
    
for carattere in "codecamp"    :
    print(carattere)
    
    
    
# cicli annidiati:

categorie = ["Frutta","Verdura"]
cibi = ["mela","carota","banana"]

for categoria in categorie:
    for cibo in cibi:
        print(categoria,cibo)
        
        
        
        
# ciclo while:

numero_segreto = 3
numero_inserito = 0

while numero_inserito != numero_segreto:
    numero_inserito = int(input("Indovina il numero segreto (1-5): "))
    if numero_inserito != numero_segreto:
        print("Sbagliato,prova di nuovo")
        
print("Indovinato!!")        



# break e continue:
    
lista_numeri = [1,2,3,4,5,6,7,8,9]

for numero in lista_numeri:
    if numero == 5: 
        print("Trovato il numero",numero)
        break
    print(numero)
    

lista_numeri = [1,2,3,4,5,6,7,8,9]

for numero in lista_numeri:
    if numero == 5: 
        print("Trovato il numero",numero)
        continue
    print(numero)
    


# combinazionedi for con else

parole = ['sky', 'apple', 'rhythm', 'fly', 'orange']

for parola in parole:
    for lettere in parola:
        if lettere.lower() in "aeiou":
            print(f"{parola} contiene la vocale {lettere}")
            break
    else:
        print(f"{parola} non contiene vocali ")
            













