myIntegerVar = 10
print(
    "integer", myIntegerVar
)  # Intero: numero intero senza decimali, ad esempio, 10o -5.

myFloatVar = 4.50
print("Float", myFloatVar)  # Float: un numero con un punto decimale, come 4.41o -0.4.

myStringVar = "Hello World!"
print(
    "Srting", myStringVar
)  # Stringa: una sequenza di caratteri racchiusa tra virgolette singole o doppie, ad esempio 'Hello world!'.

myBooleanVar = False
print("bool", myBooleanVar)  # Booleano: tipo vero o falso, scritto come Trueo False.

mySetVar = {
    5,
    6,
    1,
    2,
    4,
}  # Insieme: una raccolta non ordinata di elementi unici, come {4, 2, 0}.
print("Set", mySetVar)

my_dictionary_var = {
    "name": "Alice",
    "age": 25,
}  # Dizionario: una raccolta di coppie chiave-valore racchiuse tra parentesi graffe, come {'name': 'John Doe', 'age': 28}.
print("Dictionary:", my_dictionary_var)

myTuple = (
    1,
    2,
    3,
)  # Tupla: una raccolta ordinata e immutabile, racchiusa tra parentesi quadre, come (7, 8, 4).
print("Tuple:", myTuple)


my_range_var = range(
    5
)  # Intervallo: una sequenza di numeri, spesso utilizzata nei cicli, ad esempio range(5).
print("Range:", my_range_var)

my_list = [22, "hello world", 3.14, True]
print(
    "La mia lista int,string,float,bool", my_list
)  # Elenco: una raccolta ordinata di elementi che supporta diversi tipi di dati.

my_none_var = None
print(
    "None:", my_none_var
)  # Nessuno: un valore speciale che rappresenta l'assenza di un valore.

my_var_1 = "hello world"  # Per ottenere il tipo di dati di una variabile, è possibile utilizzare la type()funzione:
my_var_2 = 21
print(type(my_var_1))
print(type(my_var_2))

# _____________________________________________________________________________________________________

# La funzione integrata isinstance()consente di verificare se una variabile corrisponde a un tipo di dato
# specifico. Accetta un oggetto e il tipo di dato che si desidera confrontare, quindi restituisce un
#  valore booleano. Ecco alcuni esempi:

myIstance1 = isinstance("hello World", str)
myIstance2 = isinstance(True, bool)
myIstance3 = isinstance(42, int)
myIstance4 = isinstance("jon doe", int)

print(myIstance1, myIstance2, myIstance3, myIstance4)


# _______________________________________________________________________________________________________
# Cosa sono le stringhe e cos'è l'immutabilità delle stringhe?
# è possibile utilizzare entrambi i tipi di virgolette quando si lavora con le stringhe
my_str_1 = "hello "
my_str_2 = "World "

# Se hai bisogno di una stringa su più righe, puoi usare virgolette doppie triple o virgolette singole:
my_str3 = """ Multilinee 
string"""
my_var4 = """ another 
multilinee string"""

# Se la stringa contiene virgolette singole o doppie
msg = "it's a sunny day"
quote = 'she said "hallo world"'

# Per evitare le virgolette singole o doppie nella stringa, utilizzare una barra rovesciata ( \). Con questo metodo, è possibile utilizzare
# virgolette singole o doppie per racchiudere la stringa stessa:
msg = "it' a sunny day"
quote = 'she said,  "hallo world'


# A volte, potrebbe essere necessario verificare se
#  una stringa contiene uno o più caratteri. Per questo,
#  Python fornisce l' inoperatore , che restituisce un valore
#  booleano che specifica se il carattere o i caratteri sono presenti o meno nella stringa.

my_str = "hello world"
print("hello" in my_str)
print("hel" in my_str)
print("lo" in my_str)
print("world" in my_str)
print("minc" in my_str)


# Ora vediamo come ottenere la lunghezza di una stringa e come lavorare con i
#  singoli caratteri in essa contenuti, un processo chiamato indicizzazione .
# Per ottenere la lunghezza di una stringa,
#  è possibile utilizzare la funzione integrata len(). Ecco un esempio:
my_str = "hello world"
print(len(my_str))

# Ogni carattere in una stringa ha una posizione chiamata indice.
#  L'indice parte da zero, il che significa che l'indice del primo
# carattere di una stringa è 0, l'indice del secondo carattere è 1, e così via.
#  Per accedere a un carattere tramite il suo indice, si utilizzano
# parentesi quadre ( []) con l'indice del carattere a cui si desidera accedere al suo interno.
#  Ecco alcuni esempi:

my_str = "hello world"
print(my_str[0])
print(my_str[6])


# È consentita anche l'indicizzazione negativa,
#  quindi è possibile ottenere l'ultimo carattere di qualsiasi
#  stringa con -1, il penultimo carattere con -2, e così via:
my_str = "hello world"
print(my_str[-1])
print(my_str[-3])


# Le stringhe sono tipi di dati immutabili in Python.
# Ciò significa che è possibile riassegnare una stringa diversa a una variabile:

greeting = "hi"
greeting = "hello"
print(greeting)

greeting = "hi"
# greeting[0] = "H"  # TypeError: 'str' object does not support item assignment

"""In Python, è possibile combinare più stringhe con l' operatore ( + ).'
' Questo processo è chiamato concatenazione di stringhe .'
' Ecco come concatenare due stringhe con l'operatore più:"""

my_str_1 = "hello"
my_str_2 = "World"
str_plus_str = my_str_1 + "   " + "    " + my_str_2


"""
Ma tieni presente che questo funziona solo con le stringhe. 
Se provi a concatenare una stringa con un numero, otterrai TypeError:

"""
name = "John Doe"
age = 26

# name_and_age = name + age
# print(name_and_age) # TypeError: can only concatenate str (not "int") to str


"""
Questo accade perché Python non converte automaticamente altri tipi di dati,
 come gli interi, in stringhe quando li concatena. 
 ython richiede che tutti gli elementi siano stringhe prima di poterli concatenare. 
 Per risolvere questo problema, è possibile convertire il numero in una stringa con la str()funzione integrata,
che restituisce la rappresentazione in stringa dell'oggetto specificato senza modificare l'oggetto originale:
"""

name = "jhon Doe"
age = 26
name_and_age = name + str(age)
print(name_and_age)

"""
È anche possibile utilizzare l'operatore di assegnazione aumentato per la concatenazione.
Questo è rappresentato da un segno più e uguale ( +=) ed esegue sia la concatenazione che
l'assegnazione in un unico passaggio.
"""
name = "John Doe"
age = 26
name_and_age = name
name_and_age += str(age)

print(name_and_age)

"""
l processo di inserimento di variabili ed espressioni in una stringa è chiamato interpolazione di stringhe .
Python ha una categoria di stringhe chiamata f-string (abbreviazione di formatted string literals),
 che consente di gestire l'interpolazione con una sintassi compatta e leggibile.

Le stringhe F iniziano con f(minuscolo o maiuscolo) prima delle virgolette e consentono
di incorporare variabili o espressioni all'interno di campi di sostituzione indicati da
parentesi graffe ( {}). Ecco un esempio:

"""

name = "John Doe"
age = 26
name_and_age = f"my name is {name} and i am {age} years old"
print(name_and_age)
num1 = 5
num2 = 10
print(f"The sum of {num1} and {num2} is {num1 + num2}")  # The sum of 5 and 10 is 15


# Cos'è lo String Slicing e come funziona?
"""
In una lezione precedente, 
hai imparato come ogni carattere in una stringa può essere
identificato dal suo indice (a partire da zero) e come accedervi
utilizzando la notazione tra parentesi quadre:
"""
my_str = "hello world"
print(my_str[0])  # H
print(my_str[6])  # w
print(my_str[-1])  # d

# lo String Slicing  consente di estrarre una porzione di una stringa o di lavorare solo con una parte specifica.
# string[start:stop]
my_str = "Hello world"
print(my_str[1:4])  # ell
"""
Si noti che l' stopindice non è inclusivo, 
quindi [1:4]vengono estratti solo i caratteri dall'indice 1, 
fino al carattere all'indice , escluso 4.
"""

# upper(): Restituisce una nuova stringa con tutti i caratteri convertiti in maiuscolo.
uppercase_my_str = my_str.upper()
print(uppercase_my_str)
# lower(): Restituisce una nuova stringa con tutti i caratteri convertiti in minuscolo.
lowercase_my_str = my_str.lower()
print(lowercase_my_str)

"""
strip(): Restituisce una nuova stringa con i caratteri iniziali e finali 
specificati rimossi. Se non viene passato alcun argomento,
rimuove gli spazi iniziali e finali.
"""
my_str = ". hello world ."
trimmed_my_str = my_str.strip(".")  # con argomento da eliminare
trimmed_my_str = my_str.strip()  # senza argomento
print(trimmed_my_str)


"""
replace(old, new): Restituisce una nuova stringa
 con tutte le occorrenze di old sostituite da new.

"""
my_str = "hello world"
replace_my_str = my_str.replace("hello", "world")
print(replace_my_str)


"""
split(separator): Divide una stringa in base a un separatore
 specificato in un elenco di stringhe.
   Se non viene specificato alcun separatore,
     la divisione avviene in base agli spazi vuoti.
"""
my_str = " hello world "
my_str5 = " hello world , aaaaaaa"
split_word = my_str.split()  # trasforma la stringa in una lista
split_word1 = my_str5.split(",")  # indicando il punto di taglio
print(split_word)
print(split_word1)

"""
join(iterable): Unisce gli elementi di un iterabile in una stringa con un separatore.

"""
my_list = ["hello", "world"]
joined_my_str = " ".join(my_list)
print(joined_my_str)


"""
startswith(prefix): Restituisce un valore booleano che indica se una
 stringa inizia con il prefisso specificato.

"""
my_str = "hello world"
starts_with_hello = my_str.startswith("hello")
print(starts_with_hello)


"""
endswith(suffix): Restituisce un valore booleano che indica 
se una stringa termina con il suffisso specificato.

"""
my_str = "hello world"
end_with_words = my_str.endswith("world")
print(end_with_words)


"""
ind(substring): Restituisce l'indice della prima occorrenza di substring,
oppure -1se non ne trova una.

"""
my_str = "hello world"
world_index = my_str.find("world")
print(world_index)  # 6


"""
count(substring): Restituisce il numero di volte in cui una
 sottostringa appare in una stringa.
"""
my_str = "hello world"
o_count = my_str.count("o")
print(o_count)

"""
capitalize(): Restituisce una nuova stringa con il primo carattere
 in maiuscolo e gli altri caratteri in minuscolo.
"""

my_str = "hello word"
capitalized_my_str = my_str.capitalize()
print(capitalized_my_str)


"""
isupper(): Restituisce True se tutte 
le lettere nella stringa sono maiuscole e False in caso contrario.
"""
my_str = "hello word"
is_all_lower = my_str.islower()
print(is_all_lower)


"""
title(): Restituisce una nuova stringa con la prima lettera
 di ogni parola in maiuscolo.
"""
my_str = "hello word"
title_case_my_str = my_str.title()
print(title_case_my_str)


# ome si lavora con i numeri interi e i numeri in virgola mobile?
"""
Interi e float sono i principali tipi di dati numerici in Python.
 Con essi è possibile memorizzare dati numerici ed eseguire operazioni matematiche.
Diamo un'occhiata a cosa sono i numeri interi e i numeri in virgola mobile, 
come eseguire calcoli aritmetici con essi e ai diversi metodi forniti da Python per lavorare con entrambi.
"""

# Gli interi sono numeri interi senza punti decimali, positivi o negativi:
myInt1 = 56
myInt2 = -4
print(myInt1)
print(myInt2)

# Ecco come eseguire un'operazione di addizione con numeri interi:
myInt1 = 56
myInt2 = 12
sumInts = myInt1 + myInt2
print("integer addizione:", sumInts)

# Ecco come eseguire una sottrazione con numeri interi:
myInt1 = 56
myInt2 = 12
diffInts = myInt1 - myInt2
print(diffInts)

# Ecco come eseguire un'operazione di moltiplicazione con numeri interi:
myInt1 = 12
myInt2 = 4
productInts = myInt1 * myInt2
print(productInts)


# Ed ecco come eseguire un'operazione di divisione con numeri interi:
myInt1 = 56
myInt2 = 12
divInts = myInt1 / myInt2
print("divisione Intera:", divInts)


# I numeri in virgola mobile sono numeri positivi o negativi con punti decimali, come 3.14, -0.5, o 0.0.
myFloat1 = -12.0
myFloat2 = 4.9
print(type(myFloat1))
print(type(myFloat2))


# Ecco un'operazione di addizione con i numeri in virgola mobile:
myFloat1 = 5.4
myFloat2 = 12.0
floatAddition = myFloat1 + myFloat2
print(floatAddition)


# Ecco un'operazione di sottrazione con numeri in virgola mobile:
myFloat1 = 5.4
myFloat2 = 12.0
floatSubtraction = myFloat2 - myFloat1
print("sottrazione float:", floatSubtraction)

# Ecco un'operazione di moltiplicazione con i numeri in virgola mobile:
myFloat1 = 5.4
myFloat2 = 12.0
floatMoltiplication = myFloat1 * myFloat2
print("moltiplicazioneFloat :", floatMoltiplication)

# Ed ecco un'operazione di divisione con numeri in virgola mobile:

myFloat1 = 5.4
myFloat2 = 12.0
floatDivision = myFloat2 / myFloat1
print("divisione float:", floatDivision)

# Se si aggiunge un numero intero e un numero float,
# il risultato viene automaticamente convertito in un numero float:
myInt = 56
myFloat = 5.4
sumIntAndFloat = myInt + myFloat
print(sumIntAndFloat)
print(type(sumIntAndFloat))


# Questo vale anche per altre operazioni aritmetiche di base, come sottrazione, moltiplicazione e divisione. Se si combinano numeri interi e numeri in virgola mobile,
# ython restituirà un numero in virgola mobile come risultato.
#
# È anche possibile eseguire calcoli aritmetici più complessi,
# come ottenere il resto di due numeri con l'operatore modulo,
# la divisione intera e l'elevamento a potenza,
# sia con numeri interi che con numeri in virgola mobile.

# L'operatore modulo ( %) restituisce il resto
# quando il valore a sinistra viene diviso per il valore a destra:

myInt1 = 56
myInt2 = 12

myFloat1 = 5.4
myFloat2 = 12.0

modInts = myInt1 % myInt2
modFloats = myFloat1 % myFloat2

print("Modulo intero:", modInts)
print("modiulo float:", modFloats)


# La divisione intera divide due numeri e restituisce il più grande intero minore o
# uguale al risultato.
# Questo si ottiene con l'operatore di doppia barra ( // ):

myInt_1 = 56
myInt_2 = 12

myFloat_1 = 5.4
myFloat_2 = 12.0

floorDivInt = myInt1 // myInt2
floorDivFloat = myFloat2 // myFloat1

print("Integer Floor Division:", floorDivInt)  # Integer Floor Division: 4
print("Float Floor Division:", floorDivFloat)  # Float Floor Division: 2.0


# L'elevamento a potenza eleva un numero alla potenza di un
# altro e si esegue con l'operatore asterisco doppio ( **):
myInt_1 = 56
myInt_2 = 12

myFloat_1 = 5.4
myFloat_2 = 12.0

expInt = myInt1**myInt2
expFloat = myFloat1**myFloat2

print(expInt)
print(expFloat)


# La float()funzione restituisce un numero in
# virgola mobile costruito a partire dal numero specificato:

myInt1 = 56
myFloat1 = float(myInt1)

print(myFloat1)
print(type(myFloat1))


# La int()funzione restituisce un numero intero costruito a
# partire dal numero dato:
myFloat = 12.92563
myInt = int(myFloat)

print(myInt)
print(type(myInt))


# Inoltre, è possibile utilizzare le stesse funzioni integrate per
# convertire una stringa in un numero float o intero:
myStrInt = "45"
myStrFloat = "7.8"

convertedInt = int(myStrInt)
convertedFloat = float(myStrFloat)

print(convertedInt, type(convertedInt))
print(convertedFloat, type(convertedFloat))


# Ecco alcuni altri metodi forniti da Python per lavorare
# con numeri interi e numeri in virgola mobile.


# round(): Arrotonda un numero al numero di cifre decimali specificato.
# Per impostazione predefinita, questa funzione arrotonda all'intero più vicino e
# restituisce un numero intero senza cifre decimali:

myInt1 = 4.798
myInt2 = 4.253

roundedInt1 = round(myInt1)
roundedInt2 = round(myInt2)

print(roundedInt1, "", roundedInt2)


# abs(): restituisce il valore assoluto di un numero,
num = -15
absoluteValue = abs(num)
print(absoluteValue)


# abs(): restituisce il valore assoluto di un numero,
result1 = pow(2, 3)
print(result1)

result2 = pow(2, 3, 5)
print(result2)


# Come funzionano gli incarichi aumentati?

# L'assegnazione aumentata combina un'operazione binaria con un'assegnazione in un unico passaggio.
# Prende una variabile,
# le applica un'operazione con un altro valore e memorizza il risultato nella stessa variabile.

"""
Se hai familiarità con un linguaggio come JavaScript, 
probabilmente avrai sentito parlare dell'operatore di assegnazione di addizione ( +=) 
o di assegnazione di sottrazione ( -=), e di altri. Questi esistono anche in Python. 
L'unica differenza è che vengono chiamati assegnazioni aumentate .
"""

# La sintassi di base di un'assegnazione aumentata è la seguente:

#  variable <operator>= value
# Qual è il modo più efficiente per farlo:
# variable = variable <operator> value

myVar = 10
myVar += 5
# myVar è uguale a myVar+5
print(myVar)

# Ed ecco la stessa cosa, ma senza assegnazione aumentata:
my_var = 10
my_var = my_var + 5

print(my_var)  # 15


# Il vantaggio dell'assegnazione aumentata è che fornisce un modo conciso
# e leggibile per aggiornare il valore di una variabile senza ripeterne il nome.
# A sua volta, questo riduce la ridondanza e i potenziali errori che potrebbero derivare
# da un errore di battitura o simili.

# Ogni operatore può utilizzare un'assegnazione aumentata.
# Abbiamo esaminato l'operatore di assegnazione di addizione ( +=),
# quindi diamo un'occhiata agli altri.

# L'operatore di assegnazione di sottrazione ( -=) sottrae l'operando di destra
#  dalla variabile di sinistra e
# memorizza la differenza nella variabile di sinistra:

count = 14
count -= 3
print(count)  # 11


# L'operatore di assegnazione della moltiplicazione ( *=) moltiplica
# la variabile di sinistra per l'operando di
# destra e memorizza il prodotto nella variabile di sinistra:

product = 65
product *= 7
print(product)  # 455


# L'operatore di assegnazione della divisione ( /=) divide la variabile di sinistra per
# quella di destra e memorizza il risultato nella variabile di sinistra:

price = 100
price /= 4
print(price)

# L'operatore di divisione per intero ( //=) divide la
# variabile di sinistra per quella di destra e
# memorizza il risultato nella variabile di sinistra:

totalPages = 23
totalPages //= 5
print(totalPages)


# L'operatore di assegnazione del modulo ( %=) calcola il resto
#  della variabile sinistra diviso per quella
# destra e lo memorizza nuovamente nella variabile sinistra:

bits = 35
bits %= 2
print(bits)


# L'operatore di assegnazione di potenza ( **=) eleva la variabile di sinistra alla
# potenza di destra e memorizza il risultato nella variabile di sinistra:

power = 2
power **= 3
print(power)


# È possibile utilizzare anche alcuni operatori di assegnazione avanzati con le stringhe.
# Ad esempio,
# l'operatore di assegnazione di addizione semplifica la concatenazione delle stringhe:

greet = "hallo"
greet += " world"
print(greet)

# E l'operatore di assegnazione della moltiplicazione può essere utilizzato per ripetere una stringa:
greet = "hello "
greet *= 3
print(greet)


# Altre assegnazioni aumentate generano un errore
# ypeErrorquando vengono utilizzate con le stringhe:

"""
greet = 'Hello'
greet -= ' World'

print(greet) # TypeError: unsupported operand type(s) for -=: 'str' and 'str'


greet = 'Hello'
greet /= 'World'

print(greet) # TypeError: unsupported operand type(s) for /=: 'str' and 'str' 

"""


"""

Se vi state chiedendo se gli operatori di incremento e 
decremento ( ++e  --) funzionano in Python, 
sappiate che non funzionano. 
Questo perché Python evita deliberatamente 
le scorciatoie di incremento e decremento in stile C 
per mantenere il linguaggio chiaro ed esplicito.

Invece di x++, puoi semplicemente scrivere x += 1,
il che rende ovvio che stai incrementando il valore di xdi 1.

"""

# Scrivendo ++x in Python si applica semplicemente l'unario più due volte,
# senza incrementare nulla:

my_var = 5

print(+my_var)  # 5
print(++my_var)  # 5
print(+++my_var)  # 5

my_var += 1

print(my_var)  # 6


# Come funzionano le istruzioni condizionali e gli operatori logici?
"""

Le istruzioni condizionali, o condizionali, consentono di controllare il flusso del programma in base al fatto che determinate condizioni siano vere o false.

Ma prima di addentrarci in questo argomento, ripassiamo gli elementi fondamentali delle istruzioni condizionali, iniziando dagli operatori di confronto. Gli operatori di confronto sono operatori che consentono di confrontare due o più valori e restituire un valore booleano.

In una lezione precedente hai imparato che i valori booleani sono uno dei tipi di dati in Python e possono essere solo Trueo False.

Ecco una tabella con gli operatori di confronto in Python:


Operatore	Nome	Descrizione
==	Pari	Controlla se due valori sono uguali
!=	Non uguale	Controlla se due valori non sono uguali
>	Maggiore di	Controlla se il valore a sinistra è maggiore del valore a destra
<	Meno di	Controlla se il valore a sinistra è inferiore al valore a destra
>=	Maggiore o uguale	Controlla se il valore a sinistra è maggiore o uguale al valore a destra
<=	Minore o uguale	Controlla se il valore a sinistra è minore o uguale al valore a destra

"""
# Ecco alcune di quelle espressioni che restituiscono Trueo False:
print(3 > 4)  # False
print(3 < 4)  # True
print(3 == 4)  # False
print(4 == 4)  # True
print(3 != 4)  # True
print(3 >= 4)  # False
print(3 <= 4)  # True

"""
Questi operatori possono essere utilizzati nelle istruzioni
condizionali per confrontare valori ed eseguire un determinato codice a 
seconda che la valutazione della condizione sia Trueo False.
"""

# In Python, la condizione più elementare è l' ifistruzione.
# Ecco la sintassi di base:

condition = False
if condition:
    pass  # Code to execute if condition is True

"""
if le affermazioni iniziano con la ifparola chiave.

conditionè un'espressione che restituisce Trueo False, seguito da due punti ( :).

Il corpo dell'istruzione ifcostituisce un blocco di codice , ovvero un gruppo di istruzioni collegate tra loro. In Python, 
il livello di indentazione è ciò che definisce un blocco di codice.
"""

"""
Nell'esempio precedente, il corpo dell'istruzione if contiene pass 
un'istruzione. Quando passun'istruzione viene eseguita,
 non accade nulla. Questa è una parola chiave speciale
che può essere utilizzata come segnaposto per il codice futuro 
ed è utile quando non sono ammessi blocchi di codice vuoti.

"""

# Il codice nel corpo dell'istruzione ifviene eseguito
# solo quando la condizione viene valutata come True. Ad esempio:

age = 18
if age >= 18:
    print("you are adult")

"""
Nota l'indentazione prima di print('You are an adult'). 
Mentre altri linguaggi di programmazione usano caratteri come le 
parentesi graffe per definire i blocchi di codice e sfruttano 
l'indentazione solo per migliorare la leggibilità, 
in Python i blocchi di codice sono determinati dall'indentazione.
"""
"""
Il seguente codice genererebbe un'eccezione IndentationError, 
che è il modo in cui Python segnala che è necessaria 
un'indentazione in un determinato punto del codice:

age = 18

if age >= 18:
print('You are an adult') # IndentationError: expected an indented block after 'if' statement on line 3

"""

"""
Sebbene sia possibile utilizzare qualsiasi numero di spazi
(purché si sia coerenti) per determinare ogni livello di rientro, 
la guida di stile Python consiglia di utilizzare quattro spazi.

I blocchi si trovano anche nei cicli e nelle funzioni, 
di cui parleremo nelle lezioni future.

"""

# Tornando al nostro esempio, se ageè inferiore a 18,
# non viene stampato nulla nel terminale:

age = 12

if age >= 18:
    print("You are an adult")  # Nothing shows up in the terminal

# Ma cosa succede se si vuole anche stampare qualcosa
# se ageè minore di 18? È qui che elseentra in gioco la clausola.
# La elseclausola viene eseguita quando la ifcondizione è falsa.
# Ecco la sintassi di if…elseun'istruzione:

if condition:
    pass  # Code to execute if condition is True
else:
    pass  # Code to execute if condition is False

age = 12
if age >= 18:
    print("sei maggiorenne")
else:
    print("non sei maggiorenne")


# Potrebbero esserci situazioni in cui si desidera tenere
# conto di più condizioni. Per farlo, Python consente di estendere
# l'istruzione if con la elif parola chiave (else if).

condition1 = True
condition2 = True

if condition:
    pass
elif condition2:
    pass

age = 12
if age >= 18:
    print("sei maggiorenne")
elif age >= 13:
    print("sei un giovanotto")
else:
    print("sei troppo piccolo")


# Tieni presente che puoi utilizzare tutte elifle istruzioni che desideri:
age = 2

if age >= 65:
    print("You are a senior citizen")
elif age >= 30:
    print("You are an adult in your prime")
elif age >= 18:
    print("You are a young adult")
elif age >= 13:
    print("You are a teenager")
elif age >= 3:
    print("You are a young child")
else:
    print("You are a toddler or an infant")  # You are a toddler or an infant

    """
    Ora che hai capito come funzionano gli operatori di confronto
    e le istruzioni condizionali in Python, puoi iniziare
    a scrivere programmi che prendono decisioni basate sulla 
    logica e sull'input. Che tu stia confrontando valori o 
    eseguendo branching attraverso più condizioni, 
    questi strumenti sono la base per scrivere codice flessibile e reattivo.
    
    """


"""
Cosa sono i valori veri e falsi e come funzionano gli operatori booleani 
e i cortocircuiti?
Nella lezione precedente hai imparato come utilizzare gli operatori 
di confronto e le istruzioni condizionali per controllare il 
flusso dei tuoi programmi.

Sebbene siano molto potenti, spesso ci si imbatte in situazioni 
in cui è necessario confrontare più valori contemporaneamente.
Questo può portare 
a istruzioni condizionali annidate, ad esempio:

"""

isCytizen = True
age = 25

if isCytizen:
    if age >= 18:
        print("puoi andare a votare")
else:
    print("non puoi andare a votare")


"""
L'esempio precedente verificherà innanzitutto se is_citizenè True.
In tal caso, passerà all'istruzione annidata ife verificherà
se ageè maggiore o uguale a 18. Poiché ageè maggiore o uguale a 18,
il messaggio stampato sul terminale sarà You are eligible to vote.
Se is_citizenfosse False, il messaggio stampato sul terminale
sarebbe stato You are not eligible to vote.
"""

# Se si lavora con istruzioni condizionali più complesse,
# è possibile utilizzare gli operatori and, ore di Python not.

# Ma prima di addentrarci in questi operatori, diamo un'occhiata a cosa sono
# i valori veritieri(truthy) e falsi(Falsy).

"""
In Python, ogni valore ha un valore booleano intrinseco,
ovvero un'indicazione intrinseca che indica se debba essere 
trattato come Trueo Falsein un contesto logico. 
Molti valori sono considerati veritieri , 
ovvero restituiscono σ Truein un contesto logico. 
Altri sono falsi , ovvero restituiscono σ False.


Ecco alcuni valori falsi:

None
False
Integer 0
Float 0.0
Empty strings ""

Altri valori,
come i numeri diversi da zero e le stringhe non vuote, sono veritieri.

Per verificare se un valore è vero o falso, 
è possibile utilizzare la funzione integrata bool(). 
Converte esplicitamente un valore nel suo equivalente booleano e
restituisce True sia per i valori veritieri che False per quelli falsi. 
Ecco alcuni esempi:

"""

print(bool(False))  # False
print(bool(0))  # False
print(bool(""))  # False

print(bool(True))  # True
print(bool(1))  # True
print(bool("Hello"))  # True


"""
Ora che abbiamo compreso i valori veri e falsi, 
possiamo dare un'occhiata agli operatori booleani, 
noti anche come operatori logici o operatori booleani. 
Si tratta di operatori speciali che consentono di 
combinare più espressioni per creare una logica 
decisionale più complessa nel codice.

In Python ci sono tre operatori booleani: and, or, e not.

Diamo prima un'occhiata all'operatore and.

L' andoperatore accetta due operandi e restituisce il primo se è falso, altrimenti restituisce il secondo. Entrambi gli operandi devono essere veritieri affinché un'espressione restituisca un valore veritiero.

Ecco un esempio:
"""

isCitizen = True
age = 25

print(isCitizen and age)  # se true print age

"""
Nell'esempio precedente, il numero 25 viene visualizzato
sul terminale perché l' andoperatore valuterà il secondo
operando se il primo è True. 
L' andoperatore è noto come operatore di cortocircuito. Il cortocircuito significa che Python controlla i valori da sinistra a destra 
e si ferma non appena determina il risultato finale.
"""


"""
Spesso si utilizzano le istruzioni andwithin ifper
verificare se sono soddisfatte più condizioni. 
Ecco come è possibile riorganizzare l'esempio precedente per utilizzare l' 
andoperatore al posto ifdelle istruzioni annidate:
"""

isCitizen = True
age = 19

if isCitizen and age >= 18:
    print("puoi votare")
else:
    print("non puoi votare")


# Nell'esempio precedente, is_citizenè True, e age >= 18viene valutato come True.
# Poiché entrambi gli operandi dell'operatore andsono veritieri,
# la condizione is_citizen and age >= 18viene valutata come True,
# e la printchiamata nel ifblocco viene eseguita.


""" A and B

Valuta A come booleano

Se A è falso → ritorna A

Se A è vero → ritorna B


A or B

Valuta A come booleano

Se A è vero → ritorna A

Se A è falso → ritorna B


"""

# Ora diamo un'occhiata all'operatore or.
# Questo operatore restituisce il primo operando se è veritiero,
# altrimenti restituisce il secondo operando.
# Un'espressione orrestituisce un valore veritiero se almeno un operando è veritiero.
# L' oroperatore è anche noto come operatore di cortocircuito.
# Ecco un esempio:

age = 19
isEmpliyed = False
print(age or isEmpliyed)
# Il codice seguente stamperà il numero 19 perché il primo operando ageè True.


# Se devi verificare se una o più espressioni sono True,
# puoi usare l' oroperatore in una condizione come questa:

age = 19
isStudent = True
if age > 18 or isStudent:
    print("You are eligible for a student discount")
else:
    print("You are not eligible for a student discount")
# In questo caso, age < 18è False, ma is_studentè True.
# Poiché almeno una condizione è vera, l'intera orespressione viene valutata come ,
# e viene stampato True il messaggio di sconto nel blocco.if


"""
L'ultimo operatore che esamineremo è l' notoperatore che accetta 
un singolo operando e ne inverte il valore booleano. 
Converte i valori veritieri in Falsee quelli falsi in True. 
A differenza degli operatori precedenti che abbiamo esaminato, 
notrestituisce sempre Trueor False.

"""

print(not "")  # True, because empty string is falsy
print(not "Hello")  # False, because non-empty string is truthy
print(not 0)  # True, because 0 is falsy
print(not 1)  # False, because 1 is truthy
print(not False)  # True, because False is falsy
print(not True)  # False, because True is truthy


# È comune utilizzare l' notoperatore nelle istruzioni condizionali per
# verificare se qualcosa non è Trueo False, in questo modo:
isAdmin = False
if not isAdmin:  # è vero che non è vero!
    print("Accss denied")
else:
    print("welcome administrator")
# Poiché is_admin è falso, la sua negazione (not is_admin) è vera;
#  quindi la condizione risulta vera e viene stampato il messaggio
#  “Access denied for non-administrators.”

"""
Ora che hai compreso i valori truthy e falsy, 
il funzionamento degli operatori and, or e not, 
e la valutazione a corto circuito (short-circuiting), puoi scrivere una logica 
condizionale più flessibile e leggibile.
"""


#  Come funzionano le funzioni in Python?
"""

Le funzioni sono porzioni di codice riutilizzabili 
che vengono eseguite quando vengono chiamate. 
Molti linguaggi di programmazione sono dotati di 
funzioni integrate che semplificano l'avvio. Python 
non fa eccezione e abbiamo già trattato alcune 
funzioni integrate come print()nelle lezioni precedenti.

Un'altra utile funzione integrata è input(), 
che consente di chiedere all'utente un input:
"""

# name = input("come ti chiami?")
# print("ciao", name)

# D'altra parte, int()converte un numero, un valore booleano e
# una stringa numerica in un intero:
print(int(3.14))  # 3
print(int("42"))  # 42
print(int(True))  # 1
print(int(False))  # 0


"""
È anche possibile scrivere funzioni personalizzate. 
Per farlo, si utilizza la defparola chiave, 
seguita dal nome che si desidera dare alla funzione, 
da una coppia di parentesi e da due punti. 
Quindi, su una nuova riga, si scrive il codice che la funzione deve eseguire. 
Il codice eseguito dalla funzione è anche detto corpo della funzione.
"""


# Ecco un esempio di una funzione personalizzata
# denominata helloche stampa la stringa Hello Worldsul terminale:
def hello():
    print("hello world")


# Per eseguire la funzione, è necessario chiamarla con il suo
# nome seguito da una coppia di parentesi:
hello()

"""
Notate l'indentazione prima di print('Hello World'). Come ricorderete dalle lezioni precedenti, Python si basa sull'indentazione per determinare quali gruppi di istruzioni appartengono insieme. 
Questi gruppi di istruzioni sono chiamati blocchi di codice.
"""


# Ecco un'altra semplice funzione che stampa la somma di due numeri sul terminale:
def calcoloSomma(a, b):
    print(a + b)


"""
Come puoi vedere, la nostra funzione, calculate_sum, ha ae btra parentesi, separati da una virgola. Questi sono chiamati parametri. Pensa ai parametri come variabili segnaposto che fungono da "slot" per i valori che passi alle funzioni quando le chiami.

Per utilizzare i parametri, è necessario passare degli "argomenti". Gli argomenti sono i valori che si passano a una funzione quando la si chiama.

Ecco come chiamare la calculate_sumfunzione per sommare i numeri 3e 1:

"""

calcoloSomma(5, 1)

# Se si chiama la funzione senza il numero corretto di argomenti, si otterrà TypeError:

# Le funzioni utilizzano anche una parola chiave speciale returnper uscire dalla funzione e restituire un valore. Se non si utilizza esplicitamente return,
# Python restituirà Noneper impostazione predefinita.


def calcoloSomma(a, b):
    print(a + b)


mySomma = calcoloSomma(5, 10)
print(mySomma)


# Come puoi vedere, la calculate_sumfunzione stampa la somma di ae b,
#  ma non restituisce nulla in modo esplicito.
# Quindi, quando assegniamo il risultato a my_sum,
# il valore in realtà è None. Per risolvere il problema,
# puoi usare la returnparola chiave per restituire il risultato:


def calcoloSomma(a, b):
    print(a + b)
    return a + b


mySomma = calcoloSomma(5, 10)
print(mySomma)

# Ora calculate_sumrestituisce la somma di ae b, che viene memorizzata in mySomma.
