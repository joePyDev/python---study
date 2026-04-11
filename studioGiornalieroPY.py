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

"""


fhand = input("inserisci il percorso file")
with open(fhand) as myFile:
    for line in myFile:
        line = line.rstrip()
        if not line.startswith(("From")): continue
        words = line.split()
        if len(words) > 3:
            print(words[2])







