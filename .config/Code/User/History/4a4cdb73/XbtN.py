"""
Crear una funcion logica (funcion que retorna un valor logico) que determine
si un numero entero es par o impar.
"""


def is_even(number: int) -> bool:
    """
    Check if a number is even.

    :param number: The integer to check.
    :type number: int
    :return: True if the number is even, False otherwise.
    :rtype: bool
    """
    return number % 2 == 0


# Tests
print(is_even(2))
print(is_even(5))
print(is_even(0))
