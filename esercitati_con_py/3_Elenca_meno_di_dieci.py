spesa = ["cipolle", "carote", "mele", "banane"]


def lista_spesa(spesa):
    lista = []
    for prodotto in spesa:

        if prodotto.startswith("c"):
            #       print(prodotto)
            lista.append(prodotto)
    prodotto_singolo = lista[0]
    return lista, prodotto_singolo


A = lista_spesa(spesa)
