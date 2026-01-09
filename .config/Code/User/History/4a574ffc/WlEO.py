"""
Crear una funcion es_primo, que reciba un numero entero como parametro y 
devuelva verdadero si es un numero primo o falso en caso contrario.
"""
import math


def is_prime(number: int) -> bool:
    """
    Determines if an integer is a prime number.

    :param number: The number to check.
    :type number: int
    :return: True if prime, False otherwise.
    :rtype: bool
    """
    # Base case
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    limit = int(math.sqrt(number))
    for i in range(3, limit + 1, 2):
        if number % i == 0:
            return False

    return True


# Tests
print(f"¿Es 7 primo? {is_prime(7)}")   # True
print(f"¿Es 15 primo? {is_prime(15)}")  # False
