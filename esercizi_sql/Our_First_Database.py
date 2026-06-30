"""
-Crea un database SQLITE
-Crea una tabella chiamata "Ages" :
    CREATE TABLE Ages (
  name VARCHAR(128),
  age INTEGER
)

-Assicurati quindi che la tabella sia vuota eliminando tutte le
 righe inserite in precedenza.

- inserisci solo queste righe utilizzando i seguenti comandi:
DELETE FROM Ages;
INSERT INTO Ages (name, age) VALUES ('Tasniem', 21);
INSERT INTO Ages (name, age) VALUES ('Tigan', 17);
INSERT INTO Ages (name, age) VALUES ('Eilean', 13);
INSERT INTO Ages (name, age) VALUES ('Lillia', 39);
INSERT INTO Ages (name, age) VALUES ('Darrach', 18);

- Una volta completati gli inserimenti, eseguire il seguente comando SQL:
    SELECT hex(name || age) AS X FROM Ages ORDER BY X

- Individua la prima riga nel set di record risultante e inserisci la lunga stringa che ha un aspetto simile a 53656C696E613333 .
"""

import sqlite3

connessione = sqlite3.connect("first_databaseSQL.sqlite")

cursore = connessione.cursor()

"""
cursore.execute("DROP TABLE IF EXISTS Ages ")
connessione.commit()

cursore.execute("CREATE TABLE Ages (name VARCHAR(128),age INTEGER)")
connessione.commit()

cursore.execute(
    "DELETE FROM Ages;INSERT INTO Ages (name, age) VALUES ('Tasniem', 21)"
)
connessione.commit()

cursore.execute("INSERT INTO Ages (name, age) VALUES ('Tigan', 17)")
connessione.commit()

cursore.execute("INSERT INTO Ages (name, age) VALUES ('Eilean', 13)")
connessione.commit()

cursore.execute("INSERT INTO Ages (name, age) VALUES ('Lillia', 39)")
connessione.commit()

cursore.execute("INSERT INTO Ages (name, age) VALUES ('Darrach', 18)")
connessione.commit()
"""

cursore.execute("SELECT hex(name || age) AS X FROM Ages ORDER BY X")
for row in cursore:
    print(row)

connessione.close()
