"""
Pedirle al usuario sus 10 marcas favoritas. Mostrar una marca al azar de 
la lista.
"""
import random

print("Please, enter your 10 favourites brands of cars: ")

car_brands = []
for i in range(10):
    brand = input(f"Brand {i + 1}: ")
    car_brands.append(brand)

print(car_brands[random.randint(0, len(car_brands))])
