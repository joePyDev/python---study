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



casella_posta = r"mbox-short.txt"
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

Enter file name: mbox-short.txt
{'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
'ray@media.berkeley.edu': 1}



percorso_file = r"mbox-short.txt"
dizionario = {}

with open(percorso_file) as fhand:
    for line in fhand:
        if not line.startswith("From "):
            continue
        line = line.split()
        if len(line) < 2:
            continue
        dizionario[line[1]] = dizionario.get(line[1],0) +1 
print(dizionario)
        







esercizio 26
Aggiungi del codice allo script dell’esercizio precedente che indichi
chi ha il maggior numero di messaggi nel file.
Dopo che sono stati analizzati tutti i dati ed i risultati sono salvati nel dizionario
sono stati letti e il dizionario è stato creato, tramite un ciclo “massimo” (vedi
nel capitolo 5 la sezione 5.7.2 per limitare i cicli) trova chi ha più messaggi e
visualizzane il numero.


    

percorso_file = r"mbox-short.txt"
dizionario = {}
lista = []

with open(percorso_file) as fhand:
    for line in fhand:
        if not line.startswith("From "):
            continue
        line = line.split()
        if len(line) < 2:
            continue
        dizionario[line[1]] = dizionario.get(line[1],0) +1 
    for chiave , valore in dizionario.items():
        lista.append((valore,chiave))
    lista.sort(reverse=True)
    for istogramma in lista:
       print(istogramma[1] , istogramma[0])
        




esercizio 27
 Scrivi uno script che registri il nome di dominio (anziché l’indirizzo)
da cui è stato inviato il messaggio anziché il mittente (ovvero, l’intero indirizzo
email). Alla fine fai in modo che il programma visualizzi i contenuti del dizionario.
python schoolcount.py
Enter a file name: mbox-short.txt
{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}


   

percorso_file = r"mbox-short.txt"
dizionario = {}


with open(percorso_file) as fhand:
    for line in fhand:
        if not line.startswith("From "):
            continue
        line = line.rstrip()
        line = line.split()
        if len(line) < 1:
            continue
        indirizzo = line[1]
        indirizzo = indirizzo.split("@")
        indirizzo = indirizzo[1]
        dizionario[indirizzo] = dizionario.get(indirizzo,0) +1
        
        
print(dizionario)# {'uct.ac.za': 6, 'media.berkeley.edu': 4, 'umich.edu': 7, 'iupui.edu': 8, 'caret.cam.ac.uk': 1, 'gmail.com': 1}
       


        


esercizio 28
Rivediunodegliscriptprecedentinelmodoseguente: leggieanalizza
le righecontenenti “From”edestrai gli indirizzi dallariga. Conta il numerodi
messaggiprovenientidaognipersonausandoundizionario.Dopoaverlettotutti i
dati,visualizzalapersonaconilmaggiornumerodioccorrenzecreandounelenco
di tuple(count, email)daldizionario. Quindiordina l’elenco inordine inversoe
visualizzalapersonachehailmaggiornumerodioccorrenze.
Esempiodiriga:
Fromstephen.marquard@uct.ac.za Sat5Jan 09:14:162008
Inserireunnome perilfile:mbox-short.txt
cwen@iupui.edu 5
Immettereunnome file:mbox.txt
zqian@umich.edu 195





percorso_file = r"mbox-short.txt"
conteggi = {}

with open(percorso_file) as fhand:
    for linea in fhand:
        if not linea.startswith("From "):
            continue
        parti = linea.split()
        if len(parti) < 2:
            continue
        email = parti[1]
        conteggi[email] = conteggi.get(email, 0) + 1


lista_tuple = [(count, email) for email, count in conteggi.items()]
lista_tuple.sort(reverse=True)
massimo_conteggio, email_massimo = lista_tuple[0]

print("Indirizzo con più messaggi:", email_massimo)
print("Numero di messaggi:", massimo_conteggio)






esercizio 29

Questoprogrammacontaladistribuzionedelleoredelgiornoincuiè
statospeditociascunodeimessaggi.Puoiestrarrel’oradallariga“From”trovando
lastringadell’orarioequindi suddividendoquellastringausandoil caratteredei
duepunti. Dopoaver registrato i conteggiperogni timestamp, visualizzali,uno
perriga,ordinandoli inbaseall’oracomemostratodiseguito.

Esempiodiesecuzione:
pythontimeofday.py
Enterafilename: mbox-short.txt
043
061
071
092
103
116
141
152
164
172
181
191




        
percorso_file = r"mbox-short.txt"
conteggio_ore = {}

with open(percorso_file) as fhand:
    for riga in fhand:
        if not riga.startswith("From "):
            continue
        parole = riga.split()
        orario = None
        for p in parole:
            if ":" in p:
                orario = p.split(":")[0]
                break
        if orario is None:
            continue
        conteggio_ore[orario] = conteggio_ore.get(orario, 0) + 1

for ora in sorted(conteggio_ore.keys()):
    print(ora, conteggio_ore[ora])







esercizio 30

:Scriviunprogrammacheleggaunfileevisualizzi lelettereinordine
di frequenzadecrescente. Il tuoprogrammadovrebbeconvertiretuttigli input in
lettereminuscoleecontaresololeletteredallaaallaz. Ilprogrammanondovrebbe
contarespazi, cifre, segnidipunteggiaturaoaltrooltrealle letteredallaaallaz.
Trovaesempiditestoindiverselingueescopricomevarialafrequenzadellelettere
inbaseallalinguainesame.Confrontairisultaticonletabellepresenti inwikipe
dia.org/wiki/Letter_frequencies


import string
import sys

def preleva_valore(item):
    return item[1]

percorso_file = r"mbox-short.txt"
conteggio = {}

try:
    with open(percorso_file) as fhand:
        for linea in fhand:
            for carattere in linea.lower():
                if carattere in string.ascii_lowercase:
                    conteggio[carattere] = conteggio.get(carattere, 0) + 1
except FileNotFoundError:
    print("File non trovato.")
    sys.exit()

for lettera, freq in sorted(conteggio.items(), key=preleva_valore, reverse=True):
    print(lettera, freq)

# utilizzando una funzione lambda
#for lettera, freq in sorted(conteggio.items(), key=lambda x: x[1], reverse=True):
#    print(lettera, freq)




esercizio 31

Scrivi un semplice programma che simuli il comportamento del co
mando grep di Unix. Fai che richieda all’utente l’inserimento di un’espressione
regolare e poi ritorni il numero di righe che corrispondono alle specifiche della
ricerca.


import re
percorso_file = r"mbox-short.txt"
contatore = 0

inserimento_utente = input("Enter a regular expression: ") 
if inserimento_utente == "":
    inserimento_utente = "^From:.+@"

with open(percorso_file) as handle:
    for line in handle:
        line = line.rstrip()
        if re.search("^From:.+@", line):
            contatore += 1
print(f"mbox.txt had {contatore} lines that matched {inserimento_utente}")









esercizio 32

Scrivi un programma per trovare le stringhe contenenti:
`New Revision: 39772`
provvedendo ad estrarre il numero da ciascuna tramite l’uso del metodo findall()
e di una espressione regolare. Calcola e visualizza la media dei numeri.
Enter file:mbox.txt
38444.0323119
Enter file:mbox-short.txt
39756.9259259



import re
contatore = 0
percorso_file = r"mbox-short.txt"

totale_valori = 0

with open(percorso_file) as handle:
    for line in handle:
        line = line.rstrip()
        if re.search(r'^New Revision:\s+(\d+)', line):
            contatore +=1
            valori = re.findall(("\d+"),line)
            for i in valori:
               totale_valori = totale_valori + int(i)
    if contatore > 0:           
        media_valori = totale_valori / contatore
        print(media_valori)
    else:
        print("nessuna riga valida trovata")








esercizio 33
Modifica il programma socket socket1.py in modo da richiedere
all’utente l’URL rendendolo quindi in grado di leggere qualsiasi pagina web. Puoi
usare split('/') per suddividere l’URL nelle sue componenti in modo da poter
estrarre il nome host per la chiamata connect del socket. Aggiungi il controllo
degli errori usando try ed except per gestire la condizione in cui l’utente inserisca
un URL non formattato correttamente o sia inesistente.



import socket

def main():
    url = input('Enter URL (e.g., http://data.pr4e.org/romeo.txt): ').strip()
    
    # Rimuovi http:// se presente (gestisci anche https? per semplicità no)
    if url.startswith('http://'):
        url = url[7:]
    elif url.startswith('https://'):
        print("Questo programma supporta solo HTTP (porta 80).")
        return
    
    try:
        # Dividi per ottenere host e path
        parts = url.split('/')
        host = parts[0]
        if len(parts) > 1:
            path = '/' + '/'.join(parts[1:])
        else:
            path = '/'
        
        print("DEBUG >>>>>> ", path)
        
        # Connessione
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysock.connect((host, 80))
        request = f'GET {path} HTTP/1.0\r\nHost: {host}\r\n\r\n'
        mysock.send(request.encode())
        
        # Ricevi e stampa
        while True:
            data = mysock.recv(512)
            if len(data) < 1:
                break
            print(data.decode())
        mysock.close()
    
    except ValueError:
        print("URL malformato. Assicurati che sia nel formato corretto.")
    except socket.gaierror:
        print("Host non trovato. Controlla il nome del server.")
    except socket.error as e:
        print(f"Errore di connessione: {e}")
    except Exception as e:
        print(f"Errore generico: {e}")

if __name__ == '__main__':
    main()






esercizio 34
 Modifica il tuo programma socket in modo che conti il numero
di caratteri che ha ricevuto e interrompa la visualizzazione di qualsiasi testo dopo
che ne ha mostrato 3000. Il programma dovrà inoltre accettare l’intero documento,
contare il numero totale di caratteri e visualizzarne il numero.


import socket

def main():
    url = input('Enter URL (e.g., http://data.pr4e.org/romeo.txt): ').strip()
    
    # Rimuovi http:// se presente (gestisci anche https? per semplicità no)
    if url.startswith('http://'):
        url = url[7:]
    elif url.startswith('https://'):
        print("Questo programma supporta solo HTTP (porta 80).")
        return
    
    try:
        # Dividi per ottenere host e path
        parts = url.split('/')
        host = parts[0]
        if len(parts) > 1:
            path = '/' + '/'.join(parts[1:])
        else:
            path = '/'
        
        print("DEBUG >>>>>> ", path)
        
        # Connessione
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysock.connect((host, 80))
        request = f'GET {path} HTTP/1.0\r\nHost: {host}\r\n\r\n'
        mysock.send(request.encode())
        
        
        # gestione caratteri
        appoggio_data = b""
        limit = 3000
        
        while True:
            data = mysock.recv(5120)
            if not data: break
            appoggio_data += data
        testo_completo = appoggio_data.decode()
        totale_caratteri = len(testo_completo)
        
        # Stampa i primi 3000 caratteri
        print("\n--- PRIMI 3000 CARATTERI ---")
        print(testo_completo[:limit])
        print("\n--- FINE PRIMI 3000 ---")
        print(f"\nNumero totale di caratteri ricevuti: {totale_caratteri}")
        mysock.close()
    
    
    
    except ValueError:
        print("URL malformato. Assicurati che sia nel formato corretto.")
    except socket.gaierror:
        print("Host non trovato. Controlla il nome del server.")
    except socket.error as e:
        print(f"Errore di connessione: {e}")
    except Exception as e:
        print(f"Errore generico: {e}")

if __name__ == '__main__':
    main()





esercizio 35 
 Utilizza urllib per replicare l’esercizio precedente per (1) recuperare
il documento da un URL, (2) visualizzare i primi 3000 caratteri e (3) contarne
il numero complessivo. Non preoccuparti delle intestazioni per questo esercizio,
per ora è sufficiente mostrare semplicemente i primi 3000 caratteri contenuti nel
documento.




import urllib.request

url = "http://data.pr4e.org/clown.txt"
fhand = urllib.request.urlopen(url)

frammenti = []
totale = 0

for line in fhand:
    riga = line.decode()      
    frammenti.append(riga)
    totale += len(riga)

testo = ''.join(frammenti)
print(testo[:3000])
print(f"\nTotale caratteri: {totale}")





esercizio 36
 Modifica il programma urllinks.py per estrarre e contare i tag
di paragrafo (p) dal documento HTML scaricato e visualizza il conteggio dei pa
ragrafi come output del programma. Non visualizzare il testo del paragrafo: è
sufficiente contarli. Metti alla prova il programma con diverse pagine Web e di
varie dimensioni.





import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignora errori di certificato SSL (utile per siti con HTTPS)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Inserisci URL: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Trova tutti i tag <p> (paragrafo)
paragrafi = soup.find_all('p')
conteggio = len(paragrafi)

print(f"Numero di paragrafi nella pagina: {conteggio}")




"""
