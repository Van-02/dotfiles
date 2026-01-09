"""
Crear un programa que genere un archivo de texto llamado numeros.txt con
10 numeros enteros guardados en el mismo, uno por linea
"""

with open("07/numeros.txt", "w") as file:
    for i in range(10):
        file.write(str(i) + "\n")
