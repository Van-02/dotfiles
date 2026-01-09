"""
Crear una funcion llamada iguales, que tome dos palabras como parametros, y 
determine si son iguales o no. Devolviendo verdadero (true) si lo son, o falso 
(false) en caso contrario.
"""


def equals(word_1: str, word_2: str) -> bool:
    """
    Verify if both words are equal

    :type word_1: str
    :type word_2: str
    :rtype: bool
    """
    return word_1.lower() == word_2.lower()


word_1 = input("Enter the first word: ")
word_2 = input("Enter the second word: ")
result = equals(word_1, word_2)

print(f"Are both words equal? {result}")
