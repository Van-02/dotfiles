"""
Realizar una funcion que tome dos numeros: a, b y devuelva la cantidad de 
numeros pares que hay en el intervalo cerrado [a, b]. Controlar que a <= b.
"""


def even_count(a: int, b: int) -> int:
    count = 0
    if a <= b:
        for i in range(a, b + 1):
            if i % 2 == 0:
                count += 1
    else:
        return None
