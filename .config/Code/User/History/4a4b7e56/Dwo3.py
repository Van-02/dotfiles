"""
Escriba una funcion que calcule la enesima potencia de un numero, recibiendo 
como parametro un numero real base y otro entero llamado exponente.
La definicion de la funcion es: y = x**n donde x representa la base y n representa 
el exponente.
Nota: tener en cuenta que n puede ser un numero negativo.
Ejemplo: 2 ** 3 = 8 y 2 ** -3 = 0.125
"""


def power(number: float, exponent: float) -> float:
    """
    Calculate the n-th power of a real number.

    :param number: The base number to be multiplied.
    :type number: float
    :param exponent: The power to which the base is raised.
    :type exponent: float
    :return: The result of number raised to the exponent.
    :rtype: float
    """
    return number ** exponent


print(power(2, 3))
print(power(2, -3))
