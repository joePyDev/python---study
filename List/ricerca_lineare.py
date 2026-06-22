# linear search in list


def linear_serch(data, target):
    if not isinstance(data, list):
        return "invalid input: must be a list"

    if not data:
        return -1

    for i in range(len(data)):
        if data[i] == target:
            return i

    return -1


my_list = ["milli", "lulu", "fuffi"]
ricerca_lineare = linear_serch(my_list, "fuffi")


if ricerca_lineare != -1:
    print("Trovata corrispondenza su posizione:", ricerca_lineare)
else:
    print("Nessuna corrispondenza")
