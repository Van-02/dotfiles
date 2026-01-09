"""
Crear un programita que permita elegir un color de una lista de 10 colores.
Por defecto, el programa la primera vez que se inicia, empieza mostrando el 
color en pantalla azul (como texto, 'azul'), luego, cada vez que el programa sea
ejecutado mostrara en pantalla el color que el usuario habia seleccionado en la
ejecucion anterior del programa.
"""
from pathlib import Path

default = 'blue'

colours_list = ['red', 'green', 'blue', 'black',
                'violet', 'orange', 'brown', 'grey', 'yellow', 'rose']

file = Path("11/11.conf")

if not file.exists():
    with open(file, "w") as f:
        f.write(f'colour = {default}')
        print(default)

else:
    print(colours_list)
    user_input = input("Enter a colour of list: ")

    if user_input not in colours_list:
        print("Colour not avaible.")
        quit()

    with open(file, "w") as f:
        f.write(f"colour = {user_input}")
