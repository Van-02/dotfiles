"""
Crear una funcion que tome dos palabras como parametros, y devuelva el 
texto resultante de concatenar ambas palabras.
"""


def concatenate(word_1: str, word_2: str) -> str:
    """
    Concatenate two strings into one.

    :param word_1: The prefix or first part of the string.
    :type word_1: str
    :param word_2: The suffix or second part of the string.
    :type word_2: str
    :return: A single string containing both inputs joined together.
    :rtype: str
    """
    return word_1 + word_2
