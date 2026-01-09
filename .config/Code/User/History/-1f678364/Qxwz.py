"""
Tirar 20 veces un dado de 6 caras. Mostrar el promedio de esas 20 tiradas.
"""
import random

dice = []

for throw in range(20):
    dice.append(random.randint(1, 6))

total_sum = sum(dice)
print(f"The average is: {total_sum / len(dice)}")
