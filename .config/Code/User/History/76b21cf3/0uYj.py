"""
Realizar un programa que lea 2 numeros enteros desde teclado e informe en 
pantalla cual de los dos numeros es el mayor. Si son iguales debe informar en
pantalla lo siguiente: "Los numeros leidos son iguales"
"""
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))

if a == b:
    "Los numeros leidos son iguales"
elif a > b:
    print(f"El numero mas grande es {a}")
elif a < b:
    print(f"El numero mas grande es {b}")
