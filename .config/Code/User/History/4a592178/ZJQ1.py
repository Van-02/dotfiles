"""
Desarrollar una funcion que retorne la posicion de un caracter (la primera vez 
que aparezca) dentro de la cadena de N caracteres de longitud, donde se reciben 
como parametro la cadena y el caracter respectivamente.
"""


def position(text: str, target: str) -> int:
    """
    Returns the index of the first occurrence of a character.

    :param text: The string to search.
    :type text: str
    :param target: The character to find.
    :type target: str
    :return: The index (starting at 0) or -1 if not found.
    :rtype: int
    """
    for i in range(len(text)):
        if text[i] == target:
            return i

    return -1


# Tests
print(position("Hola master como estas?", "a"))
