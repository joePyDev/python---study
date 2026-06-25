"""
except Exception as e: prende qualsiasi tipo di eccezione
(da IndexError a socket.gaierror, ConnectionRefusedError,
errori di decodifica, timeout…) e la gestisce in un unico punto.

"""

import sys

try:
    y = 10 / 1

except Exception as e:
    print(f"Errore {e}")
    sys.exit()  # esci dal programma

# -------------------------------------------
try:
    value = 10 / 2
except ZeroDivisionError:
    print("Error: division by zero")
else:
    print("No exceptions occurred")
finally:
    print("Cleanup complete")
