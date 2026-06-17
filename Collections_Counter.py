from collections import Counter

a = [1,2,3,4,5,6,6,3,4,4,4,5,6,6]

cnt = Counter(a)
print(cnt)

ctr1 = Counter([1, 2, 2, 3, 3, 3]) # From a list
ctr2 = Counter({1: 2, 2: 3, 3: 1}) # From a dictionary
ctr3 = Counter('hello') # From a string

print(ctr1)
print(ctr2)
print(ctr3,"str")

print(Counter("aaa"))