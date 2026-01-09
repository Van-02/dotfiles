"""
Suma de Numeros Positivos y Negativos: Se requiere un programa que permita 
el ingreso de 10 numeros y al finalizar muestre en pantalla la cantidad numeros 
positivos y por otra parte la cantidad de numeros negativos que fueron ingresados.
"""

print("Please, enter 10 numbers")
numbers = []
positive_count = 0
negative_count = 0

for i in range(10):
    number = int(input(f"Number {i + 1}: "))
    numbers.append(number)
    if number >= 0:
        positive_count += 1
    else:
        negative_count += 1


print(f"The total positive numbers is: {positive_count}")
print(f"The total negative numbers is: {negative_count}")
