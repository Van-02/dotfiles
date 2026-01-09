"""
Permita al usuario ingresar una frase. Cambie las letras a por 4 y las 
letras e por 3.
"""

phrase = input("Ingrese una frase: ")

for letter in phrase:
    if letter == "a":
        phrase[letter] = "4"
    elif letter == "e":
        phrase[letter] = "3"

print(phrase)
