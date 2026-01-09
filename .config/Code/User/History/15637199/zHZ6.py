"""
Crear ahora una segunda funcion, que tome un tercer argumento extra, y haga 
lo mismo que la funcion del punto anterior, pero esta vez, utilizando el tercer 
argumento para saber si debe agregar o no un espacio entre medio de las dos 
palabras a concatenar. ¿Que tipo de dato utilizaria para ese tercer argumento?
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
