"""
Se le permitira al usuario ingresar una frase. Se mostraran en pantalla 
solamente las letras en posiciones pares de la misma.
"""

phrase = input("Please enter a phrase: ")
new_phrase = ""

for i in range(len(phrase)):
    if i % 2 == 0:
        new_phrase += phrase[i]

print(new_phrase)
