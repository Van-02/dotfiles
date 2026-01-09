"""
Pedirle al usuario sus 10 marcas favoritas. Mostrar una marca al azar de 
la lista.
"""
import random

print("Please, enter your 10 favorite car brands: ")

car_brands = []
for i in range(10):
    brand = input(f"Brand {i + 1}: ")
    car_brands.append(brand)

selected_brand = random.choice(car_brands)
print(f"The randomly selected brand is: {selected_brand}")
