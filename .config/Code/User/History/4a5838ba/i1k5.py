"""
Desarrollar una funcion que dados cinco numeros, recibidos por parametro, 
devuelva el promedio de ellos. Se puede generalizar para n parametros devolviendo 
el promedio de los mismos.
"""


def average(*numbers: float) -> float:
    if not numbers:
        return 0.0

    return sum(numbers) / len(numbers)


# Tests
print(average(7, 6, 5, 3, 10))
