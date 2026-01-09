"""
Crear un programa que dado un archivo de numeros con valores entre 1 y 10
(lo puede generar como ud. desee) determine cuantos numeros iguales a 5 hay en
el archivo.
"""
import random

with open("09/numbers.txt", "w+") as file:
    for _ in range(10):
        file.write(str(random.randint(1, 10)) + '\n')

    file.seek(0)
    count = 0
    lines = file.readlines()
    print(lines)
    for line in lines:
        if line == "5":
            count += 1

    print(f"This file have {count} fives.")
