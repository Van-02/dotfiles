"""
Crear una funcion llamada escribir tabla multiplicar, que reciba como 
parametro un numero entero, y escriba la tabla de multiplicar de ese numero 
(por ejemplo, para el 3 debera mostrar desde 3x0=0 hasta 3x10=30).
"""


def multiply_table(number: int) -> dict:
    table = {f"{number} x 0": number * 0,
             f"{number} x 1": number * 1,
             f"{number} x 2": number * 2,
             f"{number} x 3": number * 3,
             f"{number} x 4": number * 4,
             f"{number} x 5": number * 5,
             f"{number} x 6": number * 6,
             f"{number} x 7": number * 7,
             f"{number} x 8": number * 8,
             f"{number} x 9": number * 9,
             f"{number} x 10": number * 10
             }
