# liste : sequenza ordinata di elementi , stringhe , numeri , altre liste.
# Le liste sono mutabili , e indicizzate in base zero.


citta = ["Roma","Milano","Napoli"]


# accesso alla lista:
print(citta[0]) # Roma


# indicizzazione negativa:
print(citta[-1]) #☺ Napoli




# Per creare una lista possiamo usare il costruttore list():
developer = "jessica"
my_list = list(developer)
print(my_list)



# Per ottenere il numero totale di elementi di una lista possiamo usare len():
numeri = [1,2,3,4,5,6]
print(len(numeri))



# Aggiornare un valore di un indice:

linguaggi_programmazione = ["Python","Java","C++","Rust"]
print(linguaggi_programmazione, id(linguaggi_programmazione))

linguaggi_programmazione[1] = "Java Script"
print(linguaggi_programmazione, id(linguaggi_programmazione))

# attenzione a modificare con un indice errato




# per rimuovere un elemento possiamo usare del:
del linguaggi_programmazione[1:]
print(linguaggi_programmazione, id(linguaggi_programmazione))



# Con in possiamo verificare la presenza di un elemento:
A = "Python" in linguaggi_programmazione
print(A)



# Comuni sono liste annidiate:
misto = ["Alice","Ciao",[1,2,3],False]    
print(misto[2])
    


# accesso a un elemento della lista annidiata:
print(misto[2][0])    
    


#  decompressione dei valori di una lista:
nuova_lista = ["Alice",44,True]

nome,eta,disponibilita = nuova_lista    
    
print(nome,eta,disponibilita)
    
    
    
    
    
    
    
    
    
    
    