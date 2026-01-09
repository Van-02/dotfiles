"""
Crear un programa que dado un archivo de texto, que contiene numeros (lo
puede generar como ud. desee) determine el valor promedio y la suma de todos
ellos.
"""
import random

with open("10/numbers.txt", "w+") as file:
    for _ in range(10):
        file.write(f"{random.randint(1, 10)}\n")

    file.seek(0)

    count = 0

    for line in file:
        if line.strip() == "5":
            count += 1

    print(f"This file have {count} fives.")
