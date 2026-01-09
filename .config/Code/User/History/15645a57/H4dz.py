"""
Crear una funcion llamada capitalizar que tome una palabra como argumento y 
devuelva una palabra con la primer letra en mayusculas, y resto de las letras 
en minusculas, de la palabra original.
"""


def capitalize(word: str) -> str:
    """
    Capitalizes the first letter of a word and converts the rest to lowercase.

    :param word: The string to be transformed.
    :type word: str
    :return: The word with the first character in uppercase and the rest in lowercase.
    :rtype: str
    """

    if not word:
        return ""

    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    first_char = word[0]
    if first_char in lower:
        index = lower.find(first_char)
        word_capitalized = upper[index]
    else:
        word_capitalized = first_char

    for i in range(1, len(word)):
        char = word[i]
        if char in upper:
            index = upper.find(char)
            word_capitalized += lower[index]
        else:
            word_capitalized += char

    return word_capitalized


def capitalize_modern(word: str) -> str:
    if not word:
        return ""

    return word[0].upper() + word[1:].lower()


def capitalize_pro(word: str) -> str:
    return word.capitalize()


print(capitalize("hELLO cHAMpiOn"))
