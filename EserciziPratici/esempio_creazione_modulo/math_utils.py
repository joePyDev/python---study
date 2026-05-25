# math_utils.py

def calcolo_somma(valore1 , valore2):
    """ somma di 2 valori """
    return valore1 + valore2


def calcolo_sottrazione(valore_grande , valore_piccolo):
    """ calcolo sottrazione tra 2 valori """
    return valore_grande - valore_piccolo



class quadrato:
    """ rappresenta un rettangolo con base e altezza uguali """
    def __init__ (self,lato):
        self.lato = lato
        
    def calcolo_perimetro(self):
        """ calcolo del perimetro del quadrato """ 
        return self.lato * 4
    
    def calcolo_area(self):
        """ calcolo area quadrato """
        return self.lato ** 2
    
    
    