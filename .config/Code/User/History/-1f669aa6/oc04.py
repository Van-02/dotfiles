"""
Pedirle al usuario sus 10 marcas favoritas. Mostrar una marca al azar de 
la lista.
"""

print("Please, enter your 10 favourites brands of cars: ")

car_brands = []
for i in range(10):
    brand = input(f"Brand {i + 1}: ")
    car_brands.append(brand)
