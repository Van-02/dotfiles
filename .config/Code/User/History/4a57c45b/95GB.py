"""
Crear una funcion que dados dos valores distintos, ingresados por parametro, 
devuelva el mayor de ellos.
"""


def higher(num1: int, num2: int) -> int:
    """
    Returns the higher of two numbers.

    :param num1: First number to compare.
    :param num2: Second number to compare.
    :return: The larger of the two values.
    """
    return num1 if num1 > num2 else num2


# Tests
print(higher(2, 4))
print(higher(5, 2))
print(higher(2, 2))
