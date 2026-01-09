"""
Mostrar el contenido en pantalla del archivo de texto llamado fragmento
hobbit.txt. Determinar cuantas lineas de texto hay, mediante codigo, y mostrar 
en pantalla.
"""

with open("fragmento_hobbit.txt", "r", encoding="utf-8") as file:
    count = 0
    for line in file:
        print(line, end="")
        count += 1

    print(f"This file have {count} text lines.")
