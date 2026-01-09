"""
Desarrollar una funcion que retorne la posicion de un caracter (la primera vez 
que aparezca) dentro de la cadena de N caracteres de longitud, donde se reciben 
como parametro la cadena y el caracter respectivamente.
"""


def position(string: str, character: str) -> int:
    for i in range(len(string)):
        if string[i] == character:
            return i


# Tests
print(position("Hola master como estas?", "a"))
