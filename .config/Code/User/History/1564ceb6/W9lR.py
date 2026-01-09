"""
Crear una funcion que tome una lista de valores numericos como argumento, 
de dos elementos nada mas, y devuelva la lista ordenada. En el caso de Python, 
¿Necesito utilizar una segunda lista, auxiliar para modificarla, o pudo devolver 
la lista original, el argumento que recibio, modificado y ordenado?
"""


def sort(list_numbers: list) -> list:
    if list_numbers[0] < list_numbers[1]:
        return list_numbers
    else:
        return list_numbers[::-1]


print(sort([2, 20]))
