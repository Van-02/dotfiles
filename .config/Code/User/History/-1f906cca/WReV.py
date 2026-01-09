"""
Pida una frase al usuario, controle que tenga una longitud total mayor a 5 
caracteres. Muestre en pantalla los primeros 3 caracteres de la misma.
"""

phrase = input("Ingrese una frase: ")

if len(phrase) < 5:
    print("Ingrese una frase mayor a 5 caracteres")

else:
    print(phrase[:3])
