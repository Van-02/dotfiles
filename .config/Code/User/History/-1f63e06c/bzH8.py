"""
Diseñar e implementar un algoritmo que permita ingresar una serie de numeros, 
sumar todos los pares y al terminar la serie mostrar dicha suma. Si se ingreso 
algun impar, mostrar un mensaje Se ingresaron impares. Para finalizar el ingreso, 
indicar la cantidad de numeros a ingresar al principio del programa, o 
interrumpir la carga cuando se ingrese el numero 99.
"""

sum_count = 0
impar = False

while (entry := int(input("Enter a number ('99' to quit): "))) != 99:
    if entry % 2 == 0:
        sum_count += entry
    elif entry % 2 != 0:
        impar = True

if impar:
    print("Se ingresaron impares")
    print(f"The plus of all pairs numbers is: {sum_count}")
else:
    print(f"The plus of all pairs numbers is: {sum_count}")
