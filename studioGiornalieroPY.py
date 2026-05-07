# 1. Definizione della Classe (Il Progetto)
class Robot:
    # Il Costruttore: inizializza l'oggetto con un nome e un livello di batteria
    def __init__(self, nome_robot, capacita_robot):
        self.nome = nome_robot      # Attributo: Nome specifico dell'istanza
        self.capacita = capacita_robot
        self.batteria = 100         # Attributo: Stato iniziale comune

    # Metodo: Un'azione che il robot può compiere
    def consegna_pacco(self, destinazione):
        if self.batteria > 10:
            self.batteria -= 10
            print(f"Robot {self.nome}: Pacco consegnato a {destinazione}!")
            print(f"Batteria residua: {self.batteria}%")
        else:
            print(f"Robot {self.nome}: Batteria troppo bassa per la consegna.")

# --- Utilizzo delle Classi (Istanziazione) ---

# 2. Creiamo due oggetti distinti (Istanze)
robot_veloce = Robot("Flash","veloce")
robot_robusto = Robot("Tank","robusto")

# 3. Interagiamo con gli oggetti
robot_veloce.consegna_pacco("Via Roma 10")
robot_robusto.consegna_pacco("Corso Italia 5")

# Dimostrazione che sono entità diverse:
# Modifichiamo la batteria solo di 'Flash'
robot_veloce.batteria = 5
print(f"\nStato batterie:")
print(f"Batteria di {robot_veloce.nome}: {robot_veloce.batteria}%")
print(f"Batteria di {robot_robusto.nome}: {robot_robusto.batteria}%")     


