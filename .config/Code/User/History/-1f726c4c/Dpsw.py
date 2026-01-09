"""
Se deberan ingresar 8 notas. Se mostrara el promedio, redondeado a 2 decimales.
"""

notes = []

print("Insert 8 notes: ")
for i in range(8):
    note = int(input(f"{i} ->  "))
    notes.append(note)

count = 0
for note in notes:
    count += note

promedy = count / len(notes)
