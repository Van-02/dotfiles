"""
Ingresar una frase que contenga simbolos varios, ademas de mayusculas y 
minusculas mezclados. Determinar la cantidad de espacios, y cada simbolo que 
hay en la misma.
"""
import string

phrase = input("Cabecee el teclado: ")

letters = string.ascii_lowercase + string.ascii_uppercase
spaces = 0
simbol = 0

for char in phrase:
    if char not in letters and char != " ":
        simbol += 1
    elif char == " ":
        spaces += 1

print(letters)
