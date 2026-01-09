"""
Crear un procedimiento que se encargue de crear un archivo de texto, con el 
nombre que se le de como argumento. Y que lo llene con 250 numeros al azar entre 
1 y 100.
"""
import random


def randoms_numbers(namefile: str) -> None:
    with open(f"26/{namefile}.txt", "w") as f:
        for _ in range(250):
            f.write(str(random.randint(1, 100)))


randoms_numbers(namefile=input("Enter a name for file: "))
