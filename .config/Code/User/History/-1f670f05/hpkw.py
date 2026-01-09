"""
Tirar ahora, 2500 veces un dado de 6 caras. Mostrar el promedio de esas 
tiradas. Comparar con el promedio del ejercicio anterior. ¿Nota una diferencia
sustancial habiendo cambiado la cantidad de tiradas?
"""
import random

rolls = []

for _ in range(2500):
    rolls.append(random.randint(1, 6))

total_sum = sum(rolls)
average = total_sum / len(rolls)
print(f"The average of the 20 rolls is: {average:.2f}")

# Difference isn't very big, round like a 3.5
