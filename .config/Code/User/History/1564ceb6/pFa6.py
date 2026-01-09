"""
Crear una funcion que tome una lista de valores numericos como argumento, 
de dos elementos nada mas, y devuelva la lista ordenada. En el caso de Python, 
¿Necesito utilizar una segunda lista, auxiliar para modificarla, o pudo devolver 
la lista original, el argumento que recibio, modificado y ordenado?
"""


def sort(numbers: list) -> list:
    if numbers[0] > numbers[1]:
        numbers[0], numbers[1] = numbers[1], numbers[0]

    return numbers


print(sort([2, 20]))
