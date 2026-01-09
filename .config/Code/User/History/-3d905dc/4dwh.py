"""
Crear un programa que dado un archivo de numeros con valores entre 1 y 10
(lo puede generar como ud. desee) determine cuantos numeros iguales a 5 hay en
el archivo.
"""
import random

with open("09/numbers.txt", "r+") as file:
    for _ in range(10):
        file.write(str(random.randint(1, 10)) + '\n')
