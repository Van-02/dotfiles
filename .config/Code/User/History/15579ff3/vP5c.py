"""
Crear una funcion llamada raiz_uno, que tome tres parametros: a, b, c. Y 
calcule solo la primera raiz de la funcion cuadratica. ¿La funcion deberia 
devolver un valor numerico entero o con decimales?
"""


def sqrt_one(a: int, b: int, c: int) -> float:
    return (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
