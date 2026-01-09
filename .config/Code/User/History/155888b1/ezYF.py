"""
Crear una funcion que tome una palabra y devuelva la cantidad de vocales que 
tiene. Por ejemplo, si se le da el siguiente argumento a la funcion: 'hola' la 
funcion deberia devolver 2.
"""


def vocals_len(word: str) -> int:
    vocals = 'aeiou'
    count = 0

    for char in word:
        if char in vocals:
            count += 1

    return count
