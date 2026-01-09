"""
Crear un procedimiento que tome como parametro el nombre de un archivo de 
texto, y determine la cantidad de caracteres que tiene este, por linea, 
generando un archivo nuevo de texto, donde guardara la longitud seguida de la 
linea en cuestion, separados por punto y coma.
"""


def process_line_lengths(filename: str):
    """
    Reads a file and creates a new one with the length of each line prepended.

    :param input_filename: Name of the source file (without extension).
    """
    with open(f"31/{filename}.txt", "r") as fr, \
            open("31/test01.txt", "w") as fw:

        for line in fr:
            fw.write(f"{len(line.strip())}; {line.strip()}\n")


process_line_lengths("test00")
