"""
Permita al usuario ingresar una frase. Cambie las letras a por 4 y las 
letras e por 3.
"""

phrase = input("Ingrese una frase: ")
new_phrase = ""

for letter in phrase:
    if letter != "a" and letter != "e":
        new_phrase += letter
    elif letter == "a":
        new_phrase += "4"
    elif letter == "e":
        new_phrase += "3"

print(phrase)
