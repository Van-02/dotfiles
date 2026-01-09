"""
Crear una funcion llamada escribir tabla multiplicar, que reciba como 
parametro un numero entero, y escriba la tabla de multiplicar de ese numero 
(por ejemplo, para el 3 debera mostrar desde 3x0=0 hasta 3x10=30).
"""


def multiply_table(number: int) -> dict:
    """
    Show in screen the multiply table from number input.

    :param number: The number to analize.
    :type number: int
    """
    print(f"--- Table of {number} ---")

    for i in range(11):
        print(f"{number} x {i} = {number * i}")
