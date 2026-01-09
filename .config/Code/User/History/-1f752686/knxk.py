"""
Se le pediria al usuario una frase. Se mostraran en pantalla, una palabra 
por linea de la misma. *no usar listas en este ejercicio.
"""

phrase = input("Ingrese una frase: ")
word = ""

for letter in phrase:
    if letter != " ":
        word += letter
    elif letter == " ":
        print(word)
        word = ""

print(word)
