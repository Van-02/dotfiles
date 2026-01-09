"""
Pedir dos palabras al usuario y mostrarlas en pantalla concatenadas, 
es decir, una seguida de la otra. ¿Cuales son todas las maneras en que se pueden 
mostrar concatenadas en pantalla, cadenas de caracteres? ¿Que diferencia hay 
entre mostrarlas una seguida de otra en pantalla, y en concatenarlas?
"""

# Example 1
word_1 = input("Ingrese la primera palabra: ")
word_2 = input("Ingrese la segunda palabra: ")

print(word_1 + word_2)

# Example 2

print(f"{word_1}{word_2}")

# Example 3

print("{}{}".format(word_1, word_2))
