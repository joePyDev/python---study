"""
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

"""



fout = open(r"C:\Users\gioel\OneDrive\Desktop\nuovo_file.txt","w")
print(fout)

line = "contenuto da scrivere\n"
fout.write(line)
fout.write("1234.\n")
fout.write("1234..\n")
fout.write("1234...\n")
fout.write("1234....\n")

fout.close()



#-------------------------------- liste

vuoto = []

pieno = [1,"stringa",False]


# le liste sono mutabili
print(id(pieno))


# paretesi a sinistra, modifica del elemento:
pieno[1] = "formaggio"
print(id(pieno))

A = pieno
# ATTENZIONE!! 
A.append("11111")

print(A)
print(id(pieno))
print(pieno)




# scorrere un elenco: 

for contenuto in pieno:
    print(contenuto)




numeri = [10,15,20,25]
myList = []


for i in numeri:
    myList.append(i)        

print(myList)
















