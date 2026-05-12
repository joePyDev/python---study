"""
except Exception as e: prende qualsiasi tipo di eccezione 
(da IndexError a socket.gaierror, ConnectionRefusedError, 
errori di decodifica, timeout…) e la gestisce in un unico punto.

"""




import sys

try:
    pass

except Exception as e:
    print(f"Errore {e}")
    sys.exit() # esci dal programma

    
    