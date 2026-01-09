"""
Crear una funcion que tome una lista de valores numericos como argumento, 
de dos elementos nada mas, y devuelva la lista ordenada. En el caso de Python, 
¿Necesito utilizar una segunda lista, auxiliar para modificarla, o pudo devolver 
la lista original, el argumento que recibio, modificado y ordenado?
"""


def sort(numbers: list[int]) -> list:
    """
    Returns a sorted version of a list containing two elements.

    :param numbers: A list of two numeric values.
    :type numbers: list
    :return: A new sorted list.
    :rtype: list
    """

    if numbers[0] > numbers[1]:
        numbers[0], numbers[1] = numbers[1], numbers[0]

    return numbers


print(sort([2, 20]))
print(sort([20, 2]))


"""
En Python no necesitas una lista auxiliar, pero hay una distinción importante que todo programador debe conocer entre modificar la lista original o devolver una nueva.
"""
