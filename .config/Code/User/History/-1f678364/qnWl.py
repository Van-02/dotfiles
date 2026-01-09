"""
Tirar 20 veces un dado de 6 caras. Mostrar el promedio de esas 20 tiradas.
"""
import random

rolls = []

for _ in range(20):
    rolls.append(random.randint(1, 6))

total_sum = sum(rolls)
average = total_sum / len(rolls)
print(f"The average of the 20 rolls is: {average:.2f}")
