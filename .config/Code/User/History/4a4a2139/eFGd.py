"""
Crear una funcion que reciba un numero como parametro el cual representa el 
lado de un cuadrado y muestre en pantalla el perimetro y la superficie del 
mismo.
"""


def perimeter_area(side: int) -> tuple:
    """
    Calculate perimeter and area from side square.

    :param side: side of square
    :type side: int
    :return: (perimeter, area) in form tuple.
    """
    perimeter = 4 * side
    area = side ** 2
    return perimeter, area


p, a = perimeter_area(5)

print(f"Perimeter: {p}\nArea: {a}")
