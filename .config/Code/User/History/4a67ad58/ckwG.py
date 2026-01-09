"""
Crear un programa que permita al usuario ingresar un numero en base 10 y lo
devuelva en base binaria.
"""


def decimal_to_binary(number: int) -> str:
    """
    Converts a base-10 integer to a binary string.
    """
    # Usamos [2:] para quitar el prefijo '0b'
    return bin(number)[2:]


# Test
print(decimal_to_binary(16))  # Resultado: 10000
