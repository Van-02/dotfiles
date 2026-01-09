"""
Tirar 20 veces un dado de 6 caras. Mostrar el promedio de esas 20 tiradas.
"""
import random

rolls = []

for throw in range(20):
    rolls.append(random.randint(1, 6))

total_sum = sum(rolls)
print(f"The average is: {total_sum / len(rolls)}")
