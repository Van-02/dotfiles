"""
Permitir ingresar 10 numeros al usuario. Determinar y mostrar el menor y 
el mayor
"""
from math import sqrt


def factorial(num):
    if num == 1:
        return 1

    else:
        return num * factorial(num - 1)


print(factorial(10))


def cuadratica(a, b, c):
    valor_1 = (a + sqrt(-b ** 2 - 4 * a * c)) / -2 * a
