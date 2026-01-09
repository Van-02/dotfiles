"""
Crear ahora una segunda funcion, que tome un tercer argumento extra, y haga 
lo mismo que la funcion del punto anterior, pero esta vez, utilizando el tercer 
argumento para saber si debe agregar o no un espacio entre medio de las dos 
palabras a concatenar. ¿Que tipo de dato utilizaria para ese tercer argumento?
"""


def concatenate(word_1: str, word_2: str, space: bool) -> str:
    """
    Concatenate two strings into one.

    :param word_1: The prefix or first part of the string.
    :type word_1: str
    :param word_2: The suffix or second part of the string.
    :type word_2: str
    :param space: If True, adds a space between words. If False, joins them directly.
    :type space: bool
    :return: A single string containing both inputs joined together.
    :rtype: str
    """
    separator = " " if space else ""
    return word_1 + separator + word_2


print(concatenate("Hola", "Mundo", True))
print(concatenate("Anti", "Social", False))
