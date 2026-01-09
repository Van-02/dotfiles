"""
Diseñar e implementar un algoritmo que permita ingresar una serie de numeros, 
sumar todos los pares y al terminar la serie mostrar dicha suma. Si se ingreso 
algun impar, mostrar un mensaje Se ingresaron impares. Para finalizar el ingreso, 
indicar la cantidad de numeros a ingresar al principio del programa, o 
interrumpir la carga cuando se ingrese el numero 99.
"""

even_sum = 0
has_odd = False

while (entry := int(input("Enter a number ('99' to quit): "))) != 99:
    if entry % 2 == 0:
        even_sum += entry
    elif entry % 2 != 0:
        impar = True

if impar:
    print("Se ingresaron impares")
    print(f"The sum of all even numbers is: {even_sum}")
else:
    print(f"The sum of all even numbers is: {even_sum}")
