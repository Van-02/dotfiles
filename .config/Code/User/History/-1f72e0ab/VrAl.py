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
# Split names and append in full names data base
for i in name:
    if i != ",":
        character += i
    else:
        full_namesdb.append(character)
        character = ""

# Separate names and surnames
for full_name in full_namesdb:
    temp_db = []
    for name in full_name:
        if
