
"""
Tips:
Remember these formulas:

fahrenheit = (celsius * 9/5) + 32

celsius = (fahrenheit - 32) * 5/9

Make sure you are returning values as floating-point numbers; do not round.

"""



def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit): 
    celsius = (fahrenheit - 32) * 5/9
    return celsius



def convert_temperature(temperature, unit): 
    
    if unit == "C":
        ctf = celsius_to_fahrenheit(float(temperature))
        return ctf
    
    elif unit =="F":
        ftc = fahrenheit_to_celsius(float(temperature))
        return ftc
    



temperature_c = 25
temperature_f = 77

converted_f = convert_temperature(temperature_c, "C")
converted_c = convert_temperature(temperature_f, "F")

print(f"{temperature_c}°C is equal to {converted_f}°F")
print(f"{temperature_f}°F is equal to {converted_c}°C")