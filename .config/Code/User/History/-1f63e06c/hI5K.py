"""
Diseñar e implementar un algoritmo que permita ingresar una serie de numeros, 
sumar todos los pares y al terminar la serie mostrar dicha suma. Si se ingreso 
algun impar, mostrar un mensaje Se ingresaron impares. Para finalizar el ingreso, 
indicar la cantidad de numeros a ingresar al principio del programa, o 
interrumpir la carga cuando se ingrese el numero 99.
"""

while (entry := int(input("Enter a number ('s' to quit): "))) != 99:
