"""
Se le permitira al usuario ingresar una frase. Se mostraran en pantalla 
solamente las letras en posiciones pares de la misma.
"""

phrase = input("Please enter a phrase: ")
new_phrase = ""

for i in range(0, len(phrase), 2):
    new_phrase += i

print(new_phrase)
