"""
Crear una funcion que reciba una cadena de caracteres y una letra como 
parametros, y devuelva la cantidad de veces que dicha letra aparece en la 
cadena. Por ejemplo, si la cadena es 'Barcelona' y la letra es 'a', deberia 
devolver 2 (aparece 2 veces).
"""


def letter_repeat(string: str, letter: str) -> int:
    count = 0
    for i in string:
        if i == letter:
            count += 1

    return count


print(letter_repeat("Barcelona", "a"))
