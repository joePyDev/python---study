
"""
- lettura file mbox-short.txt
- individuare chi ha mandato il maggior numero di messaggi posta.
- trovare le righe che iniziano con"From"
- prelevare la seconda parola della riga come mittente

- creare un dizionario che associ mail mittente  al numero di volte che comapre 
-un ciclo scorre il dizionario per trovare l'utente che ha mandato piu messaggi'

"""


#  lettura file mbox-short.txt
name = input("Enter file:")
if len(name) < 1:
    name = r"mbox-short.txt"
    try:
        handle = open(name)
    except:
        print("not valid path!")
        exit()
dizionario = dict()
for riga in handle:
    riga = riga.rstrip()
    if riga.startswith("From"):
        rigasplit = riga.split()
        print("debug riga ",rigasplit)
        if len(rigasplit) < 3: 
            continue

        if not rigasplit[1] in dizionario:
            dizionario[rigasplit[1]] = 1
        else:
            dizionario[rigasplit[1]] = dizionario[rigasplit[1]] + 1
        
print(dizionario)         
         
big_chiave = None
big_valore = None
for chiave , valore in dizionario.items():
        if big_valore == None or valore > big_valore :
            big_valore = valore
            big_chiave = chiave
print(big_chiave ,  big_valore)
            
  
    