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

base = int(input("Enter a base: "))

for i in range(1, base + 1, 2):
    space = ' ' * ((base - i) // 2)
    print(space + "#" * i)
