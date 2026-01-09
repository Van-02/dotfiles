"""
Permitir ingresar 10 numeros al usuario. Determinar y mostrar el menor y 
el mayor
"""


def factorial(num):
    if num == 1:
        return 1

    else:
        return num * factorial(num - 1)


print(factorial(10))
