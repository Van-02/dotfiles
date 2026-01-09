"""
Realizar un programita que le pida ingresar una frase al usuario y coloque 
cada palabra de la misma como elemento de una lista.
"""
phrase = input("Ingrese una frase: ")
words = []
word = ""

for char in phrase:
    if char != " ":
        word += char
    elif char == " ":
        words.append(word)
        word = ""

words.append(word)

print(words)
