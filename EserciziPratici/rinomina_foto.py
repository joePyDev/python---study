import os

cartella = input("Percorso cartella: ").strip()
nuovo_nome_base = input("Nome base (es. Vacanze_a_Roma): ").strip()

# Liste estensioni: aggiungi pure tutte quelle che vuoi
estensioni = (".jpg", ".jpeg", ".png", ".gif")

# Filtraggio (case insensitive)
tutti = os.listdir(cartella)
foto = [f for f in tutti if f.lower().endswith(estensioni)]
foto.sort()

contatore = 1
for vecchio_nome in foto:
    # Preleva l'estensione originale con il punto
    nome_senza_ext, est = os.path.splitext(vecchio_nome)
    print(nome_senza_ext, est)

    # Crea il nuovo nome: base + underscore + numero + estensione originale
    nuovo_nome = f"{nuovo_nome_base}_{contatore}{est}"

    vecchio_path = os.path.join(cartella, vecchio_nome)
    nuovo_path = os.path.join(cartella, nuovo_nome)

    os.rename(vecchio_path, nuovo_path)
    print(f"{vecchio_nome}  →  {nuovo_nome}")
    contatore += 1

print("Fatto!")
