"""
Con la funcion creada en el ejercicio anterior, elabore un programa en donde 
se ingresa un caracter y 10 palabras; y muestre la cantidad total de veces que 
aparecio el caracter en las 10 palabras.
"""


def letter_repeat(words: list, letter: str) -> int:
    """
    Counts how many times a letter appears in a string.

    :param string: The text to search within.
    :type string: str
    :param letter: The specific character to count.
    :type letter: str
    :return: The total number of occurrences.
    :rtype: int
    """
    count = 0

    for i in words:
        if i == letter:
            count += 1

    return count


words = []

for i in range(10):
    word = input("Enter a word: ")
    words.append(word)

letter = input("Enter a letter: ")

print(letter_repeat(words, letter))
