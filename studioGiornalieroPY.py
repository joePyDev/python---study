"""
# ITERAZIONE

# aggiornamento variabili:
    
X = 0
X = X + 1


# while

n = 5 
while n > 0:
    print(n)
    n = n - 1
print("decollo")

    
while True:
    line = input("> ")
    if line == "done":
        break
    print(line)
print("Done!!")    


# continue
while True:
    line = input("> ")
    if line[0] == "#":
        continue
    if line == "done":
        break
    print(line)
print("Done!")    


# FOR

friends = ["joseph", "Glenn","Sally"]
for friend in friends:
    print("Happy new year:",friend)
    
print("Done!")    


# Cicli per contare e sommare

count = 0 

for interval in [3,41,12,9,74,15]:
    count = count + 1
print("Count: ",count)    


total = 0
for intervar in [3,41,12,9,74,15]:
    total = total + intervar
print(total)    



# cicli di massimo e minimo

largest = None
print("Before:",largest)
for intervar in [3,41,12,9,74,15]:
    if largest is None or intervar > largest:
        largest = intervar
    print("Loop:",intervar,largest)
print("largest:",largest)    


smallest = None
print("Before:",smallest)
for intervar in [3,41,12,9,74,15]:
    if smallest is None or intervar < smallest:
        smallest = intervar
    print("Loop:",intervar,smallest)    
print("Smallest:",smallest)



def min(values):
    smallest = None
    for value in values:
        if smallest is None or value < smallest:
            smallest = value
    return smallest        
        
val = [1,2,3,4,5,6,7,8,9]
print("minimo:",min(val))



# Stringhe

fruit = "banana"
letter = fruit[1]
print(letter)



# len()

fruit = "banana"
print(len(fruit))

lenght = len(fruit)

last = fruit[lenght-1]

print(last)

A = fruit[-1]

B = fruit[-2]

print(A,B)


# scorrere una stringa con un ciclo

index = 0
print("begin")
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index +1
print("end")


# for

for char in fruit:
    print(char)
    
    
# segmenti di stringhe

s = "Monty Python"
print(s[0:5],s[6:12])

print("!!",fruit[1:1],"!!")
    
    
# immutabili

greeting = "Hello word"
new_greeting = greeting[4:8]
print(new_greeting)
    


# cicli e conteggi
word = "Banana"
count = 0
for letter in word:
    if letter == "a":
        count = count +1
print(count)        
        
        
# operatore IN

b_ool = "a" in word
b_oool = "seed"in word

print(b_ool,b_oool)
    
    
# comparazione stringhe
if b_ool == b_oool:
    print("vero")
    
    
 
    

#----------------------------------

# metodi delle stringhe:
    
A = " sono una stringaAAA "   
print(A) 
 
    
A = A.upper()
print(A) 
    
A = A.lower()
print(A) 

A = A.strip()
print(A) 

A = A.replace("sono","ero")
print(A) 

A = A.split()
print(A) 


A = " ".join(A)
print(A)


if A.startswith("ero"):
    print(A,"startsWith")

if A.endswith(("a")):
    print(A,"endsW")
    
A = A.find("aa")
print(type(A))
    
A = " sono una stringaAAA "   

A = A.count("AA")
print(A)

A = "sono una stringaAAA "   

A = A.capitalize()
print(A)

A = A.isupper()
print(A)

A = "sono una stringaAAA "   
A = A.islower()
print(A)


A = "sono una stringaAAA "   
A = A.title()
print(A)


A = "sono una stringaAAA "   

A = A.maketrans("abc","123")
print(A)



#-------------------------------------


# operazioni matematiche



int_1 = 56
int_2 = 12

print( int_1 + int_2 )


float_1 = 5.4
float_2 = 12.0

print(float_1 + float_2)


print(int_1 + float_1)



print(int_1 % int_2)

print(int_1 / int_2)

print(int_1 // int_2)

print(int_1 ** int_2)



A = float(int_1)
print(A)


B = int(float_1)

print(B)


C = round(float_2)
print(C)


D = abs(-float_2)
print(D)


print(bin(50),oct(50),hex(50),pow(50,2))



# assegnazioni aumentate

my_var = 10
my_var += 5

print(my_var)


count = 14
count -= 3
print(count)


product = 65
product *= 7
print(product)


divisione = 100
divisione /= 4
print(divisione)



# funzioni

def get_sum(num_1,num_2):
    return num_1 + num_2

result = get_sum(3,4)
print(result)



# Se una funzione non restituisce esplicitamente un valore,
# il valore di ritorno predefinito è None:
    
    
def greet():
    print('hello') 

result = greet() # hello
print(result) # None


# specificare parametri 

def get_sum2(num_1 , num_2=5):
    return num_1 + num_2

total = get_sum2(5)

print(total)



# ambito di visibilita variabili


# local 
def my_func():
    num = 10
    print(num)


# delimitazione
def outer_func():
    msg = "hello there"
    
    def inner_func():
        print(msg)
        
    inner_func()

    
A = outer_func()       




# globale
tax = 0.70

def get_total(subtotal):
    total = subtotal + (subtotal * tax)
    return total

print(get_total(100))


# predefinito
print(str(45)) # '45'
print(type(3.14)) # <class 'float'>
print(isinstance(3, str)) # False



# operatori di comparazione
print(3 == 4)
print(3 != 4)
print(3 > 4)
print(3 < 4)
print( 3 >= 4)
print(3 <= 4)



# condizionali


age = 18
if age >= 18:
    print("sei maggiorenne")
elif age >= 13:
    print("sei un ragazzo")
else:
    print("sei un bambino")
    


# if annidiato

is_citizen = False
age = 18

if is_citizen:
    if age >= 18:
        print("puoi votare")
else:
    print("non puoi votare")        



print(bool(False)) # False
print(bool(0))  # False
print(bool('')) # False

print(bool(True)) # True
print(bool(1)) # True
print(bool('Hello')) # True


# Boolean Operators and Short-circuiting 
print(True and age) # 18

print(True or age) # True



print(not '') # True, because empty string is falsy
print(not 'Hello') # False, because non-empty string is truthy
print(not 0) # True, because 0 is falsy
print(not 1) # False, because 1 is truthy
print(not False) # True, because False is falsy
print(not True) # False, because True is truthy



is_admin = False

if not is_admin:
    print("Accesso negato per non amministratore")
else:
    print("accesso consentito")    





developer = 'Naomi'

result = developer.endswith('N') # ?

print(result)



"""






#In Python, gli operatori and e or non restituiscono necessariamente
#un valore booleano (True o False), ma restituiscono 
#l'ultimo valore valutato durante il processo.


# cortocircuito and
# and: Restituisce il primo valore Falso che incontra; se sono tutti veri, restituisce l'ultimo valore.
print( False and 0) # false
print( True and 0) # 0


# cortocorcuito or 
# or: Restituisce il primo valore Vero che incontra; se sono tutti falsi, restituisce l'ultimo valore.
print( False or 0) # 0
print( "True" or 0) # True




utente = ""

# Se 'utente' è None o vuoto, usa "Ospite"
nome = utente or "Ospite"

print(nome)




numeratore = 2
denominatore = 0

# Evita un errore di divisione per zero
risultato = (denominatore != 0) and (numeratore / denominatore)

print((risultato))



# esercizi:
X = [] or [1,2,3,4]

print(X)    


print(True and 3 > 5)


print(None or 0 or "Fine")


print("mela" and "pera")




risultato = 50 or 0

print(risultato)


print(bool("" and 10))

print([] or {} or "Dato")

print(19 < 5 or "Almeno uno è vero")


risultato = (100 > 0) and (200 > 100)


bool(0 or None)


Y = 0.0 or 0 or False
 

