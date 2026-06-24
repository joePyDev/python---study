# stampa istruzioni


def calculate_average(numbers):
    print("Input numbers:", numbers)
    total = sum(numbers)
    print("Total:", total)
    count = len(numbers)
    print("Count:", count)
    average = total / count
    print("Average:", average)
    return average


lista_numeri = [1, 5, 15, 20, 25]
calculate_average(lista_numeri)


# logging
import logging

logging.basicConfig(filename="app.log", level=logging.DEBUG)
logging.debug("This is a debug message")
logging.info("This is an informational   message")
logging.warning("This is a warning message")
logging.error("This is an error message")
