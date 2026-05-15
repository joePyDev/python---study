""" 
Esercizio 1 

Scrivi un programma che usi input per chiedere all’utente il proprio
nome e poi dia loro il benvenuto

Enter your name: Chuck
Hello Chuck



name = input(str("Enter your name:"))
print(f"Hello {name}")


"""


"""
Esercizio 2

Scrivi un programma per richiedere all’utente ore di lavoro e tariffe
orarie per calcolare la retribuzione lorda.

Enter Hours: 35
Enter Rate: 2.75
Pay: 96.25


hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
pay = float(hours) * float(rate)
print(f"\nEnter Hours: {hours}\nEnter Rate: {rate}\nPay: {pay:.2f}")

"""




"""
Esercizio 3

Scrivi un programma che, richiesta all’utente una temperatura in
gradi Celsius, la converta in Fahrenheit e poi la visualizzi.






celsius_imp = input("Inserisci i gradi Celsius: ")

def celsius_in_fahrenheit(celsius):
    try:
        # Conversione immediata
        celsius = float(celsius)
        fahrenheit = celsius * 1.8 + 32
        
        # Usiamo il Format Specifier direttamente nel return
        return f"Fahrenheit: {fahrenheit:.2f}"
        
    except ValueError:
        # Specificare il tipo di errore (ValueError) è più professionale
        return "Errore: inserisci un valore numerico valido."

A = celsius_in_fahrenheit(celsius_imp)
print(A)


"""






"""
Esercizio 4

Riscrivi lo script del calcolo della retribuzione per attribuire ad un
dipendente una maggiorazione oraria di 1,5 volte, per le ore di lavoro straordinario
fatte oltre le 40.
Enter Hours: 45
Enter Rate: 10
Pay: 475.0



ore_lavorate = float(input("Enter Hours: "))
paga_oraria = float(input("Enter Rate: "))

if ore_lavorate > 40:
    ore_ordinarie = 40 
    ore_straordinarie = ore_lavorate - 40
    retribuzione = (ore_ordinarie * paga_oraria) + (ore_straordinarie * (paga_oraria*1.5) )
else:
    retribuzione = ore_lavorate * paga_oraria
print(f"Ore lavorate: {ore_lavorate}\nPaga oraria: {paga_oraria}\nRetribuzione: {retribuzione:.2f}")


"""


"""
Esercizio 5

 Riscrivi lo script sul calcolo della retribuzione utilizzando try e
except in modo che il programma gestisca input non-numerici in maniera elegante
visualizzando un messaggio prima di uscire dal programma. Di seguito vengono
mostrate due esecuzioni del programma:
Enter Hours: 20
Enter Rate: nine
Error, please enter numeric input
Enter Hours: forty
Error, please enter numeric input



import sys

try:
    ore_lavorate = float(input("Enter Hours: "))
    paga_oraria = float(input("Enter Rate: "))
    
except ValueError:
    print("Error, please enter numeric input")
    sys.exit()

if ore_lavorate > 40:
    ore_ordinarie = 40 
    ore_straordinarie = ore_lavorate - 40
    retribuzione = (ore_ordinarie * paga_oraria) + (ore_straordinarie * (paga_oraria*1.5) )
else:
    retribuzione = ore_lavorate * paga_oraria
    
print(f"Ore lavorate: {ore_lavorate}\nPaga oraria: {paga_oraria}\nRetribuzione: {retribuzione:.2f}")

"""



"""
Esercizio 6

 Scrivi un programma per richiedere un valore compreso tra 0.0 e 1.0.
Se non è compreso nell’intervallo specificato, visualizza un messaggio di errore. Se
è compreso tra 0,0 e 1,0, visualizza un giudizio utilizzando la seguente tabella:
Score Grade
>= 0.9
A
>= 0.8
>= 0.7
>= 0.6
< 0.6
B
C
D
F
Enter score: 0.95
A
Enter score: perfect
Bad score
Enter score: 10.0
Bad score
Enter score: 0.75
C
Enter score: 0.5
F
Esegui varie volte il programma per testarlo con diversi valori di input.




import sys

try:
    my_val = float(input("Enter Score: "))
except ValueError:
    print("Bad score")
    sys.exit()
    
if my_val >= 0.0 and my_val <= 1.0:
    if my_val >= 0.9:
        grade = "A"
    elif my_val >= 0.8:
        grade = "B"
    elif my_val >= 0.7:
        grade = "C"
    elif my_val >= 0.6:
        grade = "D"
    else:
        grade = "F"
    
    print(grade)
else:
    print("Bad score")
    

"""



"""
Esercizio 7

6: Riscrivi il calcolo della tua retribuzione con gli straordinari pagati il
50%in più creando una funzione chiamata computepay che richieda i due parametri
hours e rate.
Enter Hours: 45
Enter Rate: 10
Pay: 475.0




import sys

def computepay(ore_lavorate , paga_oraria):
     #calcolo ore lavorate,retribuzione e straordinari
     #ritorna il totale retribuzione compreso straordinari
    
    if ore_lavorate > 40:
        ore_ordinarie = 40 
        ore_straordinarie = ore_lavorate - 40
        retribuzione = (ore_ordinarie * paga_oraria) + (ore_straordinarie * (paga_oraria*1.5) )
    else:
        retribuzione = ore_lavorate * paga_oraria
        
    return retribuzione




try:
    ore_lavorate = float(input("Enter Hours: "))
    paga_oraria = float(input("Enter Rate: "))
    
except ValueError:
    print("Error, please enter numeric input")
    sys.exit()

ret = computepay(ore_lavorate, paga_oraria)

print(ret)


"""






"""
Esercizio 8

Riscrivi lo script del capitolo precedente creando una funzione chia
mata computegrade che accetta un punteggio come parametro e restituisce un
voto sotto forma di stringa.





    
def computegrade(my_val):
    if my_val >= 0.0 and my_val <= 1.0:
        if my_val >= 0.9:
            grade = "A"
        elif my_val >= 0.8:
            grade = "B"
        elif my_val >= 0.7:
            grade = "C"
        elif my_val >= 0.6:
            grade = "D"
        else:
            grade = "F"
        return grade
    else:
        bad_score = ("Bad score")
        return bad_score




import sys

try:
    my_val = float(input("Enter Score: "))
except ValueError:
    print("Bad score")
    sys.exit()

X = computegrade(my_val)

print(X)



"""



"""
esercizio 9 

Scrivi un programma che legga ripetutamente i numeri fino a quando
l’utente non digiti “finito”. Una volta che viene digitato “finito”, dovrà essere
visualizzato il totale, il conteggio e la media dei numeri. Se l’utente dovesse digitare
qualcosa di diverso da un numero, occorrerà rilevare l’errore usando try e except,
visualizzare un messaggio di errore e passare al numero successivo.



import sys
contatore = 0
somma_numeri_inseriti = 0

while True:
    try:
        numeri_inseriti = input("Inserisci un numero da 1 a 10")
        if numeri_inseriti == "finito": break
        contatore += 1
        somma_numeri_inseriti = somma_numeri_inseriti + float(numeri_inseriti)
    except ValueError:
         print("input errato")
         sys.exit()
         
print(somma_numeri_inseriti)
print(contatore)
print(somma_numeri_inseriti / contatore)


"""

"""
esercizio 10

 Scrivi un altro programma che richieda un elenco di numeri come
nell’esercizio precedente e alla fine visualizzi sia il valore più grande sia quello più
piccolo.


import sys

numero_piu_piccolo = None
numero_piu_grande = None

while True:
    try:
        numero_inserito = input("inserisci un numero >>> ")
        if numero_inserito == "finito": break
        numero_inserito = int(numero_inserito)
    except ValueError:
        print("inserisci un numero valido")
        sys.exit()
        
    if numero_piu_grande == None or  numero_inserito > numero_piu_grande :
        numero_piu_grande = numero_inserito    
        
    if numero_piu_piccolo == None or numero_inserito < numero_piu_piccolo :
        numero_piu_piccolo = numero_inserito
        
    
print(f"numero piu grande {numero_piu_grande}")        
print(f"numero piu piccolo {numero_piu_piccolo}")
        
        
"""




"""
esercizio 11
Scrivi un ciclo while che inizi dall’ultimo carattere della stringa e
proceda fino al primo carattere della stringa, visualizzando ogni lettera su una riga
separata, tranne che all’indietro.



my_string = "stringa"
indice = len(my_string)-1

while indice >= 0:
    lettera = my_string[indice]
    print(lettera)
    indice -= 1

"""




"""
esercizio 12

Incorpora questo codice in una funzione chiamata “count” e rendila
in grado di accettare stringhe e lettere come argomenti.

word = 'banana'
count = 0
for letter in word:
if letter == 'a':
count = count + 1
print(count)


def count(parola,let):
    count = 0
    if isinstance(parola, str):
        for lettera in parola:
            if lettera == let:
                count += 1
    else:
        print("la funzione accetta solo stringhe")    
    
    print(f"la parola {let} è stata trovata {count} volte")
    
    return  count 


count("sono una frase" , "s")





esercizio 13
esiste un metodo per le stringhe chiamato count simile alla funzione
dell’esercizio precedente.
Leggi la documentazione di questo metodo su https://docs.python.org/3.5/librar
y/stdtypes.html#string-methods e scrivi uno script che conti il numero di volte in
cui la lettera a appare nella stringa “banana”.

stringa = "banana"
lettera = stringa.count("a")
print(lettera)

"""




r"""


esercizio 14

 prendi il seguente codice Python contenente una stringa: str =
'X-DSPAM-Confidence:0.8475
Usa find e la segmentazione delle stringhe per estrarre la porzione di stringa dopo
il carattere “:” e utilizza la funzione float per convertire la stringa estratta in un
numero a virgola mobile.


stringa = "X-DSPAM-Confidence:0.8475"

inizio_segmentazione = stringa.find(":")

parte_estratta = stringa[inizio_segmentazione+1:]
float_parte_estratta = float(parte_estratta)


print(float_parte_estratta)







esercizio 15


 Scrivi un programma per leggere un file e visualizzarne il contenuto
(riga per riga) tutto in maiuscolo. L’esecuzione del programma avrà questo aspetto:
python shout.py
Enter a file name: mbox-short.txt
FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN 5 09:14:16 2008
RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>
RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])
BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;
SAT, 05 JAN 2008 09:14:16-0500

Puoi scaricare il file da
www.py4e.com/code3/mbox-short.txt



nome_file = input("Enter a file name: ")
if nome_file == "":
    nome_file = "mbox-short.txt"
try:
    with open(nome_file) as f:
        for riga in f:
            print(riga.rstrip().upper())
except FileNotFoundError:
    print("File non trovato.")
        






esercizio 16

scrivi un programma per richiedere il nome di un file, leggerlo e
ricercare le linee del form:
`X-DSPAM-Confidence:` **`0.8475` **



Quando trovi una riga che inizia con “X-DSPAM-Confidence:” seziona la riga per
estrarre il numero a virgola mobile contenuto nella stessa. Conta queste righe e
quindi calcolane il totale dei valori di spam confidence.
Quando raggiungi la fine del file, visualizza la media dei valori di spam confidence.
Inserite il nome del file: mbox.txt
Media spam confidence : 0.894128046745
Inserisci il nome del file: mbox-short.txt
Media spam confidence: 0.750718518519
Metti alla prova il tuo script sui file mbox.txt e mbox-short.txt.



percorso = input("inserisci il percorso del file: ")
numero_righe = 0
somma = 0
try:
    with open(percorso) as handle:
        for line in handle:
            line = line.rstrip()
            if line.startswith("X-DSPAM-Confidence:"):
                posizione_valore_nella_riga = line.find(":")
                valore_nella_riga = line[posizione_valore_nella_riga+1:].strip()
                somma += float(valore_nella_riga) 
                numero_righe += 1
        if numero_righe > 0:
            calcolo_media = somma / numero_righe
            print(f"Media spam confidence: {calcolo_media}")
        else:
            print("Nessuna riga con X-DSPAM-Confidence trovata.")
except FileNotFoundError:
    print("inserisci un file valido")            
        





            

esercizio 17

 Capita che quando gli sviluppatori si annoiano o vogliono divertirsi,
aggiungano un innocuo Easter Egg al loro programma. Modifica lo script prece
dente in modo che visualizzi un messaggio divertente nel caso l’utente inserisca
quale nome del file “na na boo boo”.
Il programma dovrebbe comportarsi normalmente in tutti gli altri casi (con file
esistente o meno). Ecco un esempio del programma:
python egg.py
Immettere il nome del file: mbox.txt
There were 1797 subject lines in mbox.txt
python egg.py
Immettere il nome del file: missing.tyxt
File cannot be opened: missing.tyxt
python egg.py
Inserisci il nome del file: na na boo boo
NA NA BOO BOO TO YOU- You have been punk'd!



percorso = input("inserisci il percorso del file: ")
if percorso != "na na boo boo" :
    numero_righe = 0
    somma = 0
    try:
        with open(percorso) as handle:
            for line in handle:
                line = line.rstrip()
                if line.startswith("X-DSPAM-Confidence:"):
                    posizione_valore_nella_riga = line.find(":")
                    valore_nella_riga = line[posizione_valore_nella_riga+1:].strip()
                    somma += float(valore_nella_riga) 
                    numero_righe += 1
            if numero_righe > 0:
                calcolo_media = somma / numero_righe
                print(f"Media spam confidence: {calcolo_media}")
            else:
                print("Nessuna riga con X-DSPAM-Confidence trovata.")
    except FileNotFoundError:
        print("inserisci un file valido")     
else:
    print("NA NA BOO BOO TO YOU- You have been punk'd!")







esercizio 18

Scrivi una funzione chiamata chop che prenda un elenco, lo modifichi
rimuovendo il primo e l’ultimo elemento e restituisca None.
Quindi scrivi una funzione chiamata middle che prenda un elenco e restituisca un
nuovo elenco contenente tutti gli elementi tranne il primo e l’ultimo.



lista1 = [0,1,2,3,4,5,6,7,8,9]

def chop(my_lista):
    my_lista.pop(0)
    my_lista.pop(-1)
    
chop(lista1)


def middle(my_lista):
    new_list = list()
    new_list = my_lista[1:-1]
    return new_list
    
A = middle(lista1)
print(A)







esercizio 19

scopri quale riga del programma precedente non è ancora adeguata
mente protetta. Cerca di costruire un file di testo che faccia fallire il programma
e quindi modifica il programma in modo che la riga sia adeguatamente protetta
e testala nuovamente per essere sicuro che gestisca correttamente il nuovo file di
testo.



fhand = open(r"testoesempio.txt")
count = 0
for line in fhand:
    words = line.split()
    #print ('Debug:', words)
    if len(words) == 0 : continue
    if words[0] != 'From' : continue
    if len(words) < 3: continue # agguinto controllo lungezza minima
    print(words[2]) # IndexError: list index out of range





esercizio 20
riscrivi il codice guardiano dell’esempio precedente senza le due
istruzioni if. Usa invece un’espressione logica composta dall’operatore and e una
singola istruzione if.


fhand = open(r"testoesempio.txt")
count = 0
for line in fhand:
    words = line.split()
  #  print ('Debug:', words)
    if len(words) > 0 and words[0] == 'From' and len(words) >= 3:
        print(words[2]) 





esercizio 20

 scarica una copia del file www.py4e.com/code3/romeo.txt
Scrivi un programma che lo apra e lo legga riga per riga. Dividi la riga in un elenco
di parole usando la funzione split.
Controlla se ogni parola è già presente in un elenco. Se la parola non è nell’elenco,
aggiungila. Al termine del programma, ordina e visualizza in ordine alfabetico le
parole risultanti.


fhand = r"romeo.txt"
lista_parole = list()

try:
    with open(fhand) as handle:
        for line in handle:
            line = line.rstrip()
            parole = line.split()
            for parole_selezionate in parole:
                if not parole_selezionate in lista_parole:
                    lista_parole.append(parole_selezionate)
                    lista_parole.sort()
                  
    print(lista_parole)
                 
except FileNotFoundError:
    print("errore con il file")
                        
   





esercizio 21
Scrivi un programma per leggere i dati della casella di posta e quando
trova la riga che inizia con “From”, divida la riga in parole usando la funzione split.
Siamo interessati a sapere chi ha inviato il messaggio indicato nella parola delle
righe che iniziano con From.
From stephen.marquard@uct.ac.za Sat 5 Jan 09:14:16 2008
Analizza la riga From per visualizzarne la seconda parola, quindi conta anche il
numero di righe From (non From:), visualizzandone il risultato alla fine.



casella_posta = r"C:\Users\gioel\OneDrive\Documenti\Programmazione\Python_course2\esercizi\mbox-short.txt"
numero_righe = 0

try:
    with open(casella_posta) as hand:
        numero_righe = 0
        for linea in hand:
            if linea.startswith("From "):
                parole = linea.split()
                print(parole[1])
                numero_righe += 1
        print(f"There were {numero_righe} lines...")
except FileNotFoundError:
    print("Errore: file non trovato")        





esercizio 22

Riscrivi il programma che richiede all’utente un elenco di numeri e
ne visualizza il maggiore ed il minore, quando riceve in input la stringa “done”. Il
programma ora memorizzerà i numeri inseriti dall’utente in un elenco e tramite le
funzioni max() e min() fornirà i numeri massimo e minimo quando l’utente fornisce
in input la parola “done”.
Enter a number: 6
Enter a number: 2
Enter a number: 9
Enter a number: 3
Enter a number: 5
Enter a number: done
Maximum: 9.0
Minimum: 2.0




import sys

lista_elenco = list()
try:
   while True:
        inserimento_utente = input("Enter a number: ") # da gestire con input
        if inserimento_utente == "done": break
        lista_elenco.append(float(inserimento_utente))
except ValueError:
    print("inserire un numero correttamente")
    sys.exit()

if lista_elenco:
    numero_minore = min(lista_elenco)
    numero_maggiore =max(lista_elenco)

print(f"Maximum: {numero_maggiore}")
print(f"Mnimum: {numero_minore}")





esercizio 23

Scarica una copia del file: www.py4e.com/code3/words.txt
Scrivi un programma che legga le parole in words.txt e le memorizzi come chiavi
in un dizionario.Non importa quali siano i valori. Quindi puoi usare l’operatore
in per verificare rapidamente se una stringa è contenuta nel dizionario.




percorso_file = r"testoesempio.txt"
dizionario = dict()

with open(percorso_file) as hand:
    for line in hand:
        line = line.rstrip()
        line = line.split()
        for parola in line:
            dizionario[parola] = 1
    if "your" in dizionario:
        print(dizionario)

   

esercizio 24

Scrivi un programma che classifichi ogni messaggio di posta in base
al giorno della settimana in cui è stato inviato. Per fare ciò, cerca le righe che
iniziano con “From”, quindi cerca la terza parola e aggiorna il conteggio di ciascuno
dei giorni della settimana. Alla fine del programma visualizza i contenuti del tuo
dizionario (l’ordine non ha importanza).
Riga di esempio:
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

Esempio di esecuzione:
python dow.py
Enter a file name: mbox-short.txt
{'Fri': 20, 'Thu': 6, 'Sat': 1}



percorso_file = r"mbox-short.txt"

my_dict = dict()

with open(percorso_file) as hand:
    for line in hand:
        line = line.rstrip()
        if line.startswith("From "):
            line = line.split()
            if not line[2] in my_dict:
                my_dict[line[2]] = 1
            else:
                my_dict[line[2]] += 1
print(my_dict)

percorso_file = r"mbox-short.txt"
conteggio_giorni = {}

with open(percorso_file) as handle:
    for riga in handle:
        if not riga.startswith("From "):
            continue
        parole = riga.split()
        if len(parole) < 3:
            continue
        giorno = parole[2]
        conteggio_giorni[giorno] = conteggio_giorni.get(giorno,0)+1
        
print(conteggio_giorni)
        









esercizio 25
Scrivi un programma che analizzi un log di posta, crei un istogramma
utilizzando un dizionario per contare quanti messaggi sono arrivati da ciascun
indirizzo di posta elettronica ed infine visualizzi il dizionario

"""


percorso_file = r"C:\Users\gioel\OneDrive\Documenti\Programmazione\Python_course2\esercizi\mbox-short.txt"

        
        
        
        
        
        
        
        
        







