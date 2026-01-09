"""
Pida un numero al usuario, mayor que 1 y menor a 50. Muestre en pantalla los 
numeros de 1 hasta ese numero ingresado, uno por linea.
"""

number = int(input("Ingrese un numero: "))

if number < 1 or number > 50:
    print("Ingrese un numero mayor que 1 y menor a 50")
    quit()

for i in range(number + 1):
    print(i)
