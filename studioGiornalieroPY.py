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


"""

# cicli di massimo e minimo

largest = None
print("Before:",largest)
for intervar in [3,41,12,9,74,15]:
    if largest is None or intervar > largest:
        largest = intervar
    print("Loop:",intervar,largest)
print("largest:",largest)    
        
















