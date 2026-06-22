# ho definito la classe, assegnato attributi e metodi
class BankAccount:

    def __init__(self, initial_balance):
        self._balance = initial_balance  # convenzione: attributo protetto

    def deposito(self, amount):
        if amount < 0:
            raise ValueError("l'importo deve essere positivo")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("L'importo deve essere positivo")
        if amount > self._balance:
            raise ValueError("Saldo insufficiente")
        self._balance -= amount

    def get_balance(self):
        return self._balance


# adesso si chiama i metofdi:

conto = BankAccount((10000))
conto.deposito(1000)
conto.withdraw(200)
print(conto.get_balance())


# Uso scorretto (violazione dell'incapsulamento)
conto = BankAccount(1000)

# Accesso diretto all'attributo protetto
print(conto._balance)  # 1000   (funziona, ma è sconsigliato)

# Modifica diretta
conto._balance = 5000
print(conto.get_balance())  # 5000   (ho scavalcato tutti i controlli)

# Posso anche mettere il conto in uno stato inconsistente
conto._balance = -99999
print(conto.get_balance())  # -99999 (saldo negativo senza prelievo!)
