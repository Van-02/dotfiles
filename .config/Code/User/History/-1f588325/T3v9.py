"""
El problema es el siguiente, el usuario debera poder ingresar la longitud 
de la base de una piramide y el algoritmo debera imprimir en pantalla una 
piramide de numerales. Por ejemplo, si se ingresa 7, se deberia ver en pantalla:

a) Diseñe el algoritmo que imprima ese triangulo, en pseudocodigo.

b) Determine que restricciones deberia contemplar para que el triangulo quede 
bien formado. ¿Cualquier valor para la longitud de la base servira?

c) Implemente el programa en Python a partir del pseudocodigo creado.
   #
  ###
 #####
#######
"""

'''Pseudocodigo
ALGORITMO DibujarPiramide
    VARIABLES
        base, i, espacios, numerales: ENTERO
    INICIO
        LEER base
        PARA i DESDE 1 HASTA base CON PASO 2 HACER
            espacios = (base - i) / 2
            numerales = i
            IMPRIMIR " " multiplicado por espacios
            IMPRIMIR "#" multiplicado por numerales
            NUEVA_LINEA
        FIN_PARA
    FIN
'''
"""
b) Restricciones (Constraints)

Para que la pirámide sea simétrica y perfecta como la del ejemplo, existen dos 
restricciones clave:
   - Números Impares (Odd Numbers): La base debe ser un número impar. Si la base 
   fuera par (ej. 4), no habría un "punto medio" exacto para el primer #, y la 
   punta quedaría descentrada o plana (##).

   - Números Positivos: La base debe ser mayor a 0.
"""

base_lenght = int(input("Enter a base pyramide: "))

if base_lenght % 2 != 0 and base_lenght > 0:
    for i in range(1, base_lenght + 1, 2):
        padding = (base_lenght - i) // 2
        print(" " * padding + "#" * i)
else:
    print("Error: Please enter a positive odd number to keep the pyramid symmetrical.")
