
# dir() 
# help()




# analisi avanzata strighe

import string
#print(string.punctuation)



fname = input("inserisci il nome del file")
try:
    fhand = open(fname)
except:
    print(f"il file non può essere aperto: {fhand} ")
    exit()
count = dict() 
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans("","",string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if not word in count:
            count[word] = 1
        else:
            count[word] += 1
print(count)            




# creare una lista di chiavi/valori

A = {"A":1 , "B": 2 , "C" : 3}

print(list(A))
print(list(A.keys()))
print(list(A.values()))
print(list(A.items()))


# Bonus! 2 iteration variables


for x , y in A.items():
    print(x , y )




name = input("inserisci un file")

try:
    fhand = open(name)
except:
    print("file errato",name)
    exit()
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0)+1
print(counts)      
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword,bigcount)        
  






























