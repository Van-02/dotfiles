"""
Se deberan ingresar 8 notas. Se mostrara el promedio, redondeado a 2 decimales.
"""

notes = []

print("Ingrese 8 notas: ")
for i in range(8):
    note = int(input(f"{i} ->  "))
    notes.append(note)
