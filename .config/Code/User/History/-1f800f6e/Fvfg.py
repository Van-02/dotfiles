"""
Permita al usuario ingresar una frase. Cambie las letras a por 4 y las 
letras e por 3.
"""

phrase = input("Ingrese una frase: ")

for i in range(len(phrase)):
    if phrase[i] == "a":
        phrase[i] = "4"
    elif phrase[i] == "e":
        phrase[i] = "3"

print(phrase)
