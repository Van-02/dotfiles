"""
Crear un procedimiento que tome como parametro el nombre de un archivo de 
texto, y determine la cantidad de caracteres que tiene este, por linea, 
generando un archivo nuevo de texto, donde guardara la longitud seguida de la 
linea en cuestion, separados por punto y coma.
"""


def create_file(filename: str):
    with open(f"31/{filename}.txt", "r") as fr, open("31/test01.txt", "w") as fw:
        for line in fr:
            print(line.strip())


create_file("test00")
