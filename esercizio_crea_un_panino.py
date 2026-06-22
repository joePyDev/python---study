def make_sandwich(bread_type, filling, cheese=None, toasted=False):
    """questa funzione crea un panino:
    - bread_type = str , tipo di pane,(required)
    - filling = str , farcitura panino (required)
    - cheese = str , quale formaggio (facoltativo)
    - toasted = bool , compreso tostatura (facoltativo)
    - return str tipo di panino scelto
    """

    panino = ""
    if toasted == True and cheese == None:
        panino = f"Making a toasted {bread_type} sandwich with {filling}."
    elif toasted == True and cheese != None:
        panino = f"Making a toasted {bread_type} sandwich with {filling} and {cheese} cheese."
    else:
        panino = f"Making a {bread_type} sandwich with {filling}."

    return panino


A = make_sandwich("wheat", "turkey", "cheddar", True)
B = make_sandwich("rye", "ham")

print(A)
print(B)
