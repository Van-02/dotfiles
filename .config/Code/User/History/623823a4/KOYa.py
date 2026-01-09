"""
Crear una segunda version del procedimiento anterior, que ahora tome dos 
parametros extras, a y b para poder indicarle el intervalo de valores que se 
desean para los numeros al azar. O sea, ahora el procedimiento generara un 
archivo de texto, del nombre que se le de, con valores al azar en [a, b].
"""
import random


def randoms_numbers(filename: str, a: int, b: int) -> None:
    """
    Creates a text file and fills it with 250 random integers between 1 and 100.

    :param filename: The name of the file to be created (without extension).
    :type filename: str
    :return: None
    """
    with open(f"27/{filename}.txt", "w") as f:
        for _ in range(250):
            f.write(f"{random.randint(a, b)}\n")

    print(f"Success! File '{filename}.txt' has been created.")


randoms_numbers(filename=input("Enter a name for file: "), a=0, b=250)
