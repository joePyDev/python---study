"""
Ricorsione funzioni:
Significa che una funzione chiama se stessa.
Questo ha il vantaggio di consentire di iterare sui
dati per raggiungere un risultato.
"""


def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)  # 4 + 6 | 3 + 3 | 2 + 1 | 1 + 0
        print(result)
    else:
        result = 0
    return result


print("Recursion Example Results:")
tri_recursion(4)


"""
tri_recursion(4)
│
├─ chiama tri_recursion(3)
│  │
│  ├─ chiama tri_recursion(2)
│  │  │
│  │  ├─ chiama tri_recursion(1)
│  │  │  │
│  │  │  ├─ chiama tri_recursion(0)
│  │  │  │  └─ restituisce 0 (nessuna stampa)
│  │  │  │
│  │  │  └─ result = 1 + 0 = 1 → stampa 1 → restituisce 1
│  │  │
│  │  └─ result = 2 + 1 = 3 → stampa 3 → restituisce 3
│  │
│  └─ result = 3 + 3 = 6 → stampa 6 → restituisce 6
│
└─ result = 4 + 6 = 10 → stampa 10 → restituisce 10
"""
