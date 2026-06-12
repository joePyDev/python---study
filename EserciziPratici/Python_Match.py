
# Se viene trovata una corrispondenza, viene eseguito il blocco di codice associato.
day = int(input("digita un numero da 1 a 7"))

match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")
    
    
    
""" 
Utilizza il carattere di sottolineatura _ come ultimo valore della condizione
se desideri che un blocco di codice venga eseguito quando
non ci sono altre corrispondenze:
"""

day = 4
match day:
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:
    print("Looking forward to the Weekend")
    

"""
Utilizza il carattere barra verticale | come operatore OR nella valutazione
dei casi per verificare la presenza di più di una corrispondenza di valore 
in un singolo caso :
"""
    
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")
    
    

"""
È possibile aggiungere if delle istruzioni
nella valutazione del caso come ulteriore
verifica delle condizioni:
"""
month = 5
day = 4
match day:
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("A weekday in April")
    
        







    
    
