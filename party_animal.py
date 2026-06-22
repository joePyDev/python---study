class party_animal:
    def __init__(self):
        self.x = 0

    def party(self):
        self.x = self.x + 1
        print("so far", self.x)

    def __del__(self):
        print("i am destructed", self.x)


# crea l'istanza della classe party_animal
an = party_animal()

# qui viene chiamato il metodo di istanza
an.party()
an.party()
an.party()
# qui si passa direttamente la funzione party
party_animal.party(an)

an.__del__()


"""
Istanza = l'oggetto, la cosa (contiene i dati). Es: an, bn.
Metodo di istanza = la funzione, l'azione (contiene il codice). Es: party().

"""


class Greeter:
    def __init__(self):
        self.count = 0
        print("Greeter constructed")

    def greet(self):
        self.count = self.count + 1
        print("Greeting number", self.count)


person = Greeter()
person.greet()


class Greeter:
    def __init__(self):
        self.message = "Hello"

    def show(self):
        print(self.message)


person = Greeter()
person.show()


class Counter:
    def __init__(self):
        self.value = 0

    def bump(self):
        self.value = self.value + 1
        print(self.value)


c = Counter()
c.bump()
c.bump()
c.bump()
