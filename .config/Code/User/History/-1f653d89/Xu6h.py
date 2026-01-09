"""
Cuenta Regresiva: Se requiere un programa que permita el ingreso de un numero
positivo y muestre en pantalla la cuenta regresiva desde el numero ingresado
hasta llegar a 0. Realizar diferentes versiones del programa, utilizando en cada
una, una estructura de bucle diferente de las que tiene disponibles en Python.
"""


number = int(input(" -> "))

if number < 0:
    print("No seas boludo")
else:
    inverted_number = list(range(0, number))
    for i in inverted_number:
        print(inverted_number[-i])
