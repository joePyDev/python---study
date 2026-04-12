"""
# metodi delle lista:
    
T = [1,2,3,4,5,6,7,8,9]
T.append("fine lista")
print(T)



T1 = ["a","b","c","d"]
my_copy = T1.copy()
T2 = [1,2,3]
T1.extend(T2)
print(T1,my_copy)



t = ["a","b","c"]
XX = t.pop()
print(t , XX)


T = [1,2,3,4,5,6,7,8,9]
del T[1:5]
print(T)


T = [1,2,3,4,5,6,7,8,9]
A = T.remove(5)
print(A)



# liste e funzioni integrate

num = [1,2,3,4,5,6,7,8,9]
print(len(num))

print(max(num))

print(min(num))

print(sum(num))

print(sum(num) / len(num))


total = 0 
count= 0
while True:
    inp = input("inserisci un numero")
    if inp == "done": break
    value = float(inp)
    total = total + value
    count = count + 1

average = total / count
print("Media: ", average)    




numlist = list()

while (True):
    inp = input("inserisci un numero") 
    if inp == "done": break
    value = float(inp)
    numlist.append(value)
    
average = sum(numlist) / len(numlist)

print(average)    






S = "spam"
T = list(S)
print(T)


S = "sono una lista di parole"
T = S.split()
print(T[2])



S = "spam-spam-spam-spam"
delimiter = "-"
S = S.split(delimiter)

print(S)


T = ["spinning","for","aaa","popp"]
delimit = "...."
newT = delimit.join(T)

print(newT)




help(str.split)



fhand = input("inserisci il percorso file")
with open(fhand) as myFile:
    print(myFile,"!!!")
    for line in myFile:
        line = line.rstrip()
        if not line.startswith(("From")): continue
        words = line.split()
        if len(words) > 3:
            print(words[2])



"""




# oggetti e valori


# unico oggetto a cui fanno riferimento 2 etichette
A = "stringa"
B = "stringa"

print(A is B) # true



# creando 2 liste invece si crea 2 oggetti

a = [1,2,3]
b = [1,2,3]

print(a is b) # false

# un oggetto ha un valore che è una sequenza di eelementi



C = (1,2,3)
D = (1,2,3)

print(C is D)




# alias
# Se a si riferisce ad un oggetto e assegni b = a, allora entrambe le variabili si
# riferiscono allo stesso oggetto:

A = [1,2,3]

B = A

B.append(5) # modifica in-place tutti gli alias vedono la modifica

print(A)

print(B is A , "flag")

# Se l’oggetto con alias è modificabile, le modifiche apportate su un alias si riflettono
# sugli altri:


# Sebbene questo comportamento possa essere utile, è spesso fonte di errori. In
#generale, è meglio evitare gli alias quando si lavora con oggetti mutabili.
prezzi_originali = [100, 200, 300]
prezzi_scontati = prezzi_originali.copy() # COPIA

# Modifico la copia
for i in range(len(prezzi_scontati)):
    prezzi_scontati[i] *= 0.9
    print("Scontato:",prezzi_scontati[i] , "e prezzo originale" , prezzi_originali[i])

print(prezzi_originali) # [100, 200, 300] -> SALVO!













