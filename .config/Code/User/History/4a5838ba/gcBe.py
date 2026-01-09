"""
Desarrollar una funcion que dados cinco numeros, recibidos por parametro, 
devuelva el promedio de ellos. Se puede generalizar para n parametros devolviendo 
el promedio de los mismos.
"""


def average(num1: int, num2: int, num3: int, num4: int, num5: int) -> float:
    return sum(num1, num2, num3, num4, num5) / 5


# Tests
print(average(7, 6, 5, 3, 10))
