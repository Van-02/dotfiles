"""
Mostrar el contenido en pantalla del archivo de texto llamado fragmento
hobbit.txt. Determinar cuantas lineas de texto hay, mediante codigo, y mostrar 
en pantalla.
"""

with open("fragmento_hobbit.txt", "r") as file:
    content = file.read()
    print(content)
