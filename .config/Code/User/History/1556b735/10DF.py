"""
Crear una funcion llamada escalon, que tome un numero y devuelva 1 si este es 
positivo y 0 si este es negativo.
"""


def step(number: int) -> int:
    if number >= 0:
        return 1
    else:
        return 0


print(step(number=int(input("Enter a number: "))))
