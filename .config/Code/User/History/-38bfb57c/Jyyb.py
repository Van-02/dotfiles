"""
Crear un programa que le pida al usuario 5 colores, y los guarde en un
archivo de texto llamado colores.txt
"""

with open("08/colores.txt", "w") as file:
    print("Please, enter five colours")
    for i in range(5):
        file.write(input(f"Colour {i + 1}: ") + '\n')

print("\nDone! Your 5 colors were saved in 'colores.txt'")
