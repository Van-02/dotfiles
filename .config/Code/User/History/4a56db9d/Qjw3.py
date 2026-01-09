"""
Crear una funcion que reciba un caracter y un numero como parametros e 
imprima en pantalla un triangulo formado por ese caracter que tenga como ancho 
inicial el numero recibido como parametro.
Por ejemplo, si el caracter es * y el ancho es 4, deberia escribir:

****
***
**
*

"""


def inverse_piramidal(character: str, base: int) -> None:
    """
    Prints an inverted triangle using a specific character.

    :param character: The character used to build the triangle.
    :type character: str
    :param base: The initial width of the triangle (number of characters).
    :type base: int
    :return: None (prints directly to console).
    :rtype: None
    """
    for i in range(base):
        print(character * (base - i))


# Tests
inverse_piramidal("*", 4)
inverse_piramidal("#", 8)
inverse_piramidal("+", 2)
