"""
Crear una funcion que tome tres numeros como parametros n, a, b, y devuelva 
verdadero o falso, segun n pertenece o no al intervalo cerrado [a, b]
"""


def in_interval(n: int, a: int, b: int) -> bool:
    lower_limit = min(a, b)
    upper_limit = max(a, b)

    # Comparación encadenada: eficiente y compatible con decimales
    return lower_limit <= n <= upper_limit
