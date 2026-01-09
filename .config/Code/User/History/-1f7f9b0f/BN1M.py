"""
Permita al usuario ingresar el nombre de un archivo, genere un nuevo nombre 
donde los espacios sean reemplazados por guion bajo y la extension por numerales.
"""

name_file = input("Ingrese un nombre de archivo: ")
new_name_file = ""

for i in name_file:
    while i != ".":
        if i != " " and i != ".":
            new_name_file += i
        elif i == " ":
            new_name_file += "_"

    new_name_file += "#"
