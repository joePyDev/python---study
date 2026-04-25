
# dir() 
# help()

    
"""
- leggere il file
- trovare  dove viene visualizzata l'ora di invio ( nella figa From)
- si splitta e si trova l'indice della orario'
- slice per estrarre l'ora 
- trovato i valori :
    organizzare i valori in ora e frequenza
"""



name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

lista = []
dizionario = dict()

for riga in handle:
    riga = riga.rstrip()
    if riga.startswith("From "):
        lista = riga.split()
        orario = lista.pop(5)
        ora = orario[:2]
        ora = ora.split()
        for i in ora:
            dizionario[i] = dizionario.get(i,0)+1

newdict = dict()
newdict = sorted(dizionario.items())
for val , key in newdict:
    print(val , key)
    
    
    
    
    