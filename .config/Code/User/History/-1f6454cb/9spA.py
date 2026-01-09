"""
Permitir ingresar numeros enteros hasta que se ingrese la opcion ”s” de salir. 
Plantee primero el diseño en pseudocodigo del algoritmo e implemente luego dos 
versiones.

a) La primer implementacion funcionaria en cualquier lenguaje.

b) La segunda implementacion debera aprovechar que Python es un lenguaje dinami-
camente tipado.
"""

'''Pseudocodigo
ALGORITMO ingresarNumeros
    VARIABLES
        user_input: CADENA
    INICIO
        REPETIR
            user_input = LEER("Ingrese un número o 's' para salir")
            IMPRIMIR "Numero ingresado: " + user_input
        MIENTRAS user_input != "s"
    FIN
'''

while (entry := input("Enter a number ('s' to exit): ")) != 's':
    print(f"You entered: {entry}")
