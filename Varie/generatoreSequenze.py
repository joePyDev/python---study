def number_pattern(n):
    if not isinstance(n, int):
        return "Argument must be an integer value."
    elif n <= 0:
        return "Argument must be an integer greater than 0."
    else:
        stringa = ""
        for i in range(1, n + 1):
            stringa += str(i)
            stringa += " "
    stringa = stringa.rstrip()
    return stringa


A = number_pattern(4)
print(A)

A = number_pattern(12)
print(A)
