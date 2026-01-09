"""
Implemente el algoritmo del punto anterior en Python, pidiendo un numero al 
usuario para determinar si es par o impar.
"""

number = int(input("Ingrese un numero: "))

if number % 2 == 0:
    print("Es par")
else:
    print("Es impar")
