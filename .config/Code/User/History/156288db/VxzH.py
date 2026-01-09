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
