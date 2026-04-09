

# lavorare con i file


fname = input("inserisci il nome del file : ")
fhandle = open(fname)
count = 0
for line in fhandle:
    if line.startswith("From"):
        count = count + 1
print(f"corispondenza trovata {count} volte nel file {fhandle} ")        











