"""
Crear una funcion que convierta una temperatura en Fahrenheit, en su 
temperatura equivalente, en grados Celsius.

Recordar que la relacion entre ambas cantidades es Tc = (5/9)(Tf - 32)

Pedirle luego, al usuario temperaturas en Fahrenheit, unas 10 e ir mostrandole 
su conversion a grados centigrados.
"""


def fahrenheit_to_celsius(grades: float) -> float:
    return (5 / 9) * (grades - 32)


def celsius_to_fahrenheit(grades: float) -> float:
    return grades / (5 / 9) + 32
