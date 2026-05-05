import pandas as pd

# Leggo il file CSV e lo carico in un DataFrame (una tabella)
df = pd.read_csv("dati_grezzi.csv",encoding="latin-1")

# Mostro le prime 5 righe per vedere com'è fatto
print("Prime 5 righe:")
print(df.head())

# Mostro informazioni tecniche: numero righe, colonne, tipi di dati
print("\nInformazioni sul DataFrame:")
df.info()

# Controllo quante righe sono completamente duplicate
print("\nNumero di righe duplicate:")
print(df.duplicated().sum())

# Controllo i valori mancanti (celle vuote) per ogni colonna
print("\nValori mancanti per colonna:")
print(df.isnull().sum())



