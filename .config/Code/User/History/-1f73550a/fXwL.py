"""
Realizar un programita que le pida ingresar una frase al usuario y 
coloque cada letra como elemento de una lista.
"""

phrase = input("Ingrese una frase: ")
letters = []

for letter in phrase:
    letters.append(letter)

print(letters)
