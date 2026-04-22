even_numbers = []

for num in range(21):
    if num % 2 == 0:
        even_numbers.append(num)
print(even_numbers)        





# list comprehension:
    
even_numbers = [num for num in range(21) if num % 2 == 0]
print(even_numbers)

"""
La struttura base

[espressione for elemento in iterabile if condizione]
 "crea una lista composta da espressione per ogni elemento nell'iterabile,
 ma solo se la condizione è vera" (la parte if è opzionale).

"""

# senza condizione: 
quadrati = [x**2 for x in range(5)] 
print(quadrati)

quadrati = []
for x in range(5):
    quadrati.append(x**2)




# con condizione (if):
pari = [x for x in range(10) if x %2 == 0]



# Con if-else come ESPRESSIONE (da mettere prima del for)
risultati = ["pari" if x %2 == 0 else "dispari" for x in range(5)]



numbers = [1,2,3,4,5]
result = [(num,"even") if num % 2 == 0 else (num,"odd") for num in numbers ]  
print(result)



# funzione filter()
# Applica una funzione predicato (che restituisce True o False)
# e restituisce solo gli elementi per cui il predicato è True.
parole = ["pianta","sedia","auto","sole"]
def is_long_word(word):
    return len(word) > 4

paroleLunghe = list(filter(is_long_word, parole))
print(paroleLunghe)




# funzione map:
# Applica la funzione a ogni elemento e restituisce i risultati trasformati.
celsius = [0,10,20,30,40]

def to_far(temp):
    return (temp * 9 / 5) + 32

far = list(map(to_far, celsius))
print(far)







# funzione sum:
numbers = [5,10,15,20,25]
total = sum(numbers)
print(total) # 75


numbers = [5,10,15,20,25]
total = sum(numbers,10) # positional argument
print(total)  # 85



numbers = [5,10,15,20,25]
total = sum(numbers,start=10) # keyword argument
print(total)  # 85






















































