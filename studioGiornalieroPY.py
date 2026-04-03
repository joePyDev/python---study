
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

    

# infinito!!
"""
n = 10 
while True:
    print(n,end=" ")
    n = n -1
print("Done!")
"""    



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






















