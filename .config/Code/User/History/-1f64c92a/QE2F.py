"""
Suma de Numeros Positivos y Negativos: Se requiere un programa que permita 
el ingreso de 10 numeros y al finalizar muestre en pantalla la cantidad numeros 
positivos y por otra parte la cantidad de numeros negativos que fueron ingresados.
"""

print("Please, enter 10 numbers")
numbers = []

for i in range(10):
    number = int(input(f"Number {i + 1}: "))
    numbers.append(number)
