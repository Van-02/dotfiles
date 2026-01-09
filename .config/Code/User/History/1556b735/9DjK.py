"""
Crear una funcion llamada escalon, que tome un numero y devuelva 1 si este es 
positivo y 0 si este es negativo.
"""


def step(number: int) -> int:
    """
    Implementation of the Unit Step Function (Heaviside).

    :param number: The value to evaluate.
    :type number: int
    :return: 1 if the number is greater than or equal to zero, 0 otherwise.
    :rtype: int
    """
    return int(number >= 0)


val = int(input("Enter a value to test the step function: "))
result = step(val)
print(f"The step function output for {val} is: {result}")
