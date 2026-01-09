"""
Crear una funcion que tome tres numeros como parametros n, a, b, y devuelva 
verdadero o falso, segun n pertenece o no al intervalo cerrado [a, b]
"""


def in_interval(n: int, a: int, b: int) -> bool:
    """
    Checks if a number n belongs to the closed inverval [a, b].

    :param n: The number to check
    :type n: int
    :param a: The first boundary of the interval.
    :type a: int
    :param b: The second boundary of the interval.
    :type b: int
    :return: True if n is within the interval, False otherwise
    :rtype: bool
    """
    lower_limit = min(a, b)
    upper_limit = max(a, b)

    return lower_limit <= n <= upper_limit
