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
    weights = wf.readlines()
    heights = hf.readlines()

    for i in range(50):
        w = float(weights[i].strip())
        h = float(heights[i].strip())  # cm

        # weight / height ** 2
        h_m = h / 100   # m
        bmi = w / (h_m ** 2)

        bf.write(f"{bmi:.2f}\n")

try:
    n = int(input("Enter person number to check (1-50): "))
    if 1 <= n <= 50:
        with open("12/bmi.txt", "r") as bf:
            all_bmis = bf.readlines()
            print(f"The BMI for person #{n} is: {all_bmis[n-1].strip()}")
    else:
        print("Please enter a number between 1 and 50.")
except ValueError:
    print("Invalid input. Please enter a number.")
