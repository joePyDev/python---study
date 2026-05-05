
testo_del_paragrafo = r"C:\Users\gioel\Downloads\Testo del paragrafo.pdf"

"""
PDF 
→ estrai testo per pagina 
→ individua i dati con pattern 
→ raccogli in lista 
→ converti in CSV

"""


import PyPDF2
import pandas as pd
import re

# ---------- PASSO 1: APERTURA DEL PDF (senza with open) ----------
percorso_pdf = input("Incolla il percorso del file PDF: ").strip()

try:
    lettore = PyPDF2.PdfReader(percorso_pdf)   # 👈 diretto percorso
    totale_pagine = len(lettore.pages)
    print(f"PDF caricato: {totale_pagine} pagine trovate.")
except FileNotFoundError:
    print("File non trovato. Controlla il percorso.")
    exit()
except Exception as e:
    print(f"Errore nell'apertura del PDF: {e}")
    exit()

# ---------- PASSO 2: ESTRAZIONE DEL TESTO ----------
testo_completo = ""

for numero_pagina in range(totale_pagine):
    pagina = lettore.pages[numero_pagina]
    testo_pagina = pagina.extract_text()
    testo_completo += testo_pagina + "\n"
    print(f"Pagina {numero_pagina + 1}/{totale_pagine} estratta.")

print(f"\nTotale caratteri estratti: {len(testo_completo)}")


# ---------- PASSO 3: PARSING DEL TESTO CON ESPRESSIONI REGOLARI ----------
# (Questa parte va ADATTATA al PDF del cliente)
dati = []
righe = testo_completo.split('\n')

for riga in righe:
    # Cerca "Nome: ..."
    match_nome = re.search(r'Nome:\s*(.+)', riga)
    if match_nome:
        nome = match_nome.group(1).strip()
        dati.append({'Tipo': 'Nome', 'Valore': nome})

    # Cerca "Importo: ..."
    match_importo = re.search(r'Importo:\s*([\d.,]+)', riga)
    if match_importo:
        importo = match_importo.group(1).strip()
        dati.append({'Tipo': 'Importo', 'Valore': importo})

    # Cerca "Data: ..."
    match_data = re.search(r'Data:\s*([\d/.-]+)', riga)
    if match_data:
        data_val = match_data.group(1).strip()
        dati.append({'Tipo': 'Data', 'Valore': data_val})

print(f"Dati estratti: {len(dati)} righe.")

# ---------- PASSO 4: SALVATAGGIO IN CSV ----------
df = pd.DataFrame(dati)
nome_output = input("Nome del file di output (Invio per 'output.csv'): ").strip()
if nome_output == "":
    nome_output = "output.csv"
if not nome_output.endswith('.csv'):
    nome_output += '.csv'

df.to_csv(nome_output, index=False, encoding='utf-8-sig')
print(f"Dati salvati in '{nome_output}' ({len(df)} righe).")