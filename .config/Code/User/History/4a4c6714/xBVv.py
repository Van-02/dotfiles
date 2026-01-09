"""
Con la funcion creada en el ejercicio anterior, elabore un programa en donde 
se ingresa un caracter y 10 palabras; y muestre la cantidad total de veces que 
aparecio el caracter en las 10 palabras.
"""


def letter_repeat(words: list, letter: str) -> int:
    """
    Counts the total occurrences of a letter across a list of words.

    :param words: List of strings to search within.
    :type words: list
    :param letter: The specific character to count.
    :type letter: str
    :return: The total sum of occurrences.
    :rtype: int
    """
    count = 0

    for word in words:
        count += word.count(letter)

    return count


words = []

for i in range(10):
    word = input("Enter a word: ")
    words.append(word)

letter = input("Enter a letter: ")

print(letter_repeat(words, letter))
