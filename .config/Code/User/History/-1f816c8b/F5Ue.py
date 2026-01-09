"""
Se le permitira al usuario ingresar una frase. Se mostraran en pantalla 
solamente las letras en posiciones pares de la misma.
"""

phrase = input("Please enter a phrase: ")
filtered_phrase = ""

for i in range(len(phrase)):
    if i % 2 == 0:
        filtered_phrase += phrase[i]

print(f"Original: {phrase}")
print(f"Characters at even positions: {filtered_phrase}")

phrase = input("Please enter a phrase: ")

even_chars = phrase[::2]

print(f"Filtered result: {even_chars}")
