"""
Crear un procedimiento que se encargue de crear un archivo de texto, con el 
nombre que se le de como argumento. Y que lo llene con 250 numeros al azar entre 
1 y 100.
"""
import random


def randoms_numbers(filename: str) -> None:
    """
    Creates a text file and fills it with 250 random integers between 1 and 100.

    :param filename: The name of the file to be created (without extension).
    :type filename: str
    :return: None
    """
    with open(f"26/{filename}.txt", "w") as f:
        for _ in range(250):
            f.write(f"{random.randint(1, 100)}\n")

    print(f"Success! File '{filename}.txt' has been created.")


randoms_numbers(filename=input("Enter a name for file: "))
