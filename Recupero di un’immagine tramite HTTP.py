# Importa il modulo 'socket': permette di creare connessioni di rete a basso livello (TCP/IP).
import socket

# Importa il modulo 'time': qui non è usato, ma spesso serve per pause o timestamp.
import time

# Costante: il dominio del server a cui ci vogliamo collegare.
HOST = "data.pr4e.org"

# Costante: la porta TCP a cui collegarsi (80 = HTTP standard, non cifrato).
PORT = 80

# Crea un nuovo socket.
# AF_INET indica che useremo indirizzi IPv4.
# SOCK_STREAM indica che vogliamo una connessione TCP affidabile (a flusso).
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Stabilisce la connessione al server, specificando una tupla (HOST, PORT).
# Il sistema operativo risolve il dominio in IP e completa l'handshake TCP.
mysock.connect((HOST, PORT))

# Invia la richiesta HTTP al server.
# b"..." trasforma la stringa in una sequenza di byte, necessaria per i socket.
# \r\n (carriage return + line feed) indica la fine di una riga HTTP.
# Due \r\n\r\n finali segnano la fine delle intestazioni HTTP (header).
mysock.sendall(b"GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n")

# Inizializza un contatore a 0: conterà i byte totali ricevuti.
count = 0

# Variabile che conterrà l'intera risposta ricevuta (header + corpo) come byte.
picture = b""

# Ciclo infinito per leggere la risposta a blocchi.
while True:
    # Riceve fino a 5120 byte dalla connessione.
    # Restituisce una stringa di byte (o una vuota se la connessione è chiusa).
    data = mysock.recv(5120)

    # Se non ci sono più dati (connessione chiusa), esce dal ciclo.
    if len(data) < 1:
        break
    # La riga seguente, se commentata, avrebbe messo una pausa di 0.25 secondi
    # dopo ogni blocco ricevuto (utile per simulare trasferimenti lenti o debug).
    time.sleep(0.25)

    # Aggiorna il contatore totale di byte ricevuti.
    count = count + len(data)

    # Stampa a video: dimensione di questo blocco e totale progressivo.
    print(len(data), count)

    # Aggiunge i byte appena ricevuti alla variabile 'picture'.
    picture = picture + data

# Chiude il socket. La connessione TCP viene terminata.
mysock.close()

# Ora inizia l'analisi della risposta HTTP ricevuta.

# Cerca la posizione della sequenza \r\n\r\n (due newline consecutivi),
# che nel protocollo HTTP separa gli header dal corpo (qui l'immagine).
pos = picture.find(b"\r\n\r\n")

# Stampa la lunghezza degli header (in byte) e il loro contenuto decodificato in testo.
print("Header length", pos)
print(picture[:pos].decode())

# Elimina gli header: tiene solo il corpo (l'immagine), saltando i 4 byte \r\n\r\n.
picture = picture[pos + 4:]

# Apre (o crea) il file "stuff.jpg" in modalità scrittura binaria ('wb').
fhand = open("stuff.jpg", "wb")

# Scrive i byte dell'immagine nel file.
fhand.write(picture)

# Chiude il file: essenziale per salvare correttamente e liberare risorse.
fhand.close()