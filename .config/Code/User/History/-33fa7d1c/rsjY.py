"""
Crear una funcion que tome dos parametros, el nombre de un archivo de texto, 
y una palabra a buscar. La funcion retornara verdadero o falso segun encuentre o 
no dicha palabra dentro del contenido del archivo.
"""


def search_word(filename: str, word: str) -> bool:
    """
    Searches for a word within a text file.

    :param filename: Name of the file (without extension).
    :type filename: str
    :param word: The string to search for.
    :type word: str
    :return: True if found, False otherwise.
    :rtype: bool
    """

    with open(f"29/{filename}.txt", "r") as f:
        content = f.read()
        return word in content


# Tests
filename = input("Enter a filename: ")
word = input(f"Enter a word to search in the file {filename}: ")
print(search_word(filename, word))
