"""
Crear una funcion llamada capitalizar que tome una palabra como argumento y 
devuelva una palabra con la primer letra en mayusculas, y resto de las letras 
en minusculas, de la palabra original.
"""


def capitalize(word: str) -> str:
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    word_capitalized: ''

    if word[0] in lower:
        index = lower.find(word[0])
        word_capitalized += upper[index]


capitalize("hola")
