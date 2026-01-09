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
full_names_splited = ""
names_splited_db = []

for full_name in full_namesdb:
    for char in full_name + " ":
        if char != " ":
            full_names_splited += char

        else:
            names_splited_db.append(full_names_splited)
            full_names_splited = ""

for name in range(len(names_splited_db)):
    if name % 2 == 0:
        names.append(names_splited_db[name])
    else:
        surnames.append(names_splited_db[name])

print(f"Nombres: {names}")
print(f"Apellidos: {surnames}")
