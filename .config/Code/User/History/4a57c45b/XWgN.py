"""
Crear una funcion que dados dos valores distintos, ingresados por parametro, 
devuelva el mayor de ellos.
"""


def higher(num1: int, num2: int) -> int:
    if num1 == num2:
        return num1
    elif num1 > num2:
        return num1

    return num2


# Tests
print(higher(2, 4))
print(higher(5, 2))
print(higher(2, 2))
