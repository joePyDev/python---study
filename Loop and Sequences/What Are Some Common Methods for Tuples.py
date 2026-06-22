# metodo count() determina quante volte un elemento appare in una tupla

tp = (1, 2, 3, 1, 2, 1, 2, 3, 1, 2, 1, 2, 3)
print(tp.count(1))


# metodo index() utilizzato per trovare l'indice di un elemnto in una tupla:
tp = ("33", "56", "sss", "65")
print(tp.index("sss"))


# index() da la possibilita di passare l'indice da dove iniziare la ricerca:

# tp = ("33","56","sss","65","py","sss","sll")
# Ìprint(tp.index("sss",3)) # 5


# è possibile anche inserire un indice di arreso

tp = (
    "33",
    "56",
    "sss",
    "65",
    "py",
    "sss",
    "sll",
    "sdf",
    "sss",
    "pp",
    "155",
    "all",
    "pls",
)
print(tp.index("sss", 6, 10))  # 5


# funzione sorted():
numeri = (5, 36, 25, 85, 15, 45, 26, 18, 74, 15, 23, 45, 96, 24, 6, 84, 788, 542, 6365)
num = sorted(numeri)
print(num)

# U possiamo passare dei parametri alla funzione:
num = sorted(numeri, reverse=True)
print(num)

programming_languages = ("Rust", "Java", "Python", "C++", "Rust", "Python")
X = sorted(programming_languages, key=len)

print(X)
