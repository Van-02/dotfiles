"""
Con la funcion creada en el ejercicio anterior, elabore un programa en donde 
se ingresa un caracter y 10 palabras; y muestre la cantidad total de veces que 
aparecio el caracter en las 10 palabras.
"""


def letter_repeat(string: str, letter: str) -> int:
    """
    Counts how many times a letter appears in a string.

    :param string: The text to search within.
    :type string: str
    :param letter: The specific character to count.
    :type letter: str
    :return: The total number of occurrences.
    :rtype: int
    """
    return string.count(letter)
