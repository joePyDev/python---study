
# dir() 
# help()





x = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
y = x.items()


print(y)
days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
print(days[2])

X = ("glen","sally","joseph")
print(X[1])
X = (1,2,3,4,5,6)
print(X)
print(max(X))





(x , y) = ( 4 , 5 )

print(x)
print(y)


d = dict()
d["csev"] = 2
d["cwen"] = 4

for (k,v) in d.items():
    print(k,v)
    
tups = d.items()
print(tups)    

d = {"a":10 , "f":123,"c": 12 }

print(d.items())
print(sorted(d.items()))


d = {"a":10 , "f":123,"c": 12 }
diz = dict()
for k,v in sorted(d.items()):
    print(k,v)
    diz[k] = v
    print(diz)


c = {"a":12,"B":14,"C":45,"s":36}
tmp = list()
for k,v in c.items():
    tmp.append((v,k))
print(sorted(tmp , reverse = True))





















