"""
Crear una funcion que tome tres numeros como parametros n, a, b, y devuelva 
verdadero o falso, segun n pertenece o no al intervalo cerrado [a, b]
"""


def in_interval(n: int, a: int, b: int) -> bool:
    if a < b:
        return n in range(a, b + 1)
    else:
        return n in range(b, a + 1)
