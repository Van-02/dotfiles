"""
Crear una funcion que tome como argumentos una frase y una letra, y 
determine cuantas veces esta esa letra en dicha frase.
"""


def letter_count(phrase: str, letter: str) -> int:
    """
    Counts the occurrences of a specific letter within a phrase.

    :param phrase: The text to be searched.
    :type phrase: str
    :param letter: The character to count.
    :type letter: str
    :return: Total number of times the letter appears in the phrase.
    :rtype: int
    """
    count = 0
    for char in phrase:
        if char == letter:
            count += 1

    return count


print(letter_count("hola mundo", "o"))
