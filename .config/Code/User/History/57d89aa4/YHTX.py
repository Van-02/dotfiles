"""
Crear un procedimiento que permita tomar dos parametros, el nombre de un 
archivo de texto, y una frase. Debera agregar al final de dicho archivo, la 
frase que ha recibido.
"""


def append_text(filename: str, phrase: str) -> None:
    """
    Appends a phrase to the end of a text file on a new line.

    :param filename: The name of the file (without extension).
    :param phrase: The text to add to the file.
    """
    try:
        with open(f"30/{filename}.txt", "a") as f:
            f.write(phrase + "\n")
    except FileNotFoundError:
        print(f"Error: The file {filename}.txt was not found.")


filename = "test"
phrase = input("Enter a phrase: ")
append_text(filename, phrase)
