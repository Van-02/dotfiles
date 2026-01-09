"""
Crear una funcion logica (funcion que retorna un valor logico) que determine
si un numero entero es par o impar.
"""


def even_odd(number: int) -> bool:
    return number % 2 == 0


# Tests
print(even_odd(2))
print(even_odd(5))
print(even_odd(0))
