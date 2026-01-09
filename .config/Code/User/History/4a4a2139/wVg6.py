"""
Crear una funcion que reciba un numero como parametro el cual representa el 
lado de un cuadrado y muestre en pantalla el perimetro y la superficie del 
mismo.
"""


def perimeter_area(side: int):
    perimeter = 4 * side
    area = side ** 2
    return perimeter, area


square = perimeter_area(5)

print(f"Perimeter: {square[0]}\nArea: {square[1]}")
