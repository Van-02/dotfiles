"""
Realizar una funcion que tome dos numeros: a, b y devuelva la cantidad de 
numeros pares que hay en el intervalo cerrado [a, b]. Controlar que a <= b.
"""


def count_evens(a: int, b: int) -> int:
    """
    Counts the number of even integers in the closed interval [a, b].

    :param a: Lower bound of the interval.
    :type a: int
    :param b: Upper bound of the interval.
    :type b: int
    :return: Total count of even numbers.
    :raises ValueError: If a is greater than b.
    :rtype: int
    """
    if a > b:
        raise ValueError(
            "The lower bound 'a' must be less than or equal to 'b'.")

    return sum(1 for i in range(a, b + 1) if i % 2 == 0)


try:
    print(f"Evens found: {count_evens(1, 10)}")
except ValueError as e:
    print(e)
