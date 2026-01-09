"""
Realizar un programa que permita ingresar dos palabras y determine si tienen la 
misma longitud o no. Mostrar un mensaje en pantalla en cada caso. Misma longitud,
una menor, o una mayor.
"""

word_1 = input("Ingrese la primera palabra: ")
word_2 = input("Ingrese la segunda palabra: ")

if len(word_1) == len(word_2):
    print("Tienen la misma cantidad de caracteres")

elif len(word_1) > len(word_2):
    print(f"La palabra {word_1} tiene mas caracteres.")

elif len(word_1) < len(word_2):
    print(f"La palabra {word_2} tiene mas caracteres.")
