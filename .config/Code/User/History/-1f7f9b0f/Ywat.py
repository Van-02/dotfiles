"""
Permita al usuario ingresar el nombre de un archivo, genere un nuevo nombre 
donde los espacios sean reemplazados por guion bajo y la extension por numerales.
"""

name_file = input("Ingrese un nombre de archivo: ")
new_name_file = ""

for i in range(len(name_file)):
    if name_file[i] == ".":
        break
    elif name_file[i] == " ":
        new_name_file += "_"
    else:
        new_name_file += name_file[i]

print(new_name_file)
