"""
Realizar un programita que le pida ingresar una frase al usuario y 
coloque cada letra como elemento de una lista.
"""

phrase = input("Ingrese una frase: ")
letters = []

for char in phrase:
    letters.append(char)

print(letters)
