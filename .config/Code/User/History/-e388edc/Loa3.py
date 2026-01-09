"""
Generar dos archivos diferentes, uno llamado pesos.txt que contendra 50 
valores para designar los pesos de 50 personas. Otro llamado alturas.txt que 
contendra para dichas 50 personas, las alturas en cm correspondientes. Generar 
un tercer archivo, llamado bmi.txt que tendra calculados los BMI de cada persona. 
Permitir al usuario ingresar un numero n(del 1 al 50) para mostrarle el bmi, 
traido desde el archivo de bmi.txt que ya genero usted, de la persona numero n.
"""
import random

with open("12/weight.txt", "w") as f:
    for _ in range(50):
        f.write(random.uniform(40.0, 120.0))

with open("12/height.txt", "w") as f:
    for _ in range(50):
        f.write(random.uniform(60.0, 120.0))

with open("12/bmi.txt", "w") as f:
    w = open("12/weight.txt", "r")
    weights = w.readlines()
    h = open("12/height.txt", "r")
    heights = h.readlines

    for i in range(50):
        f.write(weights[i] / heights[i] ** 2)
