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


def fibonacci(num):
    if num == 0 or num == 1:
        return num

    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


print(fibonacci(10))
