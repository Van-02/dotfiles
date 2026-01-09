"""
Desarrollar una funcion que dados cinco numeros, recibidos por parametro, 
devuelva el promedio de ellos. Se puede generalizar para n parametros devolviendo 
el promedio de los mismos.
"""


def average(*numbers: float) -> float:
    """
    Calculates the average of any number of parameters.

    :param numbers: Variable length argument list of numbers.
    :return: The arithmetic mean of the numbers.
    :rtype: float
    """
    if not numbers:
        return 0.0

    return sum(numbers) / len(numbers)


# Tests
print(average(7, 6, 5, 3, 10))
print(average(10, 20))
print(average(1, 2, 3, 4, 5, 6))
