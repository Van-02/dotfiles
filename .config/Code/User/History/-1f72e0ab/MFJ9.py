"""
El usuario debera poder ingresar varios nombres completos 
(ejemplo: ”Luis Perez”). 
El programa debera luego, colocar los nombres en una lista y los apellidos 
en otra.
"""

name = input("Ingrese nombres completos separados por coma: ") + ","
full_namesdb = []
names = []
surnames = []

character = ""
for i in name:
    if i != ",":
        character += i
    else:
        full_namesdb.append(character)
        character = ""

for i in full_namesdb:
    pass
