"""
Crear un programa que dado un archivo de texto, que contiene numeros (lo
puede generar como ud. desee) determine el valor promedio y la suma de todos
ellos.
"""
import random

with open("10/numbers.txt", "w+") as file:
    for _ in range(5):
        file.write(f"{random.randint(1, 10)}\n")

    file.seek(0)

    numbers = [int(line.strip()) for line in file]

    total_sum = sum(numbers)
    average = total_sum / len(numbers)
