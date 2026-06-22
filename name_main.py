"""
Script di esempio per spiegare il costrutto:
    if __name__ == '__main__':
        ...

Questo script può essere eseguito direttamente oppure importato come modulo.
Quando viene eseguito direttamente, la variabile speciale __name__ assume il valore '__main__'.
Quando viene importato, __name__ diventa il nome del modulo (cioè il nome del file senza .py).

Il blocco if __name__ == '__main__' contiene codice che vogliamo eseguire SOLO
quando lo script è lanciato come programma principale, non quando viene importato.
"""

# ---------------------------
# Definizione di funzioni "utili" (il modulo)
# ---------------------------


def saluta(nome):
    """Restituisce un messaggio di saluto."""
    return f"Ciao, {nome}!"


def quadrato(x):
    """Calcola il quadrato di un numero."""
    return x * x


# ---------------------------
# Codice di test / dimostrativo
# ---------------------------

# Questo print è fuori dall'if, quindi viene eseguito SEMPRE,
# anche quando il file è importato. Di solito si evita di mettere codice
# eseguibile a livello di modulo, ma lo facciamo per mostrare la differenza.
print(f"[{__name__}] Il modulo è stato caricato.")

# Il blocco successivo viene eseguito SOLO se lo script è avviato direttamente.
if __name__ == "__main__":
    print("=" * 50)
    print("Questo codice viene eseguito SOLO in esecuzione diretta.")
    print("Se stai importando questo file, non vedrai queste righe.\n")

    # Eseguiamo un piccolo test automatico delle funzioni
    print("Test delle funzioni:")
    print(f"  saluta('Mario') = {saluta('Mario')}")
    print(f"  quadrato(5)      = {quadrato(5)}")

    # Messaggio finale
    print("\nFine del test. Tutto ok!")
    print("=" * 50)
else:
    # Questo ramo si esegue quando il file è importato (__name__ != '__main__')
    print(
        f"[{__name__}] Il modulo è stato importato. "
        "Le funzioni sono disponibili ma il test non viene eseguito."
    )
