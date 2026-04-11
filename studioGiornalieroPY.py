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

"""

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



























