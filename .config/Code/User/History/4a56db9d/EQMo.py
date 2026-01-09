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


def inverse_piramidal(character: str, base: int) -> str:
    for i in range(base):
        print(character * base - i)
