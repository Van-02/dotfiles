"""
Pedir el nombre al usuario, y corroborar si ese nombre existe entre los 
nombres de usuarios validos guardados en una lista.
"""

name = input("Ingrese su nombre: ")
namesdb = ["Jinx", "Vi", "Caitlyn", "Jayce", "Ambessa", "Mel"]

if name in namesdb:
    print("Este nombre existe")
else:
    print("Este nombre no existe")
