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
        f.write(f"{random.uniform(40.0, 110.0):.2f}\n")

with open("12/height.txt", "w") as f:
    for _ in range(50):
        f.write(f"{random.randint(140, 200)}\n")

with open("12/weight.txt", "r") as wf, open("12/height.txt", "r") as hf, open("12/bmi.txt", "w") as bf:
    w = open("12/weight.txt", "r")
    weights = w.readlines()
    h = open("12/height.txt", "r")
    heights = h.readlines

    for i in range(50):
        f.write(str(float(weights[i]) / float(heights[i] ** 2)))

    w.close()
    h.close()
