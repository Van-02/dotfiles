"""
Crear un programa que permita ingresar un numero en base 2 y lo convierta a 
base 10.
"""


def binary_to_decimal(number: str) -> str:
    """
    Converts a base-2 integer to decimal base.
    """
    power = len(number)

    digits = []
    for i in number:
        digits.append(int(i) * (2 ** power))
        power -= 1

    return sum(digits)


print(binary_to_decimal("1011"))
