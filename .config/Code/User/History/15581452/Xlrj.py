"""
Crear una funcion que tome tres numeros como parametros n, a, b, y devuelva 
verdadero o falso, segun n pertenece o no al intervalo cerrado [a, b]
"""


def in_interval(n: int, a: int, b: int) -> bool:
    """
    Checks if a number in close inverval [a, b]

    :param n: Number to search in interval
    :type n: int
    :param a: Begin of close interval
    :type a: int
    :param b: End of close interval
    :type b: int
    :return: True if number in close interval, False otherwise
    :rtype: bool
    """
    lower_limit = min(a, b)
    upper_limit = max(a, b)

    return lower_limit <= n <= upper_limit
