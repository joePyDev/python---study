""" 
Esercizio 1 

Scrivi un programma che usi input per chiedere all’utente il proprio
nome e poi dia loro il benvenuto

Enter your name: Chuck
Hello Chuck



name = input(str("Enter your name:"))
print(f"Hello {name}")


"""


"""
Esercizio 2

Scrivi un programma per richiedere all’utente ore di lavoro e tariffe
orarie per calcolare la retribuzione lorda.

Enter Hours: 35
Enter Rate: 2.75
Pay: 96.25


hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
pay = float(hours) * float(rate)
print(f"\nEnter Hours: {hours}\nEnter Rate: {rate}\nPay: {pay:.2f}")

"""




"""
Esercizio 3

Scrivi un programma che, richiesta all’utente una temperatura in
gradi Celsius, la converta in Fahrenheit e poi la visualizzi.






celsius_imp = input("Inserisci i gradi Celsius: ")

def celsius_in_fahrenheit(celsius):
    try:
        # Conversione immediata
        celsius = float(celsius)
        fahrenheit = celsius * 1.8 + 32
        
        # Usiamo il Format Specifier direttamente nel return
        return f"Fahrenheit: {fahrenheit:.2f}"
        
    except ValueError:
        # Specificare il tipo di errore (ValueError) è più professionale
        return "Errore: inserisci un valore numerico valido."

A = celsius_in_fahrenheit(celsius_imp)
print(A)


"""






"""
Esercizio 4

Riscrivi lo script del calcolo della retribuzione per attribuire ad un
dipendente una maggiorazione oraria di 1,5 volte, per le ore di lavoro straordinario
fatte oltre le 40.
Enter Hours: 45
Enter Rate: 10
Pay: 475.0



ore_lavorate = float(input("Enter Hours: "))
paga_oraria = float(input("Enter Rate: "))

if ore_lavorate > 40:
    ore_ordinarie = 40 
    ore_straordinarie = ore_lavorate - 40
    retribuzione = (ore_ordinarie * paga_oraria) + (ore_straordinarie * (paga_oraria*1.5) )
else:
    retribuzione = ore_lavorate * paga_oraria
print(f"Ore lavorate: {ore_lavorate}\nPaga oraria: {paga_oraria}\nRetribuzione: {retribuzione:.2f}")


"""


"""
Esercizio 5

 Riscrivi lo script sul calcolo della retribuzione utilizzando try e
except in modo che il programma gestisca input non-numerici in maniera elegante
visualizzando un messaggio prima di uscire dal programma. Di seguito vengono
mostrate due esecuzioni del programma:
Enter Hours: 20
Enter Rate: nine
Error, please enter numeric input
Enter Hours: forty
Error, please enter numeric input



import sys

try:
    ore_lavorate = float(input("Enter Hours: "))
    paga_oraria = float(input("Enter Rate: "))
    
except ValueError:
    print("Error, please enter numeric input")
    sys.exit()

if ore_lavorate > 40:
    ore_ordinarie = 40 
    ore_straordinarie = ore_lavorate - 40
    retribuzione = (ore_ordinarie * paga_oraria) + (ore_straordinarie * (paga_oraria*1.5) )
else:
    retribuzione = ore_lavorate * paga_oraria
    
print(f"Ore lavorate: {ore_lavorate}\nPaga oraria: {paga_oraria}\nRetribuzione: {retribuzione:.2f}")

"""



"""
Esercizio 6

 Scrivi un programma per richiedere un valore compreso tra 0.0 e 1.0.
Se non è compreso nell’intervallo specificato, visualizza un messaggio di errore. Se
è compreso tra 0,0 e 1,0, visualizza un giudizio utilizzando la seguente tabella:
Score Grade
>= 0.9
A
>= 0.8
>= 0.7
>= 0.6
< 0.6
B
C
D
F
Enter score: 0.95
A
Enter score: perfect
Bad score
Enter score: 10.0
Bad score
Enter score: 0.75
C
Enter score: 0.5
F
Esegui varie volte il programma per testarlo con diversi valori di input.




import sys

try:
    my_val = float(input("Enter Score: "))
except ValueError:
    print("Bad score")
    sys.exit()
    
if my_val >= 0.0 and my_val <= 1.0:
    if my_val >= 0.9:
        grade = "A"
    elif my_val >= 0.8:
        grade = "B"
    elif my_val >= 0.7:
        grade = "C"
    elif my_val >= 0.6:
        grade = "D"
    else:
        grade = "F"
    
    print(grade)
else:
    print("Bad score")
    

"""



"""
Esercizio 7

6: Riscrivi il calcolo della tua retribuzione con gli straordinari pagati il
50%in più creando una funzione chiamata computepay che richieda i due parametri
hours e rate.
Enter Hours: 45
Enter Rate: 10
Pay: 475.0




import sys

def computepay(ore_lavorate , paga_oraria):
     #calcolo ore lavorate,retribuzione e straordinari
     #ritorna il totale retribuzione compreso straordinari
    
    if ore_lavorate > 40:
        ore_ordinarie = 40 
        ore_straordinarie = ore_lavorate - 40
        retribuzione = (ore_ordinarie * paga_oraria) + (ore_straordinarie * (paga_oraria*1.5) )
    else:
        retribuzione = ore_lavorate * paga_oraria
        
    return retribuzione




try:
    ore_lavorate = float(input("Enter Hours: "))
    paga_oraria = float(input("Enter Rate: "))
    
except ValueError:
    print("Error, please enter numeric input")
    sys.exit()

ret = computepay(ore_lavorate, paga_oraria)

print(ret)


"""






"""
Esercizio 8

Riscrivi lo script del capitolo precedente creando una funzione chia
mata computegrade che accetta un punteggio come parametro e restituisce un
voto sotto forma di stringa.





    
def computegrade(my_val):
    if my_val >= 0.0 and my_val <= 1.0:
        if my_val >= 0.9:
            grade = "A"
        elif my_val >= 0.8:
            grade = "B"
        elif my_val >= 0.7:
            grade = "C"
        elif my_val >= 0.6:
            grade = "D"
        else:
            grade = "F"
        return grade
    else:
        bad_score = ("Bad score")
        return bad_score




import sys

try:
    my_val = float(input("Enter Score: "))
except ValueError:
    print("Bad score")
    sys.exit()

X = computegrade(my_val)

print(X)



"""



"""
Scrivi un programma che legga ripetutamente i numeri fino a quando
l’utente non digiti “finito”. Una volta che viene digitato “finito”, dovrà essere
visualizzato il totale, il conteggio e la media dei numeri. Se l’utente dovesse digitare
qualcosa di diverso da un numero, occorrerà rilevare l’errore usando try e except,
visualizzare un messaggio di errore e passare al numero successivo.
"""


import sys
contatore = 0
somma_numeri_inseriti = 0

while True:
    try:
        numeri_inseriti = input("Inserisci un numero da 1 a 10")
        if numeri_inseriti == "finito": break
        contatore += 1
        somma_numeri_inseriti = somma_numeri_inseriti + float(numeri_inseriti)
    except ValueError:
         print("input errato")
         sys.exit()
         
print(somma_numeri_inseriti)
print(contatore)
print(somma_numeri_inseriti / contatore)











