"""
Crear una funcion llamada escalon, que tome un numero y devuelva 1 si este es 
positivo y 0 si este es negativo.
"""


def step(number: int) -> int:
    return int(number >= 0)


print(step(number=int(input("Enter a number: "))))
