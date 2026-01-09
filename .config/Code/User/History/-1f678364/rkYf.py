"""
Tirar 20 veces un dado de 6 caras. Mostrar el promedio de esas 20 tiradas.
"""
import random

dice = []

for throw in range(20):
    dice.append(random.randint(1, 6))

print(dice)
