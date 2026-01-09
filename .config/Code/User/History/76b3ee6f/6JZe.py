"""
Realizar un programa que permita al usuario ingresar dos numeros enteros y 
ordenarlos de menor a mayor. Mostrarlos luego en pantalla.
"""

number_1 = int(input("Ingrese el primer numero: "))
number_2 = int(input("Ingrese el segundo numero: "))

if number_1 > number_2:
    print("Ordenados de menor a mayor: ", number_2, ",", number_1)
else:
    print("Ordenados de menor a mayor: ", number_1, ",", number_2)
