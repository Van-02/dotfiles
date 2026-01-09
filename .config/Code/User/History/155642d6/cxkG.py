"""
Crear una funcion llamada signo, que tome un numero y devuelva 1 si este es 
positivo y -1 si este es negativo.
"""


def sign(number: int) -> int:
    if number >= 0:
        return 1
    else:
        return -1


print(sign(number=int(input("Ingrese un numero: "))))
