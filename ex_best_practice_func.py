

# esercizio

def calculate_diameter_circle(radius: float) -> float:
    """ -calcolo del diametro,(diametro = raggio * 2)
        -consigliato che radius sia valore float
        -non sono accettati valori radius negativi, errore -1 
        - ritorno diametro del cerchio in float
    """
    if radius < 0:
        return -1
    return radius * 2



test_caso1 =  calculate_diameter_circle(7)
test_caso2 = calculate_diameter_circle(2.5)
test_caso3 = calculate_diameter_circle(0)
test_caso4 = calculate_diameter_circle(-3)
test_caso5 = calculate_diameter_circle(1000000)


print(f"caso1 {test_caso1},caso2 {test_caso2},caso3 {test_caso3},caso4 {test_caso4},caso5 {test_caso5},")




