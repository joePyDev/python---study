
import sys

# lavorare con i file

fname = input("inserisci il nome del file : ")
try:
    fhandle = open(fname)
except:
    print(" il file non può essere aperto")
    sys.exit()   
    
count = 0
for line in fhandle:
    if line.startswith("From"):
        count = count + 1
print(f"corispondenza trovata {count} volte nel file {fname} ")        










