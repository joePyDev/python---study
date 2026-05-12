"""
Esercizio 1: Modifica il programma socket socket1.py in modo da richiedere
all’utente l’URL rendendolo quindi in grado di leggere qualsiasi pagina web. Puoi
usare split('/') per suddividere l’URL nelle sue componenti in modo da poter
estrarre il nome host per la chiamata connect del socket. Aggiungi il controllo
degli errori usando try ed except per gestire la condizione in cui l’utente inserisca
un URL non formattato correttamente o sia inesistente.
"""

"""
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
while True:
data = mysock.recv(512)
if len(data) < 1:
break
print(data.decode(),end='')
mysock.close()
"""


import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
inp = input("inserisci url >>> ")
splitted_url = inp.split("/")

try:
    host = splitted_url[2]
    mysock.connect((host, 80))
    cmd = f'GET {inp} HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(), end='')

except Exception as e:
    print(f"Si è verificato un errore: {e}")

finally:
    mysock.close()


