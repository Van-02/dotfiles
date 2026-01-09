"""
Crear una funcion que tome una palabra y devuelva la cantidad de vocales que 
tiene. Por ejemplo, si se le da el siguiente argumento a la funcion: 'hola' la 
funcion deberia devolver 2.
"""


def vowels_len(word: str) -> int:
    """
    Counts the number of lowercase vowels in a given string.

    :param word: The string to be analyzed.
    :type word: str
    :return: The total count of vowels (a, e, i, o, u) found.
    :rtype: int
    """
    vowels = 'aeiouAEIOU'
    count = 0

    for char in word:
        if char in vowels:
            count += 1

    return count
