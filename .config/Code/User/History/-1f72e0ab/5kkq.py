"""
El usuario debera poder ingresar varios nombres completos 
(ejemplo: ”Luis Perez”). 
El programa debera luego, colocar los nombres en una lista y los apellidos 
en otra.
"""

raw_input = input("Ingrese nombres completos separados por coma: ") + ","
full_names = []
first_names = []
last_names = []

# Split names and append in full names data base
current_full_name = ""
for char in raw_input:
    if char != ",":
        current_full_name += char
    else:
        full_names.append(character)
        character = ""

# Separate names and surnames
full_names_splited = ""
word_buffer = []

for full_name in full_names:
    for char in full_name + " ":
        if char != " ":
            full_names_splited += char

        else:
            word_buffer.append(full_names_splited)
            full_names_splited = ""

for name in range(len(word_buffer)):
    if name % 2 == 0:
        first_names.append(word_buffer[name])
    else:
        last_names.append(word_buffer[name])

print(f"Nombres: {first_names}")
print(f"Apellidos: {last_names}")
