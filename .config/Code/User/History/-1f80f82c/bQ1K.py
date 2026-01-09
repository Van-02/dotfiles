"""
Diseñar un algoritmo en pseudocodigo que permita ingresar una frase al 
usuario y una letra, y determine cuantas veces esta esa letra en dicha frase. 
Luego que ya tenga el pseudocodigo, implementarlo en Python.
"""

"""Pseudocodigo

ALGORITMO letraRepetida
    VARIABLES
        phrase: str
        letter: str
        count: int
    INICIO
        phrase = "Hola Mundo"
        letter = o
        count = 0

        PARA i EN phrase HACER
            SI i == letter ENTONCES
                count += 1
            
        MOSTRAR count

"""

phrase = input("Ingrese una frase: ")
letter = input("Ingrese una letra: ")
count = 0

for i in phrase:
    if i == letter:
        count += 1

print(f"La letra se repite {count} veces.")
