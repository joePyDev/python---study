def binary_search(data, target):
    """
    Perform a binari search to find the target element whitin a sorted data list.

    Parameters
    ----------
    data : TYPE list
        DESCRIPTION.
        The sorted list of element to search through

    target : TYPE
        DESCRIPTION.
        The element to search for.
    Returns
    Int: The index of the target if found , -1 otherwise.
    -------
    """

    low = 0
    high = len(data) - 1
    print("debug lunghezza iniziale", high)

    while low <= high:
        print("debug range low e high", low, high)
        mid = (low + high) // 2
        print("debug >>> mid ", mid)
        if data[mid] == target:
            print(("debug trovata corrispondenza"))
            return mid
        elif data[mid] < target:
            print("debug target < data mid", data[mid])
            low = mid + 1
            print("debug low", low)
        else:
            print("debug target > data mid", data[mid])
            high = mid + 1
            print("debug high", high)

    return -1


lista_esempio = [0, 1, 2, 3, 4, 5, 6]
binary_search(lista_esempio, 1)
