"""
Realizar un programa que permita al usuario ingresar 3 numeros, ordenarlos y 
mostrarlos luego en pantalla de menor a mayor.
"""

num_1 = int(input("Ingrese el primer numero: "))
num_2 = int(input("Ingrese el segundo numero: "))
num_3 = int(input("Ingrese el tercer numero: "))

low = None
mid = None
high = None

if num_1 > num_2 and num_1 > num_3:
    high = num_1
    if num_2 > num_3:
        mid = num_2
        low = num_3
    else:
        mid = num_3
        low = num_2

elif num_2 > num_1 and num_2 > num_3:
    high = num_2
    if num_1 > num_3:
        mid = num_1
        low = num_3
    else:
        mid = num_3
        low = num_1

elif num_3 > num_1 and num_3 > num_2:
    high = num_3
    if num_1 > num_2:
        mid = num_1
        low = num_2
    else:
        mid = num_2
        low = num_1

print(f"Los numeros ordenados de menor a mayor: {low}, {mid}, {high}")
