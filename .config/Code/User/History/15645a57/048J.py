"""
Crear una funcion llamada capitalizar que tome una palabra como argumento y 
devuelva una palabra con la primer letra en mayusculas, y resto de las letras 
en minusculas, de la palabra original.
"""


def capitalize(word: str) -> str:
    import string
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    word_capitalized = ''

    for i in word:
        print(i.find(lower))

    return word_capitalized
