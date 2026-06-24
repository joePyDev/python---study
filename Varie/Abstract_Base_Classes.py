from abc import ABC, abstractmethod


class Animal(ABC):  # Eredito da ABC: questa è una classe astratta
    @abstractmethod  # decorazione @abstractmethod
    def make_sound(self):  # Metodo astratto: nessuna implementazione
        pass


class Dog(Animal):  # Sottoclasse concreta
    def make_sound(self):
        return "Bark!"


# ---------------------------------


class veicolo(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class macchina(veicolo):
    def start(self):
        return "Motore acceso"

    def stop(self):
        return "motore spento"


class bicicicletta(veicolo):
    def start(self):
        return "pedalata!!"

    def stop(self):
        return "frena!!"


# Entrambe le sottoclassi sono usabili

veicoli = [macchina(), bicicicletta()]

for v in veicoli:
    print(v.start())
