"""
Crear una funcion que convierta una temperatura en Fahrenheit, en su 
temperatura equivalente, en grados Celsius.

Recordar que la relacion entre ambas cantidades es Tc = (5/9)(Tf - 32)

Pedirle luego, al usuario temperaturas en Fahrenheit, unas 10 e ir mostrandole 
su conversion a grados centigrados.
"""


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """
    Converts a temperature from Fahrenheit to Celsius.

    :param fahrenheit: Temperature in degrees Fahrenheit.
    :type fahrenheit: float
    :return: Temperature in degrees Celsius.
    :rtype: float
    """
    return (5 / 9) * (fahrenheit - 32)


def celsius_to_fahrenheit(celsius: float) -> float:
    """
    Converts a temperature from Celsius to Fahrenheit.

    :param celsius: Temperature in degrees Celsius.
    :type celsius: float
    :return: Temperature in degrees Fahrenheit.
    :rtype: float
    """
    return (celsius * 9 / 5) + 32


for i in range(1, 11):
    try:
        temp_f = float(input(f"[{i}/10] Enter temperature in Fahrenheit: "))

        temp_c = fahrenheit_to_celsius(temp_f)

        print(f"Result: {temp_f}ºF is equal to {temp_c:.2f}ºC\n")

    except ValueError:
        print("Invalid input. Please enter a numeric value.")
