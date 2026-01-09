"""
Crear una funcion llamada signo, que tome un numero y devuelva 1 si este es 
positivo y -1 si este es negativo.
"""


def sign(number: int) -> int:
    """
    Determines the sign of a number.

    :param number: The integer to be evaluated
    :type number: int
    :return: 1 if positive and -1 if negative
    :rtype: int
    """
    if number >= 0:
        return 1
    else:
        return -1


print(sign(number=int(input("Enter a number: "))))
