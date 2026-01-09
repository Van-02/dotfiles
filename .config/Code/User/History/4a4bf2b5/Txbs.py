"""
Crear una funcion que reciba una cadena de caracteres y una letra como 
parametros, y devuelva la cantidad de veces que dicha letra aparece en la 
cadena. Por ejemplo, si la cadena es 'Barcelona' y la letra es 'a', deberia 
devolver 2 (aparece 2 veces).
"""


def letter_repeat(string: str, letter: str) -> int:
    """Counts how many times a letter appears in a string.

    Args:
        string (str): The text to search within.
        letter (str): The specific character to count.

    Returns:
        int: The total number of occurrences found.
    """
    return string.count(letter)
