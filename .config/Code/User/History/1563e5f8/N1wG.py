"""
Crear una funcion que tome como argumentos una frase y una letra, y 
determine cuantas veces esta esa letra en dicha frase.
"""


def letter_count(phrase: str, letter: str) -> int:
    count = 0
    for char in phrase:
        if char == letter:
            count += 1

    return count


print(letter_count("hola mundo", "o"))
