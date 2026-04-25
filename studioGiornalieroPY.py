
# dir() 
# help()


numbers = [3,9,1,10,5,2,8]

for number in numbers:
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
        
        
        
for i in range(10,-1,-1):
    print(i)
    if i == 5:
        print("Raggiunto il punto intermedio!" )
    
    
    
    
    

def livello4():
    print("Livello 4: sto per finire")
    return 4

def livello3():
    print("Livello 3: chiamo livello4")
    risultato = livello4()
    print(f"Livello 3: livello4 ha restituito {risultato}")
    return 3

def livello2():
    print("Livello 2: chiamo livello3")
    risultato = livello3()
    print(f"Livello 2: livello3 ha restituito {risultato}")
    return 2

def livello1():
    print("Livello 1: chiamo livello2")
    risultato = livello2()
    print(f"Livello 1: livello2 ha restituito {risultato}")
    return 1

# Chiamata iniziale
livello1()    






def raddoppia(x):
    print("si entra in raddoppia")
    risultato = x * 2
    print(f"con valore x {x} e risultatto {risultato}")
    print("si esce da raddoppia")
    return risultato

n = 7
doppio = raddoppia(n)
print("risultato finale", doppio)



def somma(a,b):
    print("sono dentro somma e con valori a & b = ",a,"&",b)
    return a + b

def triplo(val):
    print("ingresso su triplo val=",val)
    print("sto per entrare in somma")
    temp = somma(val, val+1)   
    print("sono tornato dentro triplo e temp è == ", temp)
    return temp + val


print("inizio")
ris = triplo(4)
print("sono uscito dalle funzioni e il risultato è")
print(ris)




